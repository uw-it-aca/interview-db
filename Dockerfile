ARG DJANGO_CONTAINER_VERSION=1.4.1

FROM gcr.io/uwit-mci-axdd/django-container:${DJANGO_CONTAINER_VERSION} as app-container

USER root

RUN apt-get update && apt-get install libpq-dev -y
RUN /app/bin/pip install psycopg2

USER acait

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker/ /app/project/

RUN /app/bin/pip install -r requirements.txt


RUN . /app/bin/activate && \
  python manage.py collectstatic --noinput && \
  python manage.py compress -f

FROM gcr.io/uwit-mci-axdd/django-test-container:${DJANGO_CONTAINER_VERSION} as app-test-container

COPY --from=app-container /app/ /app/
COPY --from=app-container /static/ /static/
