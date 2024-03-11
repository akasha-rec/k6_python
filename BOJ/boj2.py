#1차원 배열 - 3052 나머지
n = []
for _ in range(10): # 10번 반복 _:단순 반복하겠다
    a = int(input())
    b = a % 42
    n.append(b)

s = set(n) # set으로 중복값 제거
print(len(s)) #len()으로 요소수 출력

#반복문 - 문 15552 빠른 A+B
import sys

inp = int(sys.stdin.readline()) #inp = int(input())
for i in range(inp):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

#집합과 맵 > 문 10815
#데이터 50만 개, 두 수가 겹칠 일이 없다
N = int(input())
card = set(map(int, input().split()))
M = int(input())
compare_card = set(map(int, input().split()))

for i in compare_card:
    if i in card:
        print(1, end = " ")
    else:
        print(0, end = " ")

#정렬 - 2750 수 정렬하기