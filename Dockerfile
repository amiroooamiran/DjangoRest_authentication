# Use the official Python image as the base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /django_authenticated

# Copy and install Python dependencies first
COPY requirements.txt /django_authenticated/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /django_authenticated

# Clean up unnecessary files (optional)
# RUN rm -rf /var/lib/apt/lists/*

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]