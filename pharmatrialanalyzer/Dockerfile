# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Expose port (if the application exposes any port for an API, optional)
# EXPOSE 8080

# Define the default command to run your example pipeline script
CMD ["python", "examples/example_pipeline.py"]
