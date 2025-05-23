ARG DJANGO_CONTAINER_VERSION=2.0.8

FROM us-docker.pkg.dev/uwit-mci-axdd/containers/django-container:${DJANGO_CONTAINER_VERSION} AS app-prewebpack-container

USER root

RUN apt-get update && apt-get install libpq-dev -y
RUN /app/bin/pip install psycopg2

USER acait

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker/ /app/project/

RUN /app/bin/pip install -r requirements.txt

# latest node + ubuntu
FROM node:lts AS node-base
FROM ubuntu:latest AS node-bundler
COPY --from=node-base / /

ADD ./package.json /app/
WORKDIR /app/
RUN npm install .

ADD . /app/

ARG VUE_DEVTOOLS
ENV VUE_DEVTOOLS=$VUE_DEVTOOLS
RUN npm run build

FROM app-prewebpack-container AS app-container

COPY --chown=acait:acait --from=node-bundler /app/interview_db/static /app/interview_db/static

RUN . /app/bin/activate && python manage.py collectstatic --noinput

FROM us-docker.pkg.dev/uwit-mci-axdd/containers/django-test-container:${DJANGO_CONTAINER_VERSION} AS app-test-container

ENV NODE_PATH=/app/lib/node_modules
COPY --from=app-container /app/ /app/
COPY --from=app-container /static/ /static/
