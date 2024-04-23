import os
from alert import AlertFetcher, AlertUploader
from logger import ErrorLogger

from dotenv import load_dotenv


def main():
    load_dotenv()
    INPUT_ELASTICSEARCH = str(os.environ.get("INPUT_ELASTICSEARCH"))
    INPUT_INDEX = str(os.environ.get("INPUT_INDEX"))
    INPUT_API_KEY = str(os.environ.get("INPUT_API_KEY"))

    QUERY = str(os.environ.get("QUERY"))

    OUTPUT_ELASTICSEARCH = str(os.environ.get("OUTPUT_ELASTICSEARCH"))
    OUTPUT_INDEX = str(os.environ.get("OUTPUT_INDEX"))
    OUTPUT_API_KEY = str(os.environ.get("OUTPUT_API_KEY"))

    ERROR_LOGFILE = str(os.environ.get("ERROR_LOGFILE"))

    error_logger = ErrorLogger(ERROR_LOGFILE, 4096, 5)

    try:
        fetcher = AlertFetcher(
            INPUT_ELASTICSEARCH, verify_certs=False, api_key=INPUT_API_KEY
        )
        uploader = AlertUploader(
            OUTPUT_ELASTICSEARCH, verify_certs=False, api_key=OUTPUT_API_KEY
        )

        alerts = fetcher.fetch(INPUT_INDEX, QUERY)

        alerts = [alert["_source"] for alert in alerts]

        uploader.upload(OUTPUT_INDEX, alerts)

    except Exception as e:
        error_logger.log(str(e))


if __name__ == "__main__":
    main()
