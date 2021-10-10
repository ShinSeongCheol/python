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