FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apk update && apk add --no-cache tini

RUN pip install --upgrade pip --root-user-action ignore
RUN pip install pipenv --root-user-action ignore

COPY ./Pipfile* ./
RUN pipenv install --system

COPY ./compose/local/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME /app
EXPOSE 8000

ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]
