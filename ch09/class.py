#self는 필수 매개변수 > 반드시 맨 앞에 써줘야
# = 인스턴스 자체 > 관련 메서드는 self를 통해 자동전달
class Dog:
    """개를 표현하는 클래스"""

    def __init__(self, name, age): #클래스 속한 함수 = 메서드
        """name과 age 속성 초기화"""
        self.name = name #속성= 자바의 field
        self.age = age

    def sit(self):
        """앉기"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """구르기"""
        print(f"{self.name} roll over!")

my_dog = Dog("Willie", 6) #생성자 호출 > 인스턴스 생성
my_dog.sit()
print(f"개의 이름은 {my_dog.name}입니다.")
your_dog = Dog("Lucy", 3)
print(f"Your dog's name is {your_dog.name}")
print(f"Your dog's age is {your_dog.age}")
your_dog.sit()