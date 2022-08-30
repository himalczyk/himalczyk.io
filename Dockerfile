FROM alpine:latest

RUN apk add --no-cache --update python3 py3-pip bash
RUN apk add --update npm
ADD requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

ADD ./portfolio_blog /opt/webapp/
WORKDIR /opt.webapp

CMD gunicorn --bind 0.0.0.0:$PORT wsgi