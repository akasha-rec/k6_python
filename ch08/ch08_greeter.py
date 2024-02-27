#함수 만들기
def greet_user(username): #username > String > immutable
    # 독스트링 : 주석 """함수 설명"""
    """단순한 인사말을 표시합니다"""
    print(f"Hello, {username.title()}!")

greet_user("jesse") #함수 호출

#독스트링 출력 : help(함수명) / print(함수명.__doc__)
# help(greet_user)
# print(greet_user.__doc__)

def describe_pet(animal_type, pet_name):
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("hamster", "harry")
#키워드 인수 > 순서 상관X, 대신 매개변수명을 정확히 해야
describe_pet(animal_type="hamster", pet_name="harry")

#매개변수의 기본값을 지정하려면 아닌 변수를 먼저 적어줘야 한다.
def describe_pet(pet_name, animal_type="dog"):
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("wi")
describe_pet(pet_name="wi")
describe_pet(pet_name="harry", animal_type="hamster")