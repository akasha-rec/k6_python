# input() : 문자열 입력받을 때 사용
# split() : 문자를 나눌 때 사용. ()안의 구분자 기준으로 문자열을 나눔
# type() : 데이터 타입 확인
# 문자열끼리 더하면 문자열 연결만 됨
# A, B = input().split()
# # type() 확인 습관화해야

# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
A, B = input().split()
A, B = int(A), int(B)
# / : 결과 float. // : 결과 int
print(A+B, A-B, A*B, A//B, A%B, sep="\n")

