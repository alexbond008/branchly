import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging(log_dir: str = "data/logs", level: int = logging.INFO) -> logging.Logger:
    """Configure root logging for the application.

    - Creates the log directory if necessary
    - Adds a rotating file handler and a console handler
    - If logging is already configured (handlers present), returns the root logger unchanged.
    """
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger()
    # Avoid adding duplicate handlers on repeated imports
    if logger.handlers:
        return logger

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")

    logfile = os.path.join(log_dir, "branchly.log")
    file_handler = RotatingFileHandler(logfile, maxBytes=5 * 1024 * 1024, backupCount=5)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.setLevel(level)

    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console)

    return logger


__all__ = ["setup_logging"]
