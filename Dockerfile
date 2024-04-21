# Use the official Python image from the Docker Hub with Python 3.9.12
FROM python:3.9.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the entire directory into the container
COPY . /app

# Install required system packages
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Install required Python packages
RUN pip install --no-cache-dir flask tensorflow matplotlib opencv-python python-dotenv

RUN  pip install --no-cache-dir gunicorn

RUN pip install --no-cache-dir pyrebase

RUN pip install --no-cache-dir pycryptodome==3.19.0

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the Gunicorn server with 4 worker processes
CMD ["gunicorn", "--workers", "2", "--timeout", "180", "--bind", "0.0.0.0:5000", "app:app"]