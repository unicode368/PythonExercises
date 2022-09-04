categories = {"Ids": 0}
products = {"Ids": 0}
customers = {"Ids": 0}
orders = {"Ids": 0}


def edit_categories():
    empties = []
    print("Empty categories: ")
    for categoryId in list(categories.keys())[1:]:
        found = False
        for productId in list(products.keys())[1:]:
            if products[productId][2] == categoryId:
                found = True
        if not found:
            empties.append(int(categoryId))
            print("Category ID: {}".format(categoryId))

    while len(empties) != 0:
        cat_id_input = int(input("Please enter ID of category you want to change (-1 for EXIT): "))

        if cat_id_input == -1:
            break

        while not(cat_id_input in empties):
            cat_id_input = int(input("Please enter ID of category you want to change (-1 for EXIT): "))
            if cat_id_input == -1:
                break


        action_input = int(input("Choose an option: \n1. Add product to a category."
                                 "\n2. Delete category."))
        while 2 < action_input < 1:
            action_input = int(input("Choose an option: \n1. Add product to a category."
                                     "\n2. Delete category."))

        if action_input == 2:
            del categories[cat_id_input]
            empties.remove(cat_id_input)
        else:
            prod_name = input("Enter product name:")
            price = float(input("Enter price of the product:"))
            product = [prod_name, price, cat_id_input]
            insertProduct(product)
            empties.remove(cat_id_input)



def insertCategory(category):
    currentIx = categories["Ids"]
    categories[currentIx] = category
    categories["Ids"] += 1


def insertProduct(product):
    currentIx = products["Ids"]
    if product[2] in categories:
        products[currentIx] = [product[0], product[1], product[2]]
        products["Ids"] += 1
    else:
        print("Category doesn't exist")
        print()


def insertCustomerDetails(customer):
    currentIx = customers["Ids"]
    customers[currentIx] = customer
    customers["Ids"] += 1


def insertOrder(order):
    currentIx = orders["Ids"]
    Pid = order[0]
    CustomerId = order[3]
    if Pid in products and CustomerId in customers:
        orders[currentIx] = order
        orders["Ids"] += 1
    else:
        print("Ensure product and customer exist")


def adminMenu():
    while True:
        option = int(input("Get total sales based on: \n1. Product ID."
                           "\n2. Category. \n3. Price Range."
                           "\n4. Location. "
                           "\nOther options: \n5. See shipping/delivered orders."
                           "\n6. Edit categories. \n7. Exit\n"))

        if option == 1:
            productId = eval(input("Please enter the product ID: "))
            profit = 0
            quantity = 0
            for orderID in list(orders.keys())[1:]:
                if orders[orderID][0] == productId:
                    quantity += orders[orderID][1]
                    profit += orders[orderID][2]
            print()
            print("Total sold: {}".format(quantity))
            print("Total profit: £{}".format(profit))
            print()

        elif option == 2:
            categoryName = input("Please enter the category name: ")

            for currentCategory in list(categories.keys())[1:]:
                if categories[currentCategory][0] == categoryName:
                    categoryID = currentCategory

            profit = 0
            quantity = 0
            for orderID in list(orders.keys())[1:]:
                productID = orders[orderID][0]
                currentCategory = products[productID][2]
                if categoryID == currentCategory:
                    quantity += orders[orderID][1]
                    profit += orders[orderID][2]
            print()
            print("Total sold: {}".format(quantity))
            print("Total profit: £{}".format(profit))
            print()

        elif option == 3:
            direction = eval(input("Low to High or High to Low? 0 / 1"))
            visited = []
            profits = {}

            for productID in list(products.keys())[1:]:
                if productID not in visited:

                    for order in list(orders.keys())[1:]:
                        if orders[order][0] == productID:
                            if productID not in profits:
                                profits[productID] = orders[order][2]
                            else:
                                profits[productID] += orders[order][2]
                    visited.append(productID)

            pairs = []
            for item in list(profits.keys()):
                pairs.append((item, profits[item]))
            pairs = sorted(pairs, key=lambda x: x[1], reverse=bool(direction))

            print("========================")
            for item in pairs:
                print()
                print("Product ID: {}".format(item[0]))
                print("Product Name: {}".format(products[item[0]][0]))
                print("Profit: £{}".format(item[1]))
                print()
            print("========================")

        elif option == 4:
            location = input("Please enter the location: ")
            profit = 0
            quantity = 0
            for orderID in list(orders.keys())[1:]:
                customerID = orders[orderID][3]
                currentLocation = customers[customerID][3]
                if location == currentLocation:
                    quantity += orders[orderID][1]
                    profit += orders[orderID][2]
            print()
            print("Total sold: {}".format(quantity))
            print("Total profit: £{}".format(profit))
            print()

        elif option == 5:
            status_input = int(input("Enter desired status: \n1. Shipping. "
                                 "\n2. Delivered"))
            while 1 > status_input > 2:
                status_input = int(input("Enter desired status: \n1. Shipping. "
                                         "\n2. Delivered"))
            status = "Shipping" if status_input == 1 else "Delivered"

            print()
            print("Orders which are {}:".format(status))
            for orderID in list(orders.keys())[1:]:
                if orders[orderID][4] == status:
                    print("Order ID: {}".format(orderID))
                    product_name = products[orders[orderID][0]][0]
                    print("Product name: {}".format(product_name))
                print()
        elif option == 6:
            edit_categories()
        elif option == 7:
            break
        else:
            print("Invalid option")
            print()


while True:
    option = int(input("Enter the option: \n1. Insert category."
                       "\n2. Insert product. \n3. Insert customer details."
                       "\n4. Insert order. \n5. ADMIN OPTIONS. \n6. Exit.\n"))
    if option == 1:
        cat_name = input("Enter category name:")
        cat_desc = input("Enter category description:")
        category = [cat_name, cat_desc]
        insertCategory(category)
    elif option == 2:
        prod_name = input("Enter product name:")
        price = float(input("Enter price of the product:"))
        cat_id = int(input("Enter category Id:"))
        product = [prod_name, price, cat_id]
        insertProduct(product)
    elif option == 3:
        cust_email = input("Enter an email:")
        cust_phone_number = input("Enter phone number:")
        address = input("Enter the address:")
        location = input("Enter location:")
        country = input("Enter the country:")
        customer = [cust_email, cust_phone_number, address,
                    location, country]
        insertCustomerDetails(customer)
    elif option == 4:
        p_id = int(input("Enter product Id:"))
        quantity = int(input("Enter quantity of product:"))
        total_price = quantity * products[p_id][1]
        customer_id = int(input("Enter customer Id:"))
        status = input("Enter status (Delivered / Shipping):")
        while status != "Delivered" and status != "Shipping":
            status = input("Enter status (Delivered / Shipping):")
        order = [p_id, quantity, total_price, customer_id, status]
        insertOrder(order)
    elif option == 5:
        adminMenu()
    elif option == 6:
        break
    else:
        print("invalid")
