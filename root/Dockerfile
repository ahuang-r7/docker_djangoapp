FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update -q && apt-get upgrade -y \ 
    && apt-get autoremove \ 
    && apt-get autoclean
RUN apt-get install -y \
    libffi-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools \
    vim

ARG PROJECT=root
ARG PROJECT_DIR=~/Users/ahuang/Documents/root

RUN mkdir /app
WORKDIR /app

RUN pip install pipenv
ONBUILD COPY ./Pipfile* Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock
ONBUILD RUN set -ex && pipenv install --system

ADD . /app

EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python3.6", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

