def get_formatted_name(first_name, last_name):
    """실제 이름"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

unprinted_design = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

while unprinted_design:
    current_design = unprinted_design.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)