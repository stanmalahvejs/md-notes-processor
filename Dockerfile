FROM python:3.13.1-alpine

RUN apk add --no-cache npm \
    && npm install markdownlint-cli2 --global

COPY scripts /scripts

ENTRYPOINT ["python"]