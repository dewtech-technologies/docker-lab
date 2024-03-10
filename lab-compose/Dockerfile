# Base Image
FROM python:3.8-slim

# Working Directory
WORKDIR /usr/src/app

# Copy the dependencies file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Command to run on container start
CMD [ "python", "./app.py" ]