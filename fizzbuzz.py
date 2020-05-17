#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys
import time
from memory_profiler import profile

def fizbuz(n):
    if n % 3 == 0 and n % 5 == 0:
        return str(n) + ': fizzbuzz'
    elif n % 3 == 0:
        return str(n) + ': fizz'
    elif n % 5 == 0:
        return str(n) + ': buzz'
    else:
        return str(n)

@profile
def main(num):
    start = time.time()
    print('\n'.join([fizbuz(n) for n in range(1, num)]))
    result_time = time.time() - start
    print ("result_time: {0}".format(result_time) + " sec")


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print('please input Arguments')
    else:
         main(int(args[1]))