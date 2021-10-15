import math
class Circle:
    pi = math.pi
    cx, cy, radius = 0., 0., 0.
    def __init__(self, cx, cy, radius):
        self.cx = cx
        self.cy = cy
        self.radius = radius

    def calLength(self):
        return 2*self.radius*self.pi

    def calArea(self):
        return self.radius**2*self.pi

c1 = Circle(0,0,5)
c2 = Circle(10,10,3)

print(c1.calLength())
print(c1.calArea())

print(c2.calLength())
print(c2.calArea())

class Ractangle:
    x1, y1, x2, y2 = 0, 0, 0, 0
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calPerimeter(self):
        return 2*(abs(self.x2 - self.x1) + abs(self.y2- self.y1))
    
    def calArea(self):
        return abs(self.x2 - self.x1) * abs(self.y2 - self.y1)

r1 = Ractangle(150,180,100,100)
print("사각형1의 둘레 =", r1.calPerimeter())
print("사각형1의 넓이 =", r1.calArea())

r2 = Ractangle(0, 0, 280, 240)
print("사각형2의 둘레 =", r2.calPerimeter())
print("사각형2의 넓이 =", r2.calArea())

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender

    def get_info(self):
        return self.name, self.age, self.gender

class Student(Person):
    def __init__(self, name, age, gender, score):
        self.name = name 
        self.age = age 
        self.gender = gender 
        self.score = score 

    def get_result(self):
        if self.score >= 70:
            return "합격"
        else:
            return "불합격"

st1 = Student("홍길동", 16, "남자", 85)
st2 = Student("박인영", 16, "여자", 68)

name, age, gender = st1.get_info()
result = st1.get_result()
print(str(age) + "세 " + gender + "인" + name + "씨" + result + "입니다.")

name, age, gender = st2.get_info()
result = st2.get_result()
print(str(age) + "세 " + gender + "인" + name + "씨" + result + "입니다.")
