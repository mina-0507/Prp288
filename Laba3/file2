def split2(lst, n, i=0, res=None):
    if res is None:
        res = []
        for j in range(n):
            res.append([])
    if i >= len(lst):
        return res
    res[i % n].append(lst[i])
    return split2(lst, n, i + 1, res)
print(split2([1, 2, 3, 4, 5], 2))  
print(split2([1, 2, 3, 4, 5], 3))  
