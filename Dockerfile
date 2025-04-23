# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the templates directory into the container at /app/templates
COPY templates /app/templates

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir flask requests

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["python", "app.py"]