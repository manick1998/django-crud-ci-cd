# Use official Python image as base
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the current project files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run database migrations
RUN python manage.py migrate

# Expose the port on which Django runs
EXPOSE 8000

# Use Gunicorn as the production WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "crud_project.wsgi:application"]
