FROM node:16.20.1-alpine3.18

WORKDIR /frontend

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3000

CMD [ "yarn", "start" ]
