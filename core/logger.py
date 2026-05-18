import logging


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("execra")

    if logger.handlers:
        return logger  # Prevent duplicate handlers

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "[%(levelname)s] [%(asctime)s] %(name)s: %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


logger = setup_logger()