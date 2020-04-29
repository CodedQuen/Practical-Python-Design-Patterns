def write_log(filename, level, msg):
    with open(filename, "a") as log_file:
        log_file.write("[{0}] {1}\n".format(level, msg))


def critical(filename, msg):
    write_log(filename, "CRITICAL", msg)


def error(filename, msg):
    write_log(filename, "ERROR", msg)


def warn(filename, msg):
    write_log(filename, "WARN", msg)


def info(filename, msg):
    write_log(filename, "INFO", msg)


def debug(filename, msg):
    write_log(filename, "DEBUG", msg)

