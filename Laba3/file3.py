def calc1(n):
    v = [0, 0, 1.5]  
    if n == 1:
        return 0
    if n == 2:
        return 0
    if n == 3:
        return 1.5
    for i in range(4, n + 1):
        new_v = (i + 1) / (i*i + 1) * v[i-2] - v[i-3] * v[i-4]
        v.append(new_v)
    return v[n-1] 
print("v1 =", calc1(1))
print("v2 =", calc1(2))
print("v3 =", calc1(3))
print("v4 =", calc1(4))
print("v5 =", calc1(5))
print("v6 =", calc1(6))