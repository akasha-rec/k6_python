# 파이썬에서 list는 [element, element, element] 모양으로
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
# print(bicycles[4]) 배열 범위에서 벗어나서 오류

# index -1 : 항상 마지막 요소 반환 > 길이를 정확히 알지 못할 때 마지막 요소로 접근
print(bicycles[-1])
print(bicycles[-2])

# f"문자열 {변수}" : formatting + list 요소 접근
message = f"My first bicycle was a {bicycles[-1].title()}"
print(message)

motorcycles = ["honda", "yamaha","suzuki"]
print(motorcycles)

# 수정하기
motorcycles[-1] = "kia"
print(motorcycles)

# 추가하기 : append
motorcycles.append("ducati")
print(motorcycles)

# 원하는 위치에 삽입하기 : insert(index, value)
motorcycles.insert(2, "hyundai")
print(motorcycles)

# 제거하기 : del
# 제거한 요소 접근 불가
del motorcycles[0]
print(motorcycles)

# 제거한 요소 재접근
# pop으로 요소 제거 > 마지막 요소 제거 동시에 해당 요소 반환
# pop(i) = 인덱스 i에 위치한 요소 제거
motorcycles = ["honda", "yamaha","suzuki"]
popped_motorcycles = motorcycles.pop(1)
print(motorcycles)
print(f"the last owned motor was a {popped_motorcycles.title()}")

motorcycles = ["honda", "ducati", "yamaha","suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

cars = ["bmw", "audi", "toyota", "subaru"]
# cars.sort() 내림차순
# print(cars)
# cars.sort(reverse = True) 오름차순
print(cars)
# 임시 정렬 sorted(변수)
print(sorted(cars, reverse=True))
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
# 요소 수 구하기
print(len(cars))
print(cars[-1])