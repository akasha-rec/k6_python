# input() : 문자열 입력받을 때 사용
# split() : 문자를 나눌 때 사용. ()안의 구분자 기준으로 문자열을 나눔
# type() : 데이터 타입 확인
# 문자열끼리 더하면 문자열 연결만 됨
# A, B = input().split()
# # type() 확인 습관화해야

# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
A, B = input().split()
A, B = int(A), int(B)
# / : 나눗셈 결과 float. // : 결과 int
print(A+B, A-B, A*B, A//B, A%B, sep="\n")

# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
A, B =input().split()
A, B =int(A), int(B)
if(A >B):
    print(">")
elif(A <B):
    print("<")
else:
    print("==")

# 단계별로 문제 풀기 > 조건문 > 시험성적
A = int(input())
if (A > 89):
    print("A")
elif (A > 79):
    print("B")
elif (A > 69):
    print("C")
elif (A > 59):
    print("D")
else:
    print("F")

# s = input() "1 2"
# a, b = s.split() "1" "2"
# a, b = int(a), int(b) 1 2

# 문 2739 구구단
a = int(input())
for i in range(1, 10):
    print(a, "*", i, "=", a*i)

# 문 8393 합
n = int(input())
sum = 0

for a in range(1, n+1):
    sum+=a
print(sum)

# 별 찍기
n = int(input())

for i in range(1, n+1):
    print(" "*(n-i)+"*"*i)

# X보다 작은 수
    
# 최소 최대
N = int(input())
lst = list(map(int, input().split()))
print(min(lst), max(lst))

# 문 1152 단어 개수
N = input().split()
print(N, len(N))

