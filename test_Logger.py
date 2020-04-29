from singleton_logger import Logger

myLogger = Logger("singleton_logger.log")
myLogger.info(type(myLogger))
myLogger.warn("This is your first warning!")