class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"레스토랑 이름은 {self.restaurant_name}입니다.")
        print(f"레스토랑 유형은 {self.cuisine_type}입니다.")
    
    def open_restaurant(self):
        print("레스토랑이 문을 열었습니다.")

restaurant1 = Restaurant("맘스터치", "일반음식점")
restaurant2 = Restaurant("김밥천국", "분식")
restaurant3 = Restaurant("레스토랑", "레스토랑")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
# restaurant.open_restaurant()

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"사용자의 이름은 {self.first_name} {self.last_name}이고, 나이는 {self.age} 입니다.")

    def greet_user(self):
        print("환영합니다!")

user1 = User("james", "john", 18)
user2 = User("lisa", "johnson", 17)
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()