import time
import sys
sys.setrecursionlimit(100000)

def split1(lst, n):
    result = []
    for i in range(n):
        result.append([])
    for i in range(len(lst)):
        result[i % n].append(lst[i])
    return result


def split1_optimized(lst, n):
    return [lst[i::n] for i in range(n)]


def split2(lst, n, i=0, res=None):
    if res is None:
        res = []
        for j in range(n):
            res.append([])
    if i >= len(lst):
        return res
    res[i % n].append(lst[i])
    return split2(lst, n, i + 1, res)


def split2_optimized(lst, n, start=0, res=None):
    if res is None:
        res = [[] for _ in range(n)]
    if start >= len(lst):
        return res
    
    CHUNK_SIZE = 100
    end = min(start + CHUNK_SIZE, len(lst))
    
    for i in range(start, end):
        res[i % n].append(lst[i])
    
    return split2_optimized(lst, n, end, res)


def calc1(n):
    v = [0, 0, 1.5]
    if n == 1:
        return 0
    if n == 2:
        return 0
    if n == 3:
        return 1.5
    for i in range(4, n + 1):
        new_v = (i + 1) / (i * i + 1) * v[i - 2] - v[i - 3] * v[i - 4]
        v.append(new_v)
    return v[n - 1]


def calc1_optimized(n):
    if n <= 2:
        return 0.0
    if n == 3:
        return 1.5
    
    a, b, c = 0.0, 0.0, 1.5
    d = 0.0
    
    for i in range(4, n + 1):
        d = (i + 1) / (i * i + 1) * c - b * a
        a, b, c = b, c, d
    
    return d


def calc2(n):
    if n == 1:
        return 0
    if n == 2:
        return 0
    if n == 3:
        return 1.5
    v1 = calc2(n - 1)
    v2 = calc2(n - 2)
    v3 = calc2(n - 3)
    return (n + 1) / (n * n + 1) * v1 - v2 * v3


def calc2_optimized(n, cache=None):
    if cache is None:
        cache = {1: 0.0, 2: 0.0, 3: 1.5}
    if n in cache:
        return cache[n]
    cache[n] = ((n + 1) / (n * n + 1)) * calc2_optimized(n - 1, cache) \
               - calc2_optimized(n - 2, cache) * calc2_optimized(n - 3, cache)
    return cache[n]


print("=" * 55)
print("РЕЗУЛЬТАТЫ ПРОИЗВОДИТЕЛЬНОСТИ ПРОГРАММ")
print("=" * 55)


lst_large = list(range(50000))
n_splits = 300

t1 = time.time()
split1(lst_large, n_splits)
t1 = time.time() - t1

t2 = time.time()
split1_optimized(lst_large, n_splits)
t2 = time.time() - t2

print(f"\n1. split1:           {t1:.4f} сек")
print(f"   split1_optimized: {t2:.4f} сек ---> ускорение {t1/t2:.1f}x")



lst_rec = list(range(5000))
n_splits_rec = 300

t3 = time.time()
split2(lst_rec, n_splits_rec)
t3 = time.time() - t3

t4 = time.time()
split2_optimized(lst_rec, n_splits_rec)
t4 = time.time() - t4

print(f"\n2. split2:           {t3:.4f} сек")
print(f"   split2_optimized: {t4:.4f} сек ---> ускорение {t3/t4:.1f}x")



n_calc = 8000000

t5 = time.time()
calc1(n_calc)
t5 = time.time() - t5

t6 = time.time()
calc1_optimized(n_calc)
t6 = time.time() - t6

print(f"\n3. calc1:            {t5:.2f} сек")
print(f"   calc1_optimized:  {t6:.2f} сек ---> ускорение {t5/t6:.1f}x")



n_calc2 = 30

t7 = time.time()
calc2(n_calc2)
t7 = time.time() - t7

t8 = time.time()
calc2_optimized(n_calc2)
t8 = time.time() - t8

print(f"\n4. calc2:            {t7:.4f} сек")
print(f"   calc2_optimized:  {t8:.4f} сек ---> ускорение {t7/t8:.1f}x")