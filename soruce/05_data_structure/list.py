#리스트 슬라이싱
cities = ["서울", "부산", "대구"]
cities.extend(["대전", "광주", "울산", "인천"])
print(cities)

tour_list = cities[1:5]
print(tour_list)

visited_list = cities[:4]
print(visited_list)

to_go = cities[4:]
print(to_go)

to_go = cities[-3:]
print(to_go)

score = [94, 86, 92, 63, 88, 75, 52, 72, 98]
print(score)
score[3:-2] = [65, 89, 78, 54]
print(score) 

#리스트 함축
s = [x**2 for x in range(10)]
print(s)

list1 = [3, 4, 5]
list2 = [2*x for x in list1]
print(list2)

evenNum = [x for x in range(21) if x % 2 == 0]
print(evenNum)

word_list = ["Every", "bad", "thing", "has", "its", "end."]
item = [words[0] for words in word_list]
print(item)

word_list = "Every bad thing has its end.".split()
word_list = [len(w) for w in word_list]
print(word_list)

#리스트 활용

#최댓값 찾기
score = [36, 78, 55, 49, 68, 64, 80, 93, 88, 80]
maxScore = score[0]
for x in range(1, len(score)):
    if score[x] > maxScore:
        maxScore = score[x]

print(maxScore)

#조건을 만족하는 항목 모두 찾기
score = [36, 78, 55, 49, 68, 64, 80, 93, 88, 84]
excellent = []
for value in score:
    if value >= 80:
        excellent.append(value)

print(excellent)

#filter 함수 사용
score = [36, 78, 55, 49, 68, 64, 80, 93, 88, 84]
excellent = list(filter(lambda x : x >= 80, score))
print(excellent)

#내장 순차 자료형 함수
def times2x(x):
    return 2*x

numList = [1, 2, 3, 4, 5]
newList = []
for n in numList:
    newList.append(times2x(n))
print(newList)

newList2 = map(times2x,numList)
print(list(newList2))

fl = [3.6, 4.3, 7.8, 9.2, 10.5, 8.7]
il = list(map(int,fl))
print(il)

intList = [x for x in range(10)]
strList = list(map(str, intList))
print(strList)
