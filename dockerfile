# Use an official Python runtime as the base image
FROM python:3.8-slim AS base

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . /app

# Install any dependencies required for your model
RUN pip install -r requirements.txt

# This is your final image
FROM base AS final

# Set the entry point to your trained model script
CMD ["python", "untitled33.py"]
