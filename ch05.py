cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")

age = 12
if age < 4:
    print("입장료 무료")
elif age < 18:
    print("입장료 25$")
else:
    print("입장료 40$")

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")