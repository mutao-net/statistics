#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys
import time
from memory_profiler import profile

def Fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fib(n - 1)+Fib(n - 2)

@profile
def main(num):
    start = time.time()
    print([Fib(n) for n in range(1, num)])
    result_time = time.time() - start
    print ("result_time: {0}".format(result_time) + " sec")

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print('please input Arguments')
    else:
         main(int(args[1]))
