import pytest

def split1(lst, n):
    result = []
    for i in range(n):
        result.append([])
    for i in range(len(lst)):
        result[i % n].append(lst[i])
    return result

def split2(lst, n, i=0, res=None):
    if res is None:
        res = []
        for j in range(n):
            res.append([])
    if i >= len(lst):
        return res
    res[i % n].append(lst[i])
    return split2(lst, n, i + 1, res)

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

def test_split1_2():
    assert split1([1, 2, 3, 4, 5], 2) == [[1, 3, 5], [2, 4]]

def test_split1_3():
    assert split1([1, 2, 3, 4, 5], 3) == [[1, 4], [2, 5], [3]]

def test_split1_empty():
    assert split1([], 3) == [[], [], []]

def test_split1_one():
    assert split1([1], 3) == [[1], [], []]

def test_split2_2():
    assert split2([1, 2, 3, 4, 5], 2) == [[1, 3, 5], [2, 4]]

def test_split2_3():
    assert split2([1, 2, 3, 4, 5], 3) == [[1, 4], [2, 5], [3]]

def test_split_consistency():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for n in [1, 2, 3, 4, 5]:
        assert split1(lst, n) == split2(lst, n)

def test_calc1_1():
    assert calc1(1) == 0

def test_calc1_2():
    assert calc1(2) == 0

def test_calc1_3():
    assert calc1(3) == 1.5

def test_calc2_1():
    assert calc2(1) == 0

def test_calc2_2():
    assert calc2(2) == 0

def test_calc2_3():
    assert calc2(3) == 1.5

def test_calc1_v4():
    expected = 7.5 / 17
    assert abs(calc1(4) - expected) < 0.0000001

def test_calc_consistency():
    for n in range(1, 10):
        assert abs(calc1(n) - calc2(n)) < 0.0000001

if __name__ == "__main__":
    print("=" * 50)
    print("ЗАПУСК ТЕСТОВ")
    print("=" * 50)