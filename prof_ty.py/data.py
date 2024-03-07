#데이터 다루는 데 유리한 3가지 >> 모두 가능하면 AI
#1. data & data 변형하는 map > map(f, data)
#2. filter 조건을 만족하는 결과값만 출력 filter(f, data)
#3. 줄인다. reduce(f, data)

data = list(range(1, 11))
print(data)
square = lambda x:x**2
even = lambda x: x % 2 ==0
add = lambda a,b : a+b
print(list(map(square, data)))
print(list(filter(even, data)))
# reduce(add, data)
