import logging
from os import mkdir, path

def get_logger(module_path: str, logger_name: str):
    """
    Creates and configures a logger with the specified name and settings.

    Args:
        module_path (str): __file__ attribute of the module.
        logger_name (str): The name of the logger.

    Returns:
        logging.Logger: The configured logger object.
    """

    if not path.exists(_config.logs_dir):
        mkdir(_config.logs_dir)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    _console_handler = logging.StreamHandler()
    _file_handler = logging.FileHandler(f"{_config.logs_dir}/{logger_name}.log")
    _console_handler.setLevel(logging.DEBUG)
    _file_handler.setLevel(logging.DEBUG)
    _log_format = f'~ |%(levelname)-8s| [%(asctime)s] in {module_path}:%(lineno)d\n>>> %(message)s '
    _formatter = logging.Formatter(_log_format)
    _console_handler.setFormatter(_formatter)
    logger.addHandler(_console_handler)
    logger.addHandler(_file_handler)
    
    return logger
