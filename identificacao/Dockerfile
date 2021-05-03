FROM python:3.8

WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED=1

EXPOSE 5000
COPY ./identificacao ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get upgrade -y
RUN apt-get update -y
#RUN apt-get install vim -y

ENV FLASK_APP=./identifier
ENV FLASK_ENV=development

CMD  bash -c "flask run --port=5000 --host=0.0.0.0"
