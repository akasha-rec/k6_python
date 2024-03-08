# 2675 문자열 반복 / 1152 단어의 개수
# A = int(input().split())
#3052 나머지
n = []
for _ in range(10): # 10번 반복 _:단순 반복하겠다
    a = int(input())
    b = a % 42
    n.append(b)

s = set(n) # set으로 중복값 제거
print(len(s)) #len()으로 요소수 출력