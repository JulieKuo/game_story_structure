import logging, os
from logging.handlers import TimedRotatingFileHandler


class Log():
    def __init__(self):
        self.level_dict = {
            1: logging.DEBUG,
            2: logging.INFO,
            3: logging.ERROR,
            4: logging.WARNING,
            5: logging.CRITICAL,
        }

    def set_logger(self, file_path: str = "logs/log.log", level: int = 2, freq: str = "D", interval: int = 50, backup: int = 2, name: str = "log") -> logging.Logger:
        """
        Set logger configuration

        Parameters
        ----------
        file_path : str
            Path to the log file
        level : int
            Log level (1: DEBUG, 2: INFO, 3: ERROR, 4: WARNING, 5: CRITICAL)
        freq : str
            Frequency of log rotation (D: daily, H: hourly, M: minutely)
        interval : int
            Interval of log rotation
        backup : int
            Number of backup log files
        name : str
            Name of the logger

        Returns
        -------
        logger : logging.Logger
            Logger instance
        """

        # create log folder
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # define log format and date format
        format_  = "%(asctime)s %(levelname)s %(message)s"
        time_format = "%Y-%m-%d %H:%M:%S"

        formatter = logging.Formatter(format_, time_format) # create a log formatter
        log_level = self.level_dict[level] # get log level based on the provided "level"

        # initialize the logger
        self.logger = logging.getLogger(name = name)
        self.logger.setLevel(log_level)

        # create a file handler for log rotation
        self.handler = TimedRotatingFileHandler(filename = file_path, when = freq, interval = interval, backupCount = backup, encoding = "utf-8")
        self.handler.setFormatter(formatter)

        # create a stream handler for terminal output
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(formatter)

        # add the file handler to the logger
        self.logger.addHandler(self.handler)
        self.logger.addHandler(self.stream_handler)

        return self.logger

    def shutdown(self) -> None:
        """
        Shutdown the logger
        """
        self.logger.removeHandler(self.handler)  # remove log handlers
        self.logger.removeHandler(self.stream_handler)
        del self.logger, self.handler, self.stream_handler # delete logger instances


if __name__ == "__main__":
    log = Log()
    logger = log.set_logger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.error("This is an error message")
    logger.warning("This is a warning message")
    logger.critical("This is a critical message")
    log.shutdown()