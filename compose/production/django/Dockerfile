FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set work directory
WORKDIR /app

# Install system dependencies
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock
RUN pipenv install --system --deploy

# copy entrypoint.sh -- from the local folder
COPY ./compose/local/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# copy start.sh
COPY ./compose/production/django/start.sh /start.sh
RUN chmod +x /start.sh

# copy project
COPY . /app

# run entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
