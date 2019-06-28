FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

ARG PROJECT=root
ARG PROJECT_DIR=~/Users/ahuang/Documents/root

ADD requirements.txt /app
RUN pip install -r requirements.txt

ADD . /app

EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python3.6", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

