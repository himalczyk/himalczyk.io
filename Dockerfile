FROM python:3.11-slim-bookworm

WORKDIR /app

ARG NODE_MAJOR=18

RUN apt-get update \
  && apt-get install -y \
      ca-certificates \
      curl \
      gnupg \
      libpq-dev \
      gcc \
      python3-dev \
      postgresql-client \
  && mkdir -p /etc/apt/keyrings \
  && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
  && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" \
       | tee /etc/apt/sources.list.d/nodesource.list \
  && apt-get update \
  && apt-get install -y nodejs \
  && npm install -g npm \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && useradd --create-home python \
  && chown python:python -R /app

USER python

COPY --chown=python:python requirements*.txt ./

RUN pip install -r requirements.txt

ENV DEBUG="${DEBUG}" \
    PYTHONUNBUFFERED="true" \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python" \
    NODE_ENV="development"

COPY --chown=python:python . .
COPY ./portfolio_blog /app

WORKDIR /app/portfolio_blog

CMD ["python", "manage.py", "runserver"]
