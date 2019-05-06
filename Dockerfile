FROM acait/django-container:feature-refactor

USER root
RUN apt-get update && apt-get install mysql-client -y
USER acait

ADD --chown=acait:acait setup.py /app/
ADD --chown=acait:acait requirements.txt /app/

RUN . /app/bin/activate && pip install -r requirements.txt
ADD --chown=acait:acait . /app/

ADD --chown=acait:acait docker /app/project/

CMD ["/start.sh" ]
