#!/bin/bash

export SQLALCHEMY_URL="postgresql://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_DATABASE"
export SQLALCHEMY_URL_STRING="sqlalchemy.url = $SQLALCHEMY_URL"

sed -i "/sqlalchemy.url/c $SQLALCHEMY_URL_STRING" ./alembic.ini

while ! </dev/tcp/$DB_HOST/$DB_PORT; do sleep 1; done && echo DB_READY;

alembic revision --autogenerate -m "Added users table"
alembic upgrade head
python user_service.py
