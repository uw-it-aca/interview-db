#!/bin/bash
# Remove any existing httpd data
rm -rf /run/httpd/* /tmp/httpd*

source "/app/bin/activate"
export DATABASE_NAME=`echo $BRANCH | sed 's/-/_/g' `

if [ "$DB" = "mysql" ] && [ "$ENV" = "dev" ]
then
  mysql -u $DATABASE_USERNAME -p$DATABASE_PASSWORD -h $DATABASE_HOSTNAME --execute="create database $DATABASE_NAME "
fi

python3 manage.py migrate
python manage.py collectstatic
python manage.py compress

# Start Apache server in foreground
exec /usr/sbin/apachectl -DFOREGROUND
