FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the entire app directory into the container's /app directory
COPY app /app

# Expose the port that Flask will run on
EXPOSE 8000

# Start the Flask app when the container starts
CMD ["python", "main.py"]

