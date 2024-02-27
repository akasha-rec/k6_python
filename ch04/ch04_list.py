# range 따로 설정 X > 0~n미만
for value in range(6):
    print(value)

# number = set(range(6)) > {0, 1, 2, 3, 4, 5}
# number = list(range(6)) > [0, 1, 2, 3, 4, 5]
# print(number)

# 1~9까지를 출력하는데 2씩 증가 > 홀수
numbers = list(range(1, 10, 2))
print(numbers)

# squares = [] #빈 리스트
# for value in range(1, 11):
#     square = value **2 #** 제곱
#     squares.append(square)
# print(squares)

# 위의 코드와 같은데 간결하게 표현한 것
squares = [value**2 for value in range(1, 11)]
print(squares)

#슬라이스 0~n미만
print(squares[0:3])
print(squares[:3])
print(squares[-3:]) #-3~끝까지

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_list[::-1]) #역순 출력
print(my_list[::-2]) #역순 2씩 출력 [8, 6, 4, 2]

a = [1, 2, 3, 4]
b = [3, 4]
# c = a + b #요소 합치기
# print(c)

# 정말 빼기가 되네!
# a 요소 나열한 것 중에서 b가 아닌 것만 출력
c1 = [x for x in a if x not in b]
print(c1)
c2 = list(set(a)-set(b))
print(c2)

#shallow copy (원본의 값이 바뀌면 바뀌어 = 주소값을 복사한 것일 뿐)
# a = [[1, 2, 3], [4, 5, 6]] #2차원 배열
# b = a[:]
# print(b) #[[1, 2, 3], [4, 5, 6]]
# a[0][0] = 100
# print(b)

#deep copy
a = [10, 20, 30, 40, 50]
b = a[0:3]
a[0] = 100
print(b)

players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the first three player on my team")
for player in players[:3]:
    print(player.title())

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:] #deep copy?
# friend_foods = my_foods #shallow copy?

my_foods.append("cannoli")

print(my_foods)
print(friend_foods)

#tuple : immutable(변경X)
# dimensions = (10, 20, 30, 40, 50)
# # dimensions[0] = 30
# # print(dimensions)
# for dimension in dimensions:
#     print(dimension)

#덮어쓰기는 가능
dimensions = (200, 50)
print("Original dimension")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimension : ")
for dimension in dimensions:
    print(dimension)
