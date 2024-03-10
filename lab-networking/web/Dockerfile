# Base Image
FROM python:3.8-slim

# Atualiza a lista de pacotes e instala o iputils-ping
RUN apt-get update && \
    apt-get install -y iputils-ping && \
    rm -rf /var/lib/apt/lists/*

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