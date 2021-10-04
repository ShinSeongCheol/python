square = lambda x : x**2
print(square(4))

add = lambda x, y: x + y
print(add(5,8))
print(add(8,9))

add_10 = lambda x: x + 10
print(add_10(5))

a = [5,3,8,9]
b = [11,23,7,14]
c = list(map(lambda x, y : x + y, a,b))
print(c)