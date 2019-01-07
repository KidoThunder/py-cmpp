import time


def get_string_time():
    return time.strftime('%m%d%H%M%S', time.localtime(time.time()))
