# -*- coding: utf-8 -*-

from datetime import datetime


def profiling(func):
    def profiled_function(*args, **kwargs):
        t0 = datetime.now()
        try:
            # return func(*args, **kwargs)
            yield from func(*args, **kwargs)
        finally:
            t = datetime.now()
            print(func.__name__, '-'*10, t - t0, '-'*10)
    return profiled_function
