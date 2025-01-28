# wows_stats/wowsstats_logging.py

# python modules
import logging
import sys
import os

# local logging config file
import logging.config


DEFAULT_LOG_LEVEL = 'INFO'
DEFAULT_LOG_FILE = 'wowsstats.log'
def setup_logging(log_level=DEFAULT_LOG_LEVEL):
    config_file = os.path.join(os.path.dirname(__file__), 'logging.config')

    if os.path.exists(config_file):
        logging.config.fileConfig(config_file, disable_existing_loggers=False)
    else:
        logging.basicConfig(level=getattr(logging, log_level.upper(), logging.INFO),
                            format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                            datefmt='%d.%m.%Y %H:%M:%S',
                            stream=sys.stderr)

    # Add file handler explicitly
    file_handler = logging.FileHandler(DEFAULT_LOG_FILE, 'a')
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
    root_logger = logging.getLogger()
    root_logger.addHandler(file_handler)

    # Explicitly set the log level for the root logger and all other loggers
    log_level_value = getattr(logging, log_level.upper(), logging.INFO)
    root_logger.setLevel(log_level_value)
    for logger_name in logging.root.manager.loggerDict:
        logging.getLogger(logger_name).setLevel(log_level_value)


def debug_logging():
    root_logger = logging.getLogger()
    print(f"Root logger level: {logging.getLevelName(root_logger.level)}")
    for logger_name in logging.root.manager.loggerDict:
        logger = logging.getLogger(logger_name)
        print(f"Logger '{logger_name}' level: {logging.getLevelName(logger.level)}")