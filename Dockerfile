FROM acait/django-container:feature-refactor

USER root
RUN apt-get update && apt-get install mysql-client libmysqlclient-dev -y
USER acait

ADD --chown=acait:acait interview_db/VERSION interview_db/
ADD --chown=acait:acait setup.py /app/
ADD --chown=acait:acait requirements.txt /app/

RUN . /app/bin/activate && pip install -r requirements.txt && pip install mysqlclient
RUN . /app/bin/activate && python manage.py compress && python manage.py collectstatic --no-input
ADD --chown=acait:acait . /app/

ADD --chown=acait:acait docker /app/project/

