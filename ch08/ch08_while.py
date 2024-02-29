# def get_formatted_name(first_name, last_name):
#     """실제 이름"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
    
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

def print_models(unprinted_designs, completed_models):
    """빈 리스트일 때까지 출력"""

    while unprinted_designs:
        current_design = unprinted_designs.pop() #마지막부터 1개씩 꺼내면 없어져
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

# 리스트가 parameter면 mutable
def show_completed_models(completed_models):
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def modify_string(s): #String 값을 전달 받았다
    #immutable 변수는 tuple, String, boolean, 숫자
    s = s + "world" #변수 s는 원래의 s가 가리키는 주소와 달라짐
    print(s)

st = "hello"
modify_string(st)
print(st) #hello 출력 > 변경 X

# def make_pizza(size, *toppings): #튜플
#     """요약 리스트"""
#     print(f"size : {size}")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")

def build_profile(first, last, **user_info):
    """사용자 정보를 딕셔너리로 저장"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("albert", "einstein", location = "princeton", field = "physics")
print(user_profile)