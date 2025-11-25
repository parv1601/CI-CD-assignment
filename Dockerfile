# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY calculator.py .
COPY test_calculator.py .

CMD ["python", "calculator.py"]