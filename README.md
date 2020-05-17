# statistics

## fib.py
- フィボナッチ数列を計算するプログラム
- 負荷を書けるときに使おうかなと思って書いた
```
$python fib.py 10
```

### memory-profilerを使ってメモリ使用量を可視化
https://pypi.org/project/memory-profiler/
```
$ mprof run fib.py {num}
$ mprof plot
```
例
![26d1221c26b9c19b65426ef67c88a212](https://user-images.githubusercontent.com/35423021/82117379-83d17c00-97aa-11ea-8c93-b26a85ff733f.png)

## fizzbuzz
```
$ python fizzbuzz.py 1000001
.
.
.
999990: fizz
999991
999992
999993: fizzbuzz
999994
999995: buzz
999996: fizzbuzz
999997
999998
999999: fizzbuzz
1000000: buzz
result_time: 121.80275917053223 sec
Filename: fizzbuzz.py

Line #    Mem usage    Increment   Line Contents
================================================
    17     40.6 MiB     40.6 MiB   @profile
    18                             def main(num):
    19     40.6 MiB      0.0 MiB       start = time.time()
    20    114.4 MiB      0.4 MiB       print('\n'.join([fizbuz(n) for n in range(1, num)]))
    21     41.3 MiB      0.0 MiB       result_time = time.time() - start
    22     41.3 MiB      0.0 MiB       print ("result_time: {0}".format(result_time) + " sec")
```
