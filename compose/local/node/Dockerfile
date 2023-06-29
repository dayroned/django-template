FROM node:18-alpine

ENV NODE_ENV=development

WORKDIR /app

COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

RUN npm install

COPY . /app

CMD ["npm", "run", "tailwind:watch"]
