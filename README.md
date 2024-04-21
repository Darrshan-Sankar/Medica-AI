# Media AI

Media AI is an innovative application designed to diagnose diseases in brain, eyes, and lungs scan inputs using deep learning algorithms trained on medical imaging datasets. Additionally, it aims to create an OpenMRS (Open Medical Record System) to track patient diseases and analyze disease trends.

## 🌟 General Info

### Currently available for: Brain, Eyes, and Lungs
### 🧠 Brain Diseases Classification
The brain diseases classification in Media AI includes the following categories:

- Glioma
- Benign Tumor
- Normal (Non-affected)

### 👀 Eye Diseases Classification
Media AI can classify the following eye diseases:

- Normal
- Cataract
- Glaucoma
- Diabetic Retinopathy

### 🫁 Lung Diseases Classification
The lung diseases classification covers the following conditions:

- Bacterial Pneumonia
- Corona Virus Disease (COVID-19)
- Normal
- Tuberculosis
- Viral Pneumonia

### 📊 Dataset Details

Media AI relies on curated medical imaging datasets to train its machine learning models. Here are the details of the datasets used:

#### Eyes Dataset
- Contains images of eyes with classes including Normal, Cataract, Glaucoma, and Diabetic Retinopathy.
- [Eyes Diseases Classification Dataset](https://www.kaggle.com/datasets/gunavenkatdoddi/eye-diseases-classification)

#### Lungs Dataset
- Contains images of lungs with classes including Bacterial Pneumonia, Corona Virus Disease, Normal, Tuberculosis, and Viral Pneumonia.
- [Lungs Disease Dataset](https://www.kaggle.com/datasets/omkarmanohardalvi/lungs-disease-dataset-4-types)

#### Brain Dataset
- Contains images of brain scans with classes including Glioma, Benign Tumor, and Normal.
- [Multi Cancer Brain MRI Dataset](https://www.kaggle.com/datasets/mdrabbaniuvce/multi-cancer)
- Additional Normal Brain MRI Images: [Brain MRI Images Dataset](https://www.kaggle.com/datasets/babaraliuser/brain-mri-images-dataset)

#### 🚀 Motivation
The motivation behind the Media AI project is to leverage machine learning and image processing techniques to enhance medical diagnostics. By automating disease detection processes, Media AI aims to improve the efficiency and accuracy of diagnoses, leading to better patient outcomes.

### 🎯 OpenMRS Implementation
In addition to disease diagnosis, Media AI implements an OpenMRS system to store patient diseases data. This enables healthcare providers to track patient health records, analyze disease trends, and make informed decisions regarding treatment and resource allocation.

### 🧠 Why Media AI?
Media AI stands out for its ability to accurately diagnose diseases using advanced machine learning techniques. By automating the diagnosis process and implementing an OpenMRS system, Media AI offers a comprehensive solution for healthcare providers to improve patient care and optimize healthcare management.

#### ⚡ Challenges
Developing Media AI poses challenges such as dataset collection, model training, and system integration. However, overcoming these challenges will lead to a powerful tool for medical diagnostics and healthcare management.


## Prerequisites

Before setting up Medica, ensure you have completed the following prerequisites:

### Firebase Setup
1. Create a Firebase project with Authentication, Realtime Database, and Storage Bucket enabled.
2. Obtain the Firebase API credentials, including the API key, auth domain, database URL, project ID, storage bucket, messaging sender ID, app ID, and measurement ID.
3. Fill in the `.env` file with the Firebase API credentials.

## Native Setup:(On-machine)

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Darrshan-Sankar/Medica-AI.git
```

### Step 2: Create an .env file with the given template

This ``.env`` file has all the environment variables to run the application.
Use the setup made in pre-requisites to fill this file

### Step 3: Make necessary setup:

Set-up an environment to run the application:

### Windows

#### Environment Setup
1. Download and nstall Python 3.9.12 from the official website: [Python Downloads](https://www.python.org/downloads/)
2. Open Command Prompt and navigate to the project directory.
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    ```bash
    venv\Scripts\activate
    ```

#### Package Installation
5. Install required Python packages:
    ```bash
    pip install flask tensorflow matplotlib opencv-python python-dotenv
    pip install pyrebase
    pip install pycryptodome==3.19.0

    ```

#### Running the Application
6. Run the Flask application:
    ```bash
    python -m flask run
    ```

### Linux

#### Environment Setup
1. Install Python 3.9.12:
    ```bash
    sudo apt-get update
    sudo apt-get install python3.9
    ```
2. Open Terminal and navigate to the project directory.
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

#### Package Installation
5. Install required Python packages:
    ```bash
    pip install flask tensorflow matplotlib opencv-python python-dotenv
    pip install pyrebase
    pip install pycryptodome==3.19.0

    ```

#### Running the Application
6. Run the Flask application:
    ```bash
    python -m flask run
    ```

### macOS

#### Environment Setup
1. Install Python 3.9.12 using Homebrew:
    ```bash
    brew install python@3.9
    ```
2. Open Terminal and navigate to the project directory.
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

#### Package Installation
5. Install required Python packages:
    ```bash
    pip install flask tensorflow matplotlib opencv-python python-dotenv
    pip install pyrebase
    pip install pycryptodome==3.19.0
    ```

#### Running the Application
6. Run the Flask application:
    ```bash
    python -m flask run
    ```

## Docker Setup

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Darrshan-Sankar/Medica-AI.git
```
### Step 2: Create an .env file with the given template

This ``.env`` file has all the environment variables to run the application.
Use the setup made in pre-requisites to fill this file

### Step 3: Build the Docker Image

Navigate to the project directory and build the Docker image using the provided Dockerfile:

```bash
docker build -t medica .
```

### Step 4: Run the Docker Container

Once the image is built, you can run the Docker container with the following command:

```bash
docker run -p 5000:5000 medica
```

The application will be accessible at `http://localhost:5000`.
