import logging

class LoggedDecorator:
    def __init__(self, exception, mode):
        self.exception = exception
        self.mode = mode

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except self.exception as e:
                logger = logging.getLogger(__name__)
                if self.mode == "console":
                    console_handler = logging.StreamHandler()
                    logger.addHandler(console_handler)
                elif self.mode == "file":
                    file_handler = logging.FileHandler("log.txt")
                    logger.addHandler(file_handler)
                logger.error(str(e))
        return wrapper
