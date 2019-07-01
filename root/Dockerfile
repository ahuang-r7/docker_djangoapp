FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

ARG PROJECT=root
ARG PROJECT_DIR=~/Users/ahuang/Desktop/docker_djangoapp/root

ADD requirements.txt /app
RUN pip install -q -r requirements.txt uwsgi
RUN pip install tcell_agent

ADD . /app

EXPOSE 8000
STOPSIGNAL SIGINT

CMD ./entrypoint.sh.uwsgi

