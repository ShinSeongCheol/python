#numpy 인덱싱과 슬라이싱
import numpy as np
arr = np.arange(12).reshape(3, 4)
print(arr)

#인덱싱
print("arr[1, 3] =", arr[1, 3])
print("arr[2, 3] =", arr[2][2])

#인덱싱
print("arr[1][3] = %d" % arr[1, 3])
print("arr[2, 3] = %d" % arr[2][2])

arr = np.arange(16).reshape(4, 4)
print(arr)

#슬라이싱
sub00 = arr[:2, :2]
sub01 = arr[:2, 2:]
sub10 = arr[2:, :2]
sub11 = arr[2:, 2:]
print(sub00, sub01, sub10, sub11, sep="\n")

#numpy 연산
a = np.array([2, 4, 6, 8, 10])
b = np.array([3, 5, 6, 2, 8])

hap = a + b
#hap = np.add(a, b)

#cha = a - b
cha = np.subtract(a, b)

#gob = a * b
gob = np.multiply(a, b)

#jae = a / b
jae = np.divide(a, b)

print("합 = ", hap)
print("차 = ", cha)
print("곱 = ", gob)
print("제 = ", jae)

#행렬곱
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

dotP = np.dot(a,b)
print(dotP)

#행렬 원소의 합계와 평균 계산
score = np.array([[96, 90, 92]])
print(score)

#모든 원소의 합계와 평균 계산
totalSum = np.sum(score)
totalAvg = np.mean(score)
print("전체 합계 = %d" % totalSum, "전체 평균 = %d" % totalAvg)

#과목별 합계, 평균 계산
subjSum = np.sum(score, axis=0)
subjAvg = np.mean(score, axis=0)
print(subjSum)
print(subjAvg)

#개인별 합계, 평균 계산
persSum = np.sum(score, axis=1)
persAvg = np.mean(score, axis=1)
print("개인별 합계 =", persSum)
print("개인별 평균 =", persAvg)

#numpy float 출력 옵션 - 방법 1
np.set_printoptions(precision=2)
persSum = np.sum(score, axis=1)
persAvg = np.mean(score, axis=1)
print("개인별 합계 =", persSum)
print("개인별 평균 =", persAvg)

#방법 2
np.set_printoptions(formatter={"float_kind" : lambda x: "{0:0.2f}".format(x)})
persSum = np.sum(score, axis=1)
persAvg = np.mean(score, axis=1)
print("개인별 합계 =", persSum)
print("개인별 평균 =", persAvg)