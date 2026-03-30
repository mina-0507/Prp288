def split1(lst, n):
    result = []
    for i in range(n):
        result.append([])
    for i in range(len(lst)):
        result[i % n].append(lst[i])
    return result
print(split1([1, 2, 3, 4, 5], 2))
print(split1([1, 2, 3, 4, 5], 3))    