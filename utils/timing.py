import time
from functools import wraps


def timing(func):
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        return *result, duration
    return wrapper