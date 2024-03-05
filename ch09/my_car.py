from car import Car

my_new_car = Car("audi", "a4", "2024")
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23 #인스턴스에 직접 수정
my_new_car.update_odometer(12) #메서드를 통한 수정
my_new_car.read_odometer()

my_used_car = Car("subaru", "outback", 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()