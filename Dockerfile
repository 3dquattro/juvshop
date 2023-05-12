FROM python:3
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

COPY ./requirements.txt /app

# Install all requirements
RUN pip install -r requirements.txt

# Copy project
COPY . /app
VOLUME /app/storage
VOLUME /app/static

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]