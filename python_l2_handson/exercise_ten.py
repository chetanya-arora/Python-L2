from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print(f'Elapsed time: {end-start}')
        return result
    return wrapper


@timing
def f(a):
    for _ in range(a):
        pass


print(f(2000000))
