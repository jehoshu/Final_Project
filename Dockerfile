# Use an official Python runtime as the base image
FROM python:latest

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the script file
COPY project.py .

# Run the script using environment variables
CMD ["python", "project.py", "$REPO_TO_CLONE", "$BRANCH_TO_MERGE"]