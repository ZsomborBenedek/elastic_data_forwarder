import logging
from logging.handlers import RotatingFileHandler


class ErrorLogger:
    logger: logging.Logger
    loghandler: logging.Handler

    def __init__(self, logfile: str, max_log_size: int, backup_count: int) -> None:
        """Initialize a class for error logging.

        Args:
            logfile (str): Path of logfile.
            max_log_size (int): Max size of logfile in bytes.
            backup_count (int): Number of rotated logfiles.
        """

        log_format = "%(asctime)s - %(levelname)s - %(message)s"

        self.logger = logging.getLogger(logfile)
        self.logger.setLevel(logging.ERROR)
        self.loghandler = RotatingFileHandler(
            logfile, maxBytes=max_log_size, backupCount=backup_count
        )
        self.loghandler.setFormatter(logging.Formatter(log_format))
        self.logger.addHandler(self.loghandler)
        self.logger.addHandler(logging.StreamHandler())

    def log(self, msg: str):
        """Log an error

        Args:
            msg (str): Message to log.
        """
        self.logger.error(msg)
