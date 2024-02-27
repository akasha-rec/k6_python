#함수 만들기
def greet_user(username): #username > String > immutable
    # 독스트링 : 주석 """함수 설명"""
    """단순한 인사말을 표시합니다"""
    print(f"Hello, {username.title()}!")

greet_user("jesse") #함수 호출

#독스트링 출력 : help(함수명) / print(함수명.__doc__)
# help(greet_user)
# print(greet_user.__doc__)

