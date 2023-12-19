FROM python:3.11.0-slim-bullseye

# You can optionally define the environment variable.
ENV MONGO_INITDB_ROOT_USERNAME=admin \
    MONGO_INITDB_ROOT_PASSWORD=password

RUN mkdir -p /home/app

# Set the working directory
WORKDIR /home/app

# Copy your application code into the container
COPY . /home/app

# Install dependencies if needed
# Example: RUN pip install -r requirements.txt

# Expose the port that your Flask application will run on
EXPOSE 3000

# Define the default command to run when the container starts
CMD flask run --host=0.0.0.0 --port=3000
