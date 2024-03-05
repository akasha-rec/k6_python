from car import ElectricCar

my_leaf = ElectricCar("nissan", "leaf", 2024)
print("전기차는 {}".format(my_leaf.get_descriptive_name()))
my_leaf.battery_size.describe_battery()
print(f"전기차는 {my_leaf.get_descriptive_name()}")