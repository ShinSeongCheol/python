def func2x(x):
    return x * 2

list2x = []

list2x = list(map(func2x, [1,3,5,7]))
print(list2x)
