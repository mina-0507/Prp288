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
    return (n + 1) / (n*n + 1) * v1 - v2 * v3
print("v1 =", calc2(1))
print("v2 =", calc2(2))
print("v3 =", calc2(3))
print("v4 =", calc2(4))
print("v5 =", calc2(5))
print("v6 =", calc2(6))