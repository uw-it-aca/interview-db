# interview-db

[![Build Status](https://github.com/uw-it-aca/interview-db/workflows/Build%2C%20Test%20and%20Deploy/badge.svg?branch=main)](https://github.com/uw-it-aca/interview-db/actions)
[![Coverage Status](https://coveralls.io/repos/github/uw-it-aca/interview-db/badge.svg?branch=main)](https://coveralls.io/github/uw-it-aca/interview-db?branch=main)


App to collect and tag interview data, artifacts, and stories for publishing using the Django Admin app.


## Installation
Prerequisites

1. Install [docker](https://docs.docker.com/get-docker/)
2. Install [docker-compose](https://docs.docker.com/compose/install/)
3. Clone project with
    3.1. ```$ git clone git@github.com:uw-it-aca/interview-db.git``` (SSH)
    3.2. ```$ git clone https://github.com/uw-it-aca/interview-db.git``` (HTTPS)
4. Go into your interview-db folder

        $ cd interview-db
        
5. For development checkout the `develop` branch

        $ git checkout develop

Start a server:
1. With default port (8000)

        $ docker-compose up --build

2. With custom port

        $ RUNSERVER_PORT=<custom port> docker-compose up --build

Create a super user for /admin access:

    $ docker exec -it interview-db_app_1 /bin/bash
    $ . bin/activate
    $ python manage.py createsuperuser
       <Create the superuser>
    $ exit
