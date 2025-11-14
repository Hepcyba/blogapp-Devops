# Base image
FROM python:3.9

# Working directory in container
WORKDIR /app

# Copy requirements first to use Docker cache efficiently
COPY requirements.txt .

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the project
COPY . .

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "app.py"]
