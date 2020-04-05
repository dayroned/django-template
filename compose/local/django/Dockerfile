FROM python:3

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # netcat to check when postgres is ready
  && apt-get install -y netcat \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./compose/local/django/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
