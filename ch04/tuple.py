def test():
    return (10, 20)
#test(), enumerate() > tuple값 리턴
a, b = test() 
print(f"a = {a}, b = {b}")

lst = ["a", "b", "c", "d"]
for i, value in enumerate(lst):
    print(f"i = {i}, value = {value}")
