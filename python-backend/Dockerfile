FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy app code
COPY health_check.py .

## Install dependencies
RUN pip install --no-cache-dir flask

# Expose the port
EXPOSE 5000

# Command to run the app
CMD ["python", "health_check.py"]
