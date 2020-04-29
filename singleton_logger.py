class Logger(object):
    class __SingletonLogger():
        def __init__(self, file_name):
            """Return a __SingletonLogger object whose file_name is *file_name*"""
            self.file_name = file_name

        def _write_log(self, level, msg):
            """Writes the message of type level to the file_name"""
            with open(self.file_name, "a") as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))

        def critical(self, msg):
            self._write_log("CRITICAL", msg)

        def error(self, msg):
            self._write_log("ERROR", msg)

        def warn(self, msg):
            self._write_log("WARN", msg)

        def info(self, msg):
            self._write_log("INFO", msg)

        def debug(self, msg):
            self._write_log("DEBUG", msg)

    instance = None

    def __new__(cls, file_name):
        if not Logger.instance:
            Logger.instance = Logger.__SingletonLogger(file_name)

        return Logger.instance

    def critical(self, msg):
        self.instance.critical(msg)

    def error(self, msg):
        self.instance.error(msg)

    def warn(self, msg):
        self.instance.warn(msg)

    def info(self, msg):
        self.instance.info(msg)

    def debug(self, msg):
        self.instance.debug(msg)