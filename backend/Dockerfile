# Use an official Python runtime as a parent image
FROM python:3.10.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies using pipenv
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system

# Copy the current directory contents into the container at /app
COPY . /app/

RUN python manage.py migrate

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "main.wsgi:application", "--bind", "0.0.0.0:8000"]
