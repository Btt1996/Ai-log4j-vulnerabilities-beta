# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the required files to the container
COPY requirements.txt .
COPY main.py .
COPY run.sh .

# Install the necessary dependencies
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make the run script executable
RUN chmod +x run.sh

# Set environment variable for the URL
ENV WEBSITE_URL=http://example.com

# Run the script when the container starts
CMD ["./run.sh", "$WEBSITE_URL"]
