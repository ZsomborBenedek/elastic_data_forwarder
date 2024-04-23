FROM python:3.11-slim

WORKDIR /forwarder

COPY ./app/requirements.txt /forwarder/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r app/requirements.txt

COPY ./app /forwarder/app
COPY ./assets /forwarder/assets
COPY ./logs /forwarder/logs

CMD [ "python3", "app/main.py" ]
