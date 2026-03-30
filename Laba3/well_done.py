import time

# СТАРАЯ ВЕРСИЯ split
def split_old(lst, n):
    res = []
    for i in range(n):
        res.append([])
    for i in range(len(lst)):
        res[i % n].append(lst[i])
    return res

# НОВАЯ ВЕРСИЯ split (быстрее)
def split_new(lst, n):
    res = []
    for i in range(n):
        res.append(lst[i::n])
    return res

# СТАРАЯ ВЕРСИЯ calc
def calc_old(n):
    v = [0, 0, 1.5]
    if n <= 3:
        return v[n-1]
    for i in range(4, n+1):
        new = (i+1)/(i*i+1)*v[i-2] - v[i-3]*v[i-4]
        v.append(new)
    return v[n-1]

# НОВАЯ ВЕРСИЯ calc (быстрее)
def calc_new(n):
    if n == 1 or n == 2:
        return 0
    if n == 3:
        return 1.5
    a, b, c = 0, 0, 1.5
    for i in range(4, n+1):
        d = (i+1)/(i*i+1)*c - b*a
        a, b, c = b, c, d
    return c

# ПРОВЕРКА
print("Проверка split:")
print("Старая:", split_old([1,2,3,4,5], 2))
print("Новая: ", split_new([1,2,3,4,5], 2))
print()

print("Проверка calc:")
for i in range(1, 7):
    print("v"+str(i)+"=", calc_new(i))
print()

# ТЕСТ СКОРОСТИ
lst = list(range(10000))

start = time.time()
for _ in range(100):
    split_old(lst, 5)
t1 = time.time() - start

start = time.time()
for _ in range(100):
    split_new(lst, 5)
t2 = time.time() - start

print("split ускорение:", round(t1/t2, 1), "раз")

start = time.time()
for _ in range(100):
    calc_old(1000)
t1 = time.time() - start

start = time.time()
for _ in range(100):
    calc_new(1000)
t2 = time.time() - start

print("calc ускорение:", round(t1/t2, 1), "раз")