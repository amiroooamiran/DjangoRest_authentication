# Use the official Python image as the base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Set the working directory in the container
WORKDIR /authenticated

# Copy and install Python dependencies first
COPY requirements.txt /authenticated/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /authenticated

# Clean up unnecessary files (optional)
# RUN rm -rf /var/lib/apt/lists/*

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]