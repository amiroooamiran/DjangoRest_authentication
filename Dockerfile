# Use the official Python image as the base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install build dependencies
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libc-dev \
    linux-headers \
    python3-dev \
    build-base

# Set the working directory in the container
WORKDIR /django_authenticated

# Copy and install Python dependencies first
COPY requirements.txt /django_authenticated/requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /django_authenticated

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]