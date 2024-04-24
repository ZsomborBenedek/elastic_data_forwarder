# Elastic Alert Forwarder

### Usage

```sh
python3 app/main.py .env
```

Via Docker:
```sh
docker build -t elkalertforwarder --rm . && docker run \
    --env-file .env \
    -v ./logs/:/forwarder/logs \
    -v ./assets:/forwarder/assets elkalertforwarder
```
