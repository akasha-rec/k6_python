# class Car:
#     """자동차를 표현하는 클래스"""

#     def __init__(self, make, model, year):
#         """자동차 속성 초기화"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """뜻이 분명하고 깔끔한 이름으로 반환"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         """자동차 주행거리를 출력합니다"""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         # """거리계를 주어진 값으로 설정합니다."""
#         # self.odometer_reading = mileage
#         """현재 값보다 적은 값을 할당할 수 없습니다."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("주행거리를 줄일 수 없어요")

#     def increment_odometer(self, miles):
#         """거리계 값을 주어진 값만큼 늘립니다."""
#         self.odometer_reading += miles

from car import Car

class Battery:
    """전기차의 배터리를 표현하는 클래스"""

    def __init__(self, battery_size = 40):
        """배터리 속성을 초기화합니다"""
        self.battery_size = battery_size

    def describe_battery(self):
        """배터리의 크기를 설명하는 문장을 출력합니다"""
        print(f"이 차의 배터리는 {self.battery_size}-kWh입니다.")
        
class ElectricCar(Car):
    """전기차만 해당하는 특성을 정의합니다"""

    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화합니다"""
        super().__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self):
    #     """배터리 크기를 설명하는 문장을 출력합니다"""
    #     print(f"이 차의 배터리는 {self.battery_size}-kWh 입니다.")

    # def get_descriptive_name(self):
    #     print(super().get_descriptive_name())
    #     print(f"차량 배터리의 크기는 {self.battery_size}입니다.")
        
my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
# my_leaf.describe_battery()
# my_leaf.get_descriptive_name()
