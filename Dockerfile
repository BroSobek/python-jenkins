# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies specified in requirements.txt
# If you have any dependencies, uncomment the following line
# RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container launches
CMD [ "ls" ]
