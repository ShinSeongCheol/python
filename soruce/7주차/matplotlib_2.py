import numpy as np
import matplotlib.pyplot as plt

randArr1 = np.random.randint(10)
print(randArr1)

randArr1 = np.random.randint(10,100)
print(randArr1)

import numpy.random as rd
randArr1 = rd.randint(10, 100)
print(randArr1)

#random.rand(n) 함수 : [0, 1) 사이의 실수형 난수 n개를 균일한 분포로 취하여 배열 생성
randArr1d = rd.rand(20)
randArr2d = rd.rand(20).reshape(4, 5)
print(randArr1d)
print(randArr2d)

#np.random.randn(n) 표준 정규 분포 (평균:0, 표준편차:1, 평균을 중심으로 좌우대칭 종모양)를 따르는 n개의 실수 선택하여 numpy arrya를 생성
randnArr1d = rd.randn(50)
randnArr2d = rd.randn(50).reshape(10, 5)
print(randnArr2d)

x = [x for x in range(1, 11)]
#10 이상 50미만의 임의의 정수 열 개를 원소로 가지는 리스트 생성
y = [np.random.randint(10, 50) for i in range(len(x))]
plt.xticks(x)
plt.bar(x, y)
#plt.show()

x = [x for x in range(1, 11)]
y1 = [rd.randint(10,50) for i in range(len(x))]
y2 = [rd.randint(10,50) for i in range(len(x))]
plt.xticks(x)
plt.bar(x, y1, color = 'y', width = 0.3)
plt.bar(x, y2, color = 'g', width = 0.3)
#plt.show()

#원형 그래프 그리기
expenditure = [300000, 150000, 100000, 70000, 30000, 250000]
item = ['A', 'B', 'C', 'D', 'E', 'F']

#plt.pie(expenditure, labels = item, autopct = '%.2f%%')
#plt.legend()
#plt.show()

#expenditure = [300000, 150000, 100000, 70000, 30000, 250000]
#item = ['A', 'B', 'C', 'D', 'E', 'F']
#plt.pie(expenditure, labels = item, autopct = '%.2f%%', startangle = 90)
#plt.legend()
#plt.show()

plt.pie(expenditure, labels = item, autopct = '%.2f%%', startangle = 90, shadow = True, explode = (0.1, 0, 0.1, 0, 0, 0))
plt.legend()
plt.show()
