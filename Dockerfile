FROM python:3-alpine

# Pillow image libs
RUN apk add --no-cache --virtual build-dependencies postgresql-dev make gcc \
    g++ ca-certificates zlib-dev jpeg-dev tiff-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev libxml2-dev libxslt-dev libffi-dev

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE "cutetube.settings_prod"

RUN mkdir /app
ADD requirements.txt /app/
ADD src/ /app/
WORKDIR /app
RUN pip install -r requirements.txt

# Static files, media files
RUN mkdir -p /static /media
# chown 777 /media ?
ENV STATIC_ROOT "/static"
ENV MEDIA_ROOT "/media"

RUN python manage.py collectstatic --noinput

VOLUME ["/static", "/media"]

# ONLY add entrypoint. This script should be run in docker-compose.py
ADD docker-entrypoint.sh /docker-entrypoint.sh
