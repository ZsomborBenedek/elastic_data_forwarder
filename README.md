# Elastic Alert Forwarder

### Usage

```sh
docker build -t elkalertforwarder --rm .
docker run --env-file .env -v ./logs/:/code/logs elkalertforwarder 
```
