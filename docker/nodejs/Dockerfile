FROM node:16-alpine

USER root
EXPOSE 8080

ENV NODE_ENV=development

RUN npm install -g @vue/cli
RUN yarn install --save-dev

CMD ["tail", "-f", "/dev/null"]