FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y supervisor \
    && apt-get install -y postgresql-client \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -U pip

COPY ./requirements.txt /usr/src/

RUN pip install -r /usr/src/requirements.txt

COPY ./image_storage/ /usr/src/
