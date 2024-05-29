# interview-db

[![Build Status](https://github.com/uw-it-aca/interview-db/workflows/Build%2C%20Test%20and%20Deploy/badge.svg?branch=main)](https://github.com/uw-it-aca/interview-db/actions)
[![Coverage Status](https://coveralls.io/repos/github/uw-it-aca/interview-db/badge.svg?branch=main)](https://coveralls.io/github/uw-it-aca/interview-db?branch=main)


App to collect and tag interview data, artifacts, and stories for publishing using the Django Admin app.

## System Requirements

- Python (3+)
- Docker
- Node

## Development Stack

- Django (4.2)
- Vue (3.2)
- Vite (3.1)
- Vitest (0.23.2)

## Design Stack

- Bootstrap (5.2)
- Bootstrap Icons (1.10.1)

## Installation

Clone the repository

        $ git clone git@github.com:uw-it-aca/interview-db.git

Go to your working directory

        $ cd interview-db

Copy the sample .env file so that your environment can be run.

        $ cp .env.sample .env

Update any .env variables for local development purposes

## Development (using Docker)

Docker/Docker Compose is used to containerize your local build environment and deploy it to an 'app' container which is exposed to your localhost so you can view your application. Docker Compose creates a 'devtools' container - which is used for local development. Changes made locally are automatically syncd to the 'app' container.

        $ docker-compose up --build

View your application using your specified port number in the .env file

        Demo: http://localhost:8000/

### Loading data (inside the container)
To load sample interview data and collection models, you can call respectively:
        $ bin/python manage.py loaddata /app/interview_db/fixtures/interview.json

        $ bin/python manage.py loaddata /app/interview_db/fixtures/collections.json

## Testing

### Front-end Testing (using Vitest)

Run Vitest test scripts and generate coverage report

        $ npm run test
        $ npm run coverage

### Linting (using ESLint and Stylelint)

Run ESLint for JS linting

        $ npm run eslint

Run Stylelint for CSS linting

         $ npm run stylelint

### Python Testing (using Django)

Run unittest

        $ docker compose run --rm app bin/python manage.py test

## Authors

[Univesity of Washington Teaching & Learning Systems](https://github.com/uw-it-aca)

## License

Copyright 2024 UW Information Technology, University of Washington

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
