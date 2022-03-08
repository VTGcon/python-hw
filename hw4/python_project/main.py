import math
import multiprocessing
import random
import threading
import time
import concurrent.futures as pool


def fib_func(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    ans = [1, 1]
    for i in range(n - 1):
        ans.append(ans[-1] + ans[-2])
    return ans


def integrate_part(f, a, b, n_iter):
    start = time.time()
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return [acc, f"[{a}, {b}] starts in {start}\n"]


def integrate(f, a, b, n_jobs=1, n_iter=1000):
    n_iter = int(n_iter / n_jobs)
    step = (b - a) / n_jobs
    acc = 0
    log = f"start work: n_jobs={n_jobs}, start={time.time()}\n"
    executor = pool.ProcessPoolExecutor(max_workers=3)
    jobs = [executor.submit(integrate_part, f, a + i * step, a + (i + 1) * step, n_iter)
            for i in range(n_jobs)]
    for job in pool.as_completed(jobs):
        result = job.result()
        acc += result[0]
        log += result[1]
    fout = open("medium_logs.txt", 'w')
    print(log, file=fout)
    return acc


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
    # medium
    for n_jobs in range(1, 2 * multiprocessing.cpu_count()):
        time_start = time.time_ns()
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        time_end = time.time_ns()
        fout = open("medium.txt", 'a')
        print(f"n_jobs={n_jobs} {time_end - time_start}\n", file=fout)
