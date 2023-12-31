#!/usr/bin/env bash
set -e

python manage.py makemigrations
python manage.py migrate
python manage.py create_super_user
python manage.py input_initial_data

if [[ ${DJANGO_BIND_ADDRESS+x} ]] && [[ ${DJANGO_BIND_PORT+x} ]];
then
    echo "OK! Using custom ADDRESS $DJANGO_BIND_ADDRESS and PORT $DJANGO_BIND_PORT"
    python manage.py runserver ${DJANGO_BIND_ADDRESS}:${DJANGO_BIND_PORT}
else
    echo "Using 0.0.0.0:${DJANGO_BIND_PORT}"
    python manage.py runserver 0.0.0.0:${DJANGO_BIND_PORT}
fi
