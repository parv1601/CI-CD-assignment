# Dockerfile
# Use a minimal Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application and test code
COPY calculator.py .
COPY test_calculator.py .

# Define the command to run when the container starts
CMD ["python", "calculator.py"]