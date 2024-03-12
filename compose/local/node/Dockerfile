FROM node:18-alpine

ENV NODE_ENV=development

WORKDIR /app

RUN apk update && apk add --no-cache tini

COPY package*.json ./
RUN npm install

COPY ./compose/local/node/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME /app

ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]
