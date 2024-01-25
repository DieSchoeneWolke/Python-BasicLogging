#https://www.youtube.com/watch?v=TjSKSfMKQ_I

import logging

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s | %(levelname)s | %(message)s", filename="logs.txt")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs.txt")
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger = logging.getLogger()
logger.debug("Debug")
logger.info("Info")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")

