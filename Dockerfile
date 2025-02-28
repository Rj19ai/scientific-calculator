# Use official Python base image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Set entrypoint to run the calculator script
ENTRYPOINT ["python3", "sc_calculator.py"]
