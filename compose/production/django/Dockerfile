# Stage 1: Build frontend assets using Node.js
FROM node:18-alpine AS frontend-build

ENV NODE_ENV=production

WORKDIR /app

COPY ./package*.json ./
RUN npm clean-install

COPY . .

RUN npm run tailwind:build

# Stage 2: Setup the Python environment and copy the built frontend assets
FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apk update && apk add --no-cache tini

RUN pip install --upgrade pip --root-user-action ignore
RUN pip install pipenv --root-user-action ignore

COPY ./Pipfile* ./
RUN pipenv install --system --deploy

COPY --from=frontend-build /app .

COPY ./compose/production/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]
