#!/usr/bin/python
# -*- Coding: utf-8 -*-
import time

def Fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fib(n - 1)+Fib(n - 2)

if __name__ == '__main__':
    start = time.time()
    print([Fib(n) for n in range(1, 45)])
    result_time = time.time() - start
    print ("result_time: {0}".format(result_time) + " sec")
