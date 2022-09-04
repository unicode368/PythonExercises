total = 0
pizza = 0
burger = 0
pasta = 0
option = int(input("Please choose the option:\n1. Pizza (200). \n2. Burger (150)."
               "\n3. Pasta (180). \n4. Exit."))
while option < 1 or option > 4:
    option = int(input("Please choose the option:\n1. Pizza (200). \n2. Burger (150)."
                       "\n3. Pasta (180). \n4. Exit."))
while 1 <= option <= 4:
    if option == 1:
        pizza_add = int(input("U have chosen pizza. How many pizzas do you want?"))
        while pizza_add < 0:
            pizza_add = int(input("How many pizzas do you want?"))
        pizza += pizza_add
        total += pizza_add * 200
    elif option == 2:
        burger_add = int(input("U have chosen burger. How many burgers do you want?"))
        while burger_add < 0:
            burger_add = int(input("How many burgers do you want?"))
        burger += burger_add
        total += burger_add * 150
    elif option == 3:
        pasta_add = int(input("U have chosen pasta. How many pastas do you want?"))
        while pasta_add < 0:
            pasta_add = int(input("How many pastas do you want?"))
        pasta += pasta_add
        total += pasta_add * 180
    else:
        print("List of all orders:")
        if pizza != 0:
            print("1. Pasta (" + str(pizza) + ") => " + str(pizza * 200))
        if burger != 0:
            print("2. Burger (" + str(burger) + ") => " + str(burger * 150))
        if pasta != 0:
            print("3. Pasta (" + str(pasta) + ") => " + str(pasta * 180))
        print("-------------------------------------------------")
        print("Total: " + str(total))
        break
    option = int(input("Please choose the option:\n1. Pizza (200). \n2. Burger (150)."
                       "\n3. Pasta (180). \n4. Exit."))