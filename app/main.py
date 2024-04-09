import os
from app.alert import AlertFetcher, AlertUploader
from app.logger import ErrorLogger


def main():
    INPUT_ELASTICSEARCH = str(os.environ.get("INPUT_ELASTICSEARCH"))
    INPUT_INDEX = str(os.environ.get("INPUT_INDEX"))
    INPUT_API_KEY = str(os.environ.get("INPUT_API_KEY"))

    OUTPUT_ELASTICSEARCH = str(os.environ.get("OUTPUT_ELASTICSEARCH"))
    OUTPUT_INDEX = str(os.environ.get("OUTPUT_INDEX"))
    OUTPUT_API_KEY = str(os.environ.get("OUTPUT_API_KEY"))

    ERROR_LOGFILE = str(os.environ.get("ERROR_LOGFILE"))

    error_logger = ErrorLogger(ERROR_LOGFILE, 4096, 5)

    try:
        fetcher = AlertFetcher(INPUT_ELASTICSEARCH, INPUT_API_KEY, verify_certs=True)
        uploader = AlertUploader(
            OUTPUT_ELASTICSEARCH, OUTPUT_API_KEY, verify_certs=False
        )

        alerts = fetcher.fetch(INPUT_INDEX, "query.json")
        result = uploader.upload(OUTPUT_INDEX, alerts)

        print(result)

    except Exception as e:
        error_logger.log(str(e))


if __name__ == "__main__":
    main()
