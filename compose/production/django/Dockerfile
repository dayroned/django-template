# Stage 1: Build frontend assets using Node.js
FROM node:18-alpine as frontend-build

WORKDIR /app

ENV NODE_ENV=production

COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

RUN npm clean-install --only=production

COPY . /app

RUN npm run tailwind:build

# Stage 2: Setup the Python environment and copy the built frontend assets
FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apk update && apk add --no-cache gcc musl-dev libffi-dev

RUN pip install --upgrade pip && pip install pipenv

COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock

RUN pipenv install --system --deploy

COPY ./compose/local/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/production/django/start.sh /start.sh
RUN chmod +x /start.sh

COPY --from=frontend-build /app /app

EXPOSE 5000

ENTRYPOINT ["/entrypoint.sh"]
