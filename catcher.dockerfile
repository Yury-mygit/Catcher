# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the application code into the container
COPY . /code/



# Set the entry point for the container
CMD ["python", "catcher/manage.py", "runserver", "0.0.0.0:80"]
#CMD ["python", "catcher/manage.py", "runserver"]
