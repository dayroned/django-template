FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apk update && apk add --no-cache tini gcc musl-dev libffi-dev

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock
RUN pipenv install --system --deploy

COPY ./compose/local/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME /app
EXPOSE 8000

ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]
