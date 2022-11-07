from time import time

def time_measurement(func):
    def time_result(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        return end - start
    return time_result