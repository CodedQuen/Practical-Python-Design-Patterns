import logger

try:
    a = 1 / 0
except:
    logger.error("object.log", "something went wrong")