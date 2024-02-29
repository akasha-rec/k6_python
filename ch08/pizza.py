def make_pizza(size, *toppings):
    """요약 리스트"""
    print(f"\nㅡMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
         print(f"- {topping}")