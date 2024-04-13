import sys
import logging
import colorlog


def get_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        stream_formatter = colorlog.ColoredFormatter(
            '%(log_color)sAPP-%(levelname)s%(reset)s:\t%(message)s',
            log_colors={
                'DEBUG': 'white',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            },
            reset=True,
            style='%'
        )

        # Make a StreamHandler if doesn't exist
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)

    return logger
