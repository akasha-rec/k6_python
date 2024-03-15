#문 11021 A+B - 7
case = int(input())

for i in range(1, case+1):
    a, b = map(int, input().split())
    sum = a+b
    print(f"Case #{i}: {sum}")

#문 11021 A+B - 8
case = int(input())

for i in range(1, case+1): #1 ~ case까지 출력
    a,b  = map(int, input().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")

# 문2438 별 찍기-1
case = int(input())

for i in range(1, case+1):
    print(i * "*")

# 문 2439 별 찍기 -2
case = int(input())

for i in range(1, case+1):
    print(" " * (case-i) + "*" * i)

#문10952 A+B - 5
a, b = map(int, input().split())
while (a > 0 and b > 0): #파이썬에서는 &&, || > and, or 사용
    a, b = map(int, input().split())
    print(a+b)
    if (a == 0 and b == 0):
        break

a, b = map(int, input().split())
while (a > 0 and b > 0): #파이썬에서는 &&, || > and, or 사용
    print(a+b)
    a, b = map(int, input().split())
    if (a == 0 and b == 0):
        break