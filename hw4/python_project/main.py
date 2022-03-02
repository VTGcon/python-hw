import random
import time, threading, multiprocessing, math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fib_func(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    ans = [1, 1]
    for i in range(n - 1):
        ans.append(ans[-1] + ans[-2])
    return ans


if __name__ == '__main__':
    # easy
    fout = open("easy.txt", 'w')
    cur_time = time.time_ns()
    random_args = [random.randint(50000, 100000) for i in range(10)]
    threads = []
    for i in range(10):
        t = threading.Thread(target=fib_func, args=(random_args[i],))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    new_time = time.time_ns()
    print(new_time - cur_time, file=fout)
    cur_time = time.time_ns()
    multiprocessings = []
    for i in range(10):
        m = multiprocessing.Process(target=fib_func, args=(random_args[i],))
        m.start()
        multiprocessings.append(m)
    for m in multiprocessings:
        m.join()
    new_time = time.time_ns()
    print(new_time - cur_time, file=fout)

