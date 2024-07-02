# Use an official Python runtime as a parent image
FROM python:3.9-slim


# Set up application directory
WORKDIR /src

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ./app/* ./

# Expose port 8080
EXPOSE 8080

# Command to run the Flask application
CMD ["python", "app.py"]
