FROM python:3-alpine

# Pillow image libs
RUN apk add --no-cache --virtual build-dependencies postgresql-dev make gcc \
    g++ ca-certificates zlib-dev jpeg-dev tiff-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev libxml2-dev libxslt-dev libffi-dev

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD src/ /app/
