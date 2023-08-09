FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN python3.9 -m pip install -U pip setuptools

COPY requirements /tmp/requirements

RUN python3.9 -m pip install -U --no-cache-dir -r /tmp/requirements/development.txt

COPY docker/django/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]