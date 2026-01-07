# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

RUN pip install pytest

# Copy the current directory contents into the container at /app
COPY . student1.py.

# Run the script
CMD ["python", "docker_student1.py"]