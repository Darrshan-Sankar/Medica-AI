import pyrebase
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, session
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import base64
from PIL import Image
import os
import datetime

from dotenv import load_dotenv
load_dotenv()

import collections 
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    from collections.abc import MutableMapping
else:
    from collections import MutableMapping

app = Flask(__name__)
app.secret_key = 'd@123'

# Load the model
gmodal = load_model('./models/vgg16-epc15.h5')
gindex=['Brain', 'Eyes', 'Lungs']
lmodal = load_model('./models/Lungs/VGG-res - epc15.h5')
lindex = index=['Bacterial Pneumonia', 'Corona Virus Disease', 'Normal', 'Tuberculosis', 'Viral Pneumonia']
emodal = load_model('./models/Eyes/VGG-res.h5')
eindex = index=[ 'cataract', 'diabetic _ retinopathy' , ' glaucoma ' , ' normal' ]
bmodal = load_model('./models/Brain/res-vgg-epc15.h5')
bindex = ['brain_glioma', 'brain_menin', 'brain_tumor', 'normal']

# Configure Firebase
firebase_config = {
   "apiKey": os.environ.get("FIREBASE_API_KEY"),
   "authDomain": os.environ.get("FIREBASE_AUTH_DOMAIN"),
   "databaseURL": os.environ.get("FIREBASE_DATABASE_URL"),
   "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET"),
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    # Handle sign-up logic here
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        # Create a new user in Firebase Authentication
        user = auth.create_user_with_email_and_password(email, password)

        # Store the user's information in the Firebase Realtime Database
        user_data = {
            'name': name,
            'email': email
        }
        db.child('users').child(user['localId']).set(user_data)

        flash('User created successfully', 'success')
        return redirect('/')
    except Exception as e:
        # Handle exceptions
        flash(str(e), 'error')
        return redirect('/')

@app.route('/signin', methods=['POST'])
def signin():
    # Handle sign-in logic here
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        # Sign in the user using Firebase Authentication
        user = auth.sign_in_with_email_and_password(email, password)
        # user is authenticated, store user's email in the session
        session['email'] = email
        # User is authenticated, redirect to the medical form
        return render_template('form.html')

    except Exception as e:
        # Handle exceptions
        return jsonify({'error': str(e)})

@app.route('/logout', methods=['POST'])
def logout():
    # Remove the email from the session
    session.pop('email', None)
    # Redirect to the home page
    return render_template("login.html")

@app.route('/details', methods=['POST'])
def details():
    # Get form data
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    age = request.form.get('age')
    dob = request.form.get('dob')
    gender = request.form.get('occupation')
    email = request.form.get('email')
    address = request.form.get('address')
    address2 = request.form.get('address2')
    phone = request.form.get('phone')
    post = request.form.get('post')
    city = request.form.get('city')
    upload = request.files['upload']
    uploaded = upload
    upload = upload.read()
    encoded = base64.b64encode(upload).decode('utf-8')
    img = Image.open(uploaded)
    img = img.convert()
    img = img.resize((250,250))
    mime_type = 'image/jpeg'  # Replace with the actual MIME type of your image
    data_url = f'data:{mime_type};base64,{encoded}'
    
    # # Check if the image mode is RGBA
    # if img.mode == 'RGBA':
    # Convert the image to RGB
    img = img.convert('RGB')
    
    img.save("temp.jpg")

    # Upload the temporary file to Firebase Storage
    with open("temp.jpg", "rb") as image_file:
        storage.child("images/"+firstname+lastname+".jpg").put(image_file)

    # Delete the temporary file
    os.remove("temp.jpg")

    # Process the data as needed
    x = img
    x = image.img_to_array(x)
    x = np.expand_dims(x,axis = 0)#changing the shape

    g_preds=gmodal.predict(x)
    g_pred=np.argmax(g_preds, axis=1)
    g_result = str(gindex[g_pred[0]])

    if g_result=="Brain":
        b_preds=bmodal.predict(x)
        b_pred=np.argmax(b_preds, axis=1)
        res = str(bindex[b_pred[0]])
    elif g_result=="Eyes":
        e_preds=emodal.predict(x)
        e_pred=np.argmax(e_preds, axis=1)
        res = str(eindex[e_pred[0]])
    else:
        l_preds=lmodal.predict(x)
        l_pred=np.argmax(l_preds, axis=1)
        res = str(lindex[l_pred[0]])

    # Get the current timestamp as a datetime object
    current_time = datetime.datetime.now()

    # You can format the timestamp as a string if needed
    current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
    
    dat = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age,
        "dob": dob,
        "gender": gender,
        "email": email,
        "address": address,
        "address2": address2,
        "phone": phone,
        "post": post,
        "city": city,
        "img":"images/"+res+"_"+firstname+lastname+current_time_str+".jpg"
    }

    db.child("details").push(dat)

    # Render the results page
    return render_template('result.html', firstname=firstname, lastname=lastname, age=age, dob=dob, gender=gender, email=email, address=address, address2=address2, phone=phone, post=post, city=city, upload=data_url, res=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
