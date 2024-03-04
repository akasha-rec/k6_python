#함수의 매개변수로 함수 전달하기

def ten_times(func):
    for i in range(5):
        func()

def print_hello():
    print("Hello")

ten_times(print_hello)

def print_work():
    print("coding")

ten_times(print_work)

#func, parameter 모두 전달
def add(x, y):
    return x+y

def minus(x, y):
    return x-y

def apply_operation(operation, x, y):
    return operation(x, y)

result = apply_operation(add, 3, 4)
result2 = apply_operation(minus, 4, 3)
print(f"add 결과 : {result}, minus 결과 : {result2}")

#map(), filter() 함수
#> map(함수, 데이터) : 머신러닝, 딥러닝 때 사용
#>> filter(함수, 데이터)

# def power(item):
#     return item * item

# def under_three(item):
#     return item < 3

#lambda
power = lambda x: x*x
under_three = lambda x: x < 3

lst = [1, 2, 3, 4, 5]
map_list = map(power, lst)
print(f"map() 함수 적용결과 : {list(map_list)}")

filter_list = filter(under_three, lst)
print(f"filter() 함수 적용결과 : {list(filter_list)}")

