number = input("양의 정수를 입력 : ").split()
number = list(int(x) for x in number);

def dispEvenNum(num):
    list =[]
    for i in num:
        if i % 2 == 0:
            list.append(i)
    print(list)

dispEvenNum(number)

def detectEvenNum(num):
    list = []

    for i in num:
        if i%2 == 0:
            list.append(i)
    
    return list

EvenNumber = detectEvenNum(number)
print(EvenNumber)