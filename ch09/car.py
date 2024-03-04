class Car:
    """자동차를 표현하는 클래스"""

    def __init__(self, make, model, year):
        """자동차 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """뜻이 분명하고 깔끔한 이름으로 반환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """자동차 주행거리를 출력합니다"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        # """거리계를 주어진 값으로 설정합니다."""
        # self.odometer_reading = mileage
        """현재 값보다 적은 값을 할당할 수 없습니다."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("주행거리를 줄일 수 없어요")

    def increment_odometer(self, miles):
        """거리계 값을 주어진 값만큼 늘립니다."""
        self.odometer_reading += miles

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