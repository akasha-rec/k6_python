import car as c #파일을 import한 경우

my_mustang = c.Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())
my_leaf = c.ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())