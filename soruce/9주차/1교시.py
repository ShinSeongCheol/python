import numpy as np
import pandas as pd

#pandas 자료구조
#Series
#DataFrame

#Series
#일련의 자료를 담을 수 있는 1차원 배열과 같은 자료구조로, SeRies의 실제 데이터는 numpy의 1차원 array구조로 저장

#Series의 생성
#정수형 인덱스를 갖는 시리즈의 생성

sc = pd.Series([96, 88, 100, 68])
print(sc)

#시리즈 객체는 색인과 값을 갖는다.
#시리즈의 색인 확인
print(sc.index)

#시리즈의 값 확인
print(sc.values)

#문자열을 이용한 색인
obj = pd.Series([96, 88, 100, 69], index=['a', 'b', 'c', 'd'])
print(obj)

#사전 구조를 이용한 시리즈의 생성
dic = {'a' : 96, 'b':88, 'c':100, 'd':68}
obj = pd.Series(dic)
print(obj)

score = pd.Series([96, 88, 100, 68], index=['김은서', '박민철', '정윤주', '홍길동'])
print(score)

#색인을 이용한 데이터 검색
print(score['정윤주'])
print(score[2])

#색인을 이용한 데이터 수정
score['박민철'] = 85
print(score)

#특정 조건을 만족하는 값을 가진 데이터 검색
##점수가 80점 이상인 데이터들을 검색하여 출력
print(score[score>=80])

#Series 요소의 연산
##pandas 데이터 객체의 모든 요소에 한꺼번에 스칼라 연산이 가능하다.
obj1 = pd.Series([1, 3, 5, 7, 9])
obj2 = obj1 * 2
print(obj2)

##pandas객체에 numpy함수를 적용할 수 있다.
obj1 = pd.Series([1,3,5,7,9])
obj2 = np.sqrt(obj1)
print(obj2)

#코로나19 데이터를 이용한 Series연습
##사전을 이용한 시리즈의 생성
###2021-04-19
covid19 = {'서울' : 35628, '대구' : 9176, '경기' : 31946, '경북' : 3843, '안천' : 5488, '광주' : 2295, '충남': 2886, '부산' : 4670}
covid_19 = pd.Series(covid19)
print(covid_19)

covid_19 = pd.Series([35628, 9176, 31946, 3843, 5488, 2295, 2886, 4670], index=['세울', '대구', '경기', '경북', '안천', '광주', '충남', '부산'])
print(covid_19)

##색인 변경
covid_19.index = ['서울', '대구', '경기', '경북', '인천', '광주', '충남', '부산']
covid_19 = covid_19.rename({'세울' : '서울', '안천' : '인천'})
print(covid_19)

covid_19.name = '2021-04-19 COVID19 확진자수'
covid_19.index.name = '지역'
print(covid_19)

#DataFrame
##numpy의 2차원 array와 유사

#DataFrame의 생성
##DataFrame: 엑셀의 표와 같은 형식의 자료구조
data = {'지역' : ['서울', '대구', '경기', '경북', '인천', '광주', '충남', '부산'],
    '2020-10-19' : [5702, 7142, 4869, 1573, 999, 502, 505, 571],
    '2021-04-19' : [35628, 9176, 31946, 3843, 5488, 2295, 2886, 4670]
    }
covid_19f = pd.DataFrame(data)
covid_19f.name = '2020년 10월고 ㅏ2021년 4월의 COVID19 확진자수 비교'
print(covid_19f)

##'지역'칼럼을 인덱스로 사용
covid_19f = covid_19f.set_index('지역')
print(covid_19f)

##head() 함수 : 처음 5개의 행만 출력
print(covid_19f.head(3))

##사전에 없는 값을 넘기면 결측치로 저장
co210419 = pd.DataFrame(covid_19f, columns=['2021-04-19', '격리해제', '사망', '완치율'])
print(co210419)

##칼럼명 변경
co210419 = co210419.rename({'2021-04-19' : '확진'}, axis=1)
print(co210419)

##결측치를 가진 칼럼에 값을 대입
co210419['격리해제'] = 0
co210419['사망'] = 0
co210419['완치율'] = 0
print(co210419)

co210419['격리해제'] = [324643, 4009, 28842, 3515, 5210, 2207, 2652, 4009]
co210419['사망'] = [443, 219, 570, 77, 58, 21, 36, 121]
print(co210419)

##완치율 계산
co210419['완치율'] = co210419['격리해제']/co210419['확진']
print(co210419)

##DataFrame의 전치 (행과 열을 뒤집음)
print(co210419.T)
co210419 = co210419.astype({'확진' : 'Int32', '격리해제' : 'Int32', '사망' : 'Int32'})
print(co210419.T)

#DataFrame 편집
##재색인
obj_s = pd.Series(np.arange(5.0), index=['d', 'b', 'a', 'c', 'e'])
print(obj_s)

obj_s = obj_s.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj_s)

##drop메서드를 이용한 행 또는 열 삭제
###한개의 행 삭제
obj_new = obj_s.drop('c')
print(obj_new)
###두 개 이상의 행 삭제
obj_new = obj_new.drop(['b', 'd'])
new_co210419 = co210419.drop('인천')
print(new_co210419)
###DataFrame의 행 삭제 = 충남, 광주, 인천
new_co210419 = co210419.drop(['충남', '광주', '인천'])
print(new_co210419)
###DataFrame 열 삭제 - '사망'
new_co210419 = new_co210419.drop('사망', axis=1)
print(new_co210419)

##
