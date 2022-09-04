coffee_size = {'small': 2, 'medium': 3, 'large': 4}
coffee_types = {'brewed': 0, 'espresso': 0.5, 'cold brew': 1}
coffee_flavors = {'none': 0, 'hazelnut': 0.5, 'vanilla': 0.5, 'caramel': 0.5}
orders = {'Ids': 1}


def get_total_per_coffee(size, c_type, flavor):
    return coffee_size[size] + coffee_types[c_type] + coffee_flavors[flavor]


def print_total():
    global total
    print("Your orders list:")
    print("________________________________________________________")
    total = 0
    if len(orders.keys()) == 1:
        print("None")
    for i in list(orders.keys())[1:]:
        print(f"{orders[i][0][0].upper() + orders[i][0][1:]} {orders[i][1]} coffee, "
              f"{'no' if orders[i][2] == 'none' else orders[i][2]} flavor - £{orders[i][3]}")
        total += orders[i][3]
        print("________________________________________________________")
    print(f"Total: £{total}")
    print(f"The price with a tip is £{total + round(total * 0.15, 2)}")


print("Welcome!")
total = 0
while True:
    option = int(input("Please, choose an option: \n1. Order. \n2. Leave\n"))
    if option == 1:
        size = input("Do you want small, medium, or large?\n").lower()
        while size not in coffee_size.keys():
            size = input("Please, re-enter coffee size.\n").lower()
        c_type = input("Do you want brewed, espresso, or cold press?\n").lower()
        while c_type not in coffee_types.keys():
            c_type = input("Please, re-enter coffee type.\n").lower()
        is_flavor_needed = input("Do you want a flavored syrup? (Yes or No)\n").lower()
        while is_flavor_needed != "yes" and is_flavor_needed != "no":
            is_flavor_needed = input("Please, re-enter your answer.\n").lower()
        if is_flavor_needed == "yes":
            flavor = input("Do you want hazelnut, vanilla, or caramel?\n").lower()
            while c_type not in coffee_types.keys():
                c_type = input("Please, re-enter coffee type.\n").lower()
        else:
            flavor = "none"
        order = [size, c_type, flavor, get_total_per_coffee(size, c_type, flavor)]
        print(f"You've ordered {size} cup of {c_type} coffee "
              f"with {'no' if flavor == 'none' else flavor} flavor")
        print()
        orders[orders["Ids"]] = order
        orders["Ids"] += 1
        print_total()
    elif option == 2:
        if total == 0:
            print("Total: £0.")
        break
    else:
        print("Invalid input. Please, re-enter the option")
    print()
