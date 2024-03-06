current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# prompt = "\n당신이 방문했던 도시의 이름을 입력해주세요"
# prompt += "\n(quit을 눌러주세요)"
# while True:
#     city = input(prompt)

#     if city == "quit":
#         break
#     else:
#         print(f"나는 {city.title()}가 너무 좋았어요!")

# a = [1, 2, 3]
# b = []
# N = len(a)

# for _ in range(N): # for _ in a:
    # p = a.pop()
    # b.append(p)

# print(a)
# print(b)

a = [1, 2, 3]
b = []
N = len(a)

# while 0 < N:
#     p = a.pop()
#     b.append(p)
#     N -= 1
# print(a)
# print(b)

while True:
    if not a: break
    p = a.pop()
    b.append(p)
print(a)
print(b)

d1 = {}
d1["정원"] = list(map(int, input().split()))
print(d1)