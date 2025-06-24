# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY health_check.py .

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "health_check.py"]
