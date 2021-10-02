def func():
    global a
    a = []
    for i in range(5):
        a.append(i)

func()
print(a)
