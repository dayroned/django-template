# Stage 1: Build frontend assets using Node.js
FROM node:18-alpine as frontend-build

ENV NODE_ENV=production

WORKDIR /app

COPY package*.json ./
RUN npm clean-install

COPY . .

RUN npm run tailwind:build

# Stage 2: Setup the Python environment and copy the built frontend assets
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

COPY --from=frontend-build /app .

COPY ./compose/production/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]
