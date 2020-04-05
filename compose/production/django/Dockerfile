FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock
RUN pipenv install --system --deploy --ignore-pipfile

# copy entrypoint.sh -- from the local folder
COPY ./compose/local/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# copy start.sh
COPY ./compose/production/django/start.sh /start.sh
RUN chmod +x /start.sh

# set work directory
WORKDIR /app

# copy project
COPY . .

# run docker-entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
