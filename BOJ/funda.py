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

# 문 10871 X보다 작은 수
# 정수 N개, 수열 A와 정수 X가 주어진다. 이 때 A에서 X보다 작은 수를 모두 출력
N, X = map(int, input().split()) #map 객체는 변수를 여러개 저장 가능
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")

# 문10818 최소 최대
N = int(input()) # 입력 받겠다.
lst = list(map(int, input().split())) #문자열로 입력받은 것을 map 함수를 사용해 int형으로 바꿔줘
print(min(lst), max(lst))

# 문 1152 단어 개수
str= input().split() #60초
print(len(str))

string = input() # 56초
print(len(string.split()))
 
#집합과 맵 > 문 10815
#데이터 50만 개, 두 수가 겹칠 일이 없다 > key로 접근 = dictionary 써라
import sys
input = sys.stdin.readline

dic = {}
#튜플 arr, arr2를 이용해서 dic으로 업데이트 > arr의 각 요소가 dic의 키로 존재하는가?
N = int(input().rstrip()) #공백으로 구분된 수에서 공백 제거 > 불필요한 공백으로 인한 오류방지
arr = tuple(map(int,input().rstrip().split())) #공백을 기준으로 분리하여 정수로 변환 후 튜플에 저장
M = int(input().rstrip())
arr2= tuple(map(int,input().rstrip().split()))

for i in range(len(arr2)): #arr2의 각 요소를 키로 가지는 dic 생성
    dic[arr2[i]] = 0

for idx in range(len(arr)): 
    if arr[idx] in dic.keys(): #arr의 요소가 dic의 키로 존재하는지 확인
        dic[arr[idx]]+=1 #존재한다면 1씩 증가

print(*dic.values()) #dic의 값을 풀어서 인자로 전달