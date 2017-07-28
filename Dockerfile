FROM python:3-alpine

# Pillow image libs
RUN apk add --no-cache --virtual build-dependencies postgresql-dev make gcc \
    g++ ca-certificates zlib-dev jpeg-dev tiff-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev libxml2-dev libxslt-dev libffi-dev

ENV PYTHONUNBUFFERED 1
#ENV DJANGO_SETTINGS_MODULE "cutetube.settings_prod"

RUN mkdir /app

ADD requirements.txt /app/
ADD src/ /app/

WORKDIR /app

RUN pip install -r requirements.txt

ADD docker-entrypoint.sh /docker-entrypoint.sh

#ENV DJANGO_SETTINGS_MODULE "cutetube.settings_prod"

# Gunicorn - 8000
#EXPOSE 8000

# start gunicorn
#CMD ["gunicorn", "cutetube.wsgi:application", "-b :8000"]
