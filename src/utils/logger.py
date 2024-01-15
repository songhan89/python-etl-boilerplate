import logging
import logging.config
from logging.handlers import RotatingFileHandler
import os


# Keep log file to a max size of 1 MB and a max of 1 backup file
LOG_MAX_BYTES = 1024 * 1024
LOG_MAX_BACKUP = 1


def setup_logger():
    """
    Set up the logger configuration.
    """
    # current working directory name
    project_name = os.getcwd().split('/')[-1]

    # Import logging configuration file
    logging.config.fileConfig(fname=os.path.join(
        'config', 'log.config'), disable_existing_loggers=False)
    # Get the logger specified in the file
    f_handler = RotatingFileHandler(os.path.join('logs', 'app.log'),
                                    maxBytes=LOG_MAX_BYTES,
                                    backupCount=LOG_MAX_BACKUP)
    f_handler.setLevel(logging.DEBUG)
    logger = logging.getLogger(project_name)
    f_format = logging.Formatter('%(asctime)s - \
    %(name)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)

    return logger