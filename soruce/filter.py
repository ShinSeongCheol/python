#filter함수
num = [5, 12, 13, 8, 10, 9, 16]
even = list(filter(lambda x : x % 2 == 0 , num))
print(even)

#리스트 함축
sqList = list(x ** 2 for x in range(1,6))
print(sqList)

#원값과 제곱값의 순서쌍 만들기
sqTuple = list((x, x**2) for x in range(1,6))
print(sqTuple)
