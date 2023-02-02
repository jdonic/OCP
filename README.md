# OCP project
A small python project that listenes to messages on Kafka topic, processes those messages and stores them into sqlite db.


## Prerequisites
- [docker](https://docs.docker.com/engine/install/)
- [docker-compose](https://docker-docs.netlify.app/compose/install/#install-compose)
- [tox](https://pypi.org/project/tox/#description) (optional, for running tests and linters)

## Running the Project
Build the Docker images and run the containers:

`docker-compose up -d --build`

Export the env variable for kafka username and password (you will find the credentials in the doc):

`export KAFKA_USERNAME=VALUE`
`export KAFKA_PASSWORD=VALUE`

There are CLI scripts implemented to ease the usage of the application:

To run the listener a process the messages run:

`python3 app/cli.py listener`

The script will continously listen to messages on the topic and process them

To view the data store inside the DB, open a new tab and run one of the following scripts based on the table you are insterested in:

`python3 app/cli.py categories`

`python3 app/cli.py offers`

`python3 app/cli.py products`



To run the tests and linters execute:

`tox`