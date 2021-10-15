#Numerical Python 
#Numpy
import numpy as np
stList = ["20210000", "홍길동", "남"]
print(stList)

stList.append(4.3)
print(stList)

stArr = np.array([6, 7.5, 8, 0, 1])
print(stArr)

np.append(stArr, [4.3])
print(np.append(stArr, [4.3]))
print(stArr)

stArr = np.append(stArr,[4.3])
print(stArr)

my_arr = np.arange(1000000)
my_list = list(range(1000000))
print(my_arr)
print(my_list)

#%time for _ in range(10): my_arr2 = my_arr * 2

#%time for _ in range(10) : my_list2 = [x * 2 for x in my_list]

#numpy 배열 score의 생성과 차원 확인
score = np.array([4.8, 3.6, 3.7, 4.2, 5.0, 2.8], dtype = "float32")
print(score.ndim)
print(score.shape)
print(score.dtype)

#2차원 numpy arrya의 생성
#리스트를 numpy array로 변환
data2 = [[1,2,3,4], [5,6,7,8]]
arr2 = np.array(data2)
print(data2)
print(arr2)

print(arr2.ndim)
print(arr2.shape)
print(arr2.dtype)

#연속적인 수를 원소로 갖는 2차원 배열 생성
seq15_1d = np.arange(15)
print(seq15_1d)
seq15_2d = np.arange(15).reshape(3,5)
print(seq15_2d)

#3행 3열의 단위 행렬 생성
iA = np.identity(3)
print(iA)

#원소로 10개의 0.0을 가지고 있는 실수형의 일차원 배열 생성
a0 = np.zeros(10)
print(a0)

a1 = np.ones(10)
print(a1)

a1_5 = np.ones(5, dtype=int)
print(a1_5)
print(a1_5.dtype)

#3행 6열의 2차원 배열 생성
s = (3,6)
a0_36 = np.zeros(s)
print(a0_36)

emp = np.empty((2,3,4))
print(emp)

arrValue5_1 = np.zeros((2,3)) + 5
print(arrValue5_1)

arrValue5_2 = np.ones((2,3)) * 5
print(arrValue5_2)

arrValue5_3 = np.full((2,3), 5.0)
print(arrValue5_3)

#numpy의 데이터 형태 지정하기
arr1f = np.ones(10)
print(arr1f)

arr1i = arr1f.astype("int32")
print(arr1i)

arr1 = np.array([1,2,3], dtype="i4")
print(arr1)

arr2 = np.array([4,5,6], dtype="float64")
print(arr2.dtype)

arr3 = arr1.astype("float64")
print(arr3)

arr4 = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr4)