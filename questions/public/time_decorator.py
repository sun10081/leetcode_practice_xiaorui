# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: time_decorator
@time: 2023/11/21 12:50 PM
@desc:
"""
import timeit
from functools import wraps


def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        print(f"函数运行时间: {end_time - start_time}秒")
        return result
    return wrapper

@timer_decorator
def count():
    n = 100000
    while n:
        n -= 1


if __name__ == '__main__':
    count()