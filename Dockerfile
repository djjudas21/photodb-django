# PhotoDB
FROM python:3-alpine
LABEL maintainer "Jonathan Gazeley"

RUN apk add git

# Project Files and Settings
ARG PROJECT_DIR=/var/www/photodb
RUN mkdir -p $PROJECT_DIR
ADD . $PROJECT_DIR
WORKDIR $PROJECT_DIR
RUN pip install .

# Run migrations
RUN python manage.py migrate

# Server
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
