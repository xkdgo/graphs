# -*- coding: utf-8 -*-

from datetime import datetime


def profiling(function):
    def profiled_function(*args, **kwargs):
        t0 = datetime.now()
        try:
            # return function(*args, **kwargs)
            yield from function(*args, **kwargs)
        finally:
            t = datetime.now()
            print(function.__name__, '-'*10, t - t0, '-'*10)
    return profiled_function


