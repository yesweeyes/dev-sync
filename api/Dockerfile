FROM python:3.12

# Set working directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application files
COPY ./app /code/app

# Copy application environment variables
COPY ./.env /code/.env

# Copy alembic.ini
COPY ./alembic.ini /code/alembic.ini

# Add your entire migrations folder
COPY ./migrations /code/migrations

# Copy the entrypoint script
COPY ./setup.sh /code/setup.sh

# Make the entrypoint script executable
RUN chmod +x /code/setup.sh

# Expose the port FastAPI will run on
EXPOSE 8000

# Use the entrypoint script
ENTRYPOINT ["/code/setup.sh"]
