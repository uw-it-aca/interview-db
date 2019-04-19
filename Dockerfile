FROM acait/django-container:develop
RUN apt-get update && apt-get install mysql-client -y
RUN mkdir /app/logs
ADD interview_db/VERSION /app/interview_db/
ADD setup.py /app/
ADD requirements.txt /app/
ENV LC_ALL C.UTF-8
RUN . /app/bin/activate && pip install -r requirements.txt
ADD /docker/web/apache2.conf /tmp/apache2.conf
RUN rm -rf /etc/apache2/sites-available/ && \
    mkdir /etc/apache2/sites-available/ && \
    rm -rf /etc/apache2/sites-enabled/ && \
    mkdir /etc/apache2/sites-enabled/ && \
    rm /etc/apache2/apache2.conf && \
    cp /tmp/apache2.conf /etc/apache2/apache2.conf && \
    mkdir /etc/apache2/logs
ADD . /app/
ENV DB sqlite3
ADD docker /app/project/
ADD docker/web/start.sh /start.sh
RUN chmod +x /start.sh
RUN mkdir /static

RUN groupadd -r interview_db -g 1000 && \
    useradd -u 1000 -rm -g interview_db -d /home/interview_db -s /bin/bash -c "container user" interview_db &&\
    chown -R interview_db:interview_db /app &&\
    chown -R interview_db:interview_db /static &&\
    chown -R interview_db:interview_db /var &&\
    chown -R interview_db:interview_db /run &&\
    mkdir /var/lock/apache2 &&\
    chown -R interview_db:interview_db /var/lock/ &&\
    chown -R interview_db:interview_db /home/interview_db
USER interview_db

ENV PORT 8000
CMD ["/start.sh" ]
