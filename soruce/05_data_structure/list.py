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

#파이썬의 자료구조
#리스트, 튜플, 사전, 집합
#튜플 : 순서쌍

ractangle1 = 100, 200
print(ractangle1)

ractangle1 = (100,200)
print(ractangle1)

print(ractangle1[0])
print(ractangle1[1])

ractangle2 = (0,0), 100, 100
print(ractangle2)

ractangle3 = (100,100), (200,300)
print(ractangle3)

ract_pos = (100,100), 200, 100
print(ract_pos)
print(ract_pos[1])

circle = (200,200), 100
print(circle)

#리스트를 튜플로, 튜플을 리스트로 만들기
print("리스트를 튜플로, 튜플을 리스트로 만들기")
num = tuple(range(10))
print(num)

numList = [x for x in range(10)]
print(numList)

numTuple = tuple(numList)
print(numTuple)

newNumList = list(numTuple)
print(newNumList)

#튜플도 리스트처럼 여러 자료형을 섞어서 저장해도 된다
student = ("20210000", "홍길동", 20, 4.3)
print(student)
#튜플은 원소의 값을 변경할수 없다
#student[2] = 21
#print(student)

#중첩된 튜플
ract_pos = (100, 100), 200, 100
pos = ract_pos[0]
width = ract_pos[1]
height = ract_pos[2]
print("사각형의 시작 좌표 =", pos)
print("너비 =", width)
print("높이 =", height)

circle = (200,200), 100
center_x = circle[0][0]
center_y = circle[0][1]
radius = circle[1]
print("중심 좌표_x :", center_x)
print("중심 좌표_y :", center_y)
print("반지름 길이 :", radius)

#튜플에서 값 분리하기
ract_pos = (100, 100), 200, 100
pos, width, height = ract_pos
print("시작 좌표 =", pos, "너비 =", width, "높이 =", height)

circle = (200,200), 100
center, radisu = circle
print("중심 좌표 :", center, "반지름 길이 :", radius)

#두 변수의 값 교환
a, b = 10, 20
print(a,b)
b, a = a, b
print(a,b)

#사전
#사전 선언하기
#중괄호를 이용하여 사전을 선언
#사전 구조의 학생 성적 입력 (키 : 번호)
score1 = {1:88, 2:96, 3:73, 4:68, 5:72, 6:80}
print(score1)

score2 = {"강은미":88, "김영민":96, "도민준":73, "박현우":68, "이기쁨":72, "하지은":80}
print(score2)

score3 = dict(강은미=88, 김영민=96, 도민준=73, 박현우=68, 이기쁨=72, 하지은=80)
print(score3)

circle = {"center" : (10,10), "radius" : 5}
print(circle)

#사전의 원소에 접근
#키를 이용하여 접근한다. 순서가 없기 때문에 인덱스로는 접근할 수 없다.
print(score2["박현우"])

#3은 키이기 때문에 된다.
print(score1[3])

#사전 원소 값(value)의 변경
score1[3] = 75
score2["이기쁨"] = 78
print(score1)
print(score2)

#사전의 여러 원소를 한꺼번에 변경
score2.update(강은미=89, 하지은=83)
print(score2)

#키가 숫자일 때 update(키 : 값)
score1.update({2 : 100})
print(score1)

#사전에서 키-값 쌍의 삭제
print(score3.pop("박현우"))
print(score3)
score3["강은미"] = 100
print(score3)
del score3["강은미"]
print(score3)

#사전의 모든 키-값 삭제
score3.clear()
print(score3)

#집합
#인덱스로 접근 불가능, 순서가 정렬됨
numbers = {5, 2, 3, 5, 6, 8}
print(numbers)

#집합의 원소 추가
numbers.add(7)
print(numbers)

#집합의 원소 삭제
numbers.discard(6)
print(numbers)

#집합을 공집합으로 만들기
numbers.clear()
print(numbers)

print(len(numbers))

char = set("It_is my pleasure.")
print(char)

#집합의 연산
a = {5, 7, 3, 8, 9, 1}
b = {8, 4, 2, 3, 5, 6}
print(a | b)
print(a.union(b))
print(b.union(a))
print(a & b)
print(a.intersection(b))
print(b.intersection(a))
print(a-b)
print(b-a)