import random

discounts = ('TEN15', 'TEN20', 'TEN25', 'FIVE10', 'FIVE08', 'FIVE05', 'ONE03', 'ONE04', 'ONE05')
products = {"Milk": 10, "Cheese": 25, "Candy": 5, "TV": 2000, "Car": 10000, "Phone": 4000}
basket = {}


def get_total(basket):
    total = 0
    for i in basket.keys():
        total += basket[i] * products[i]
    return total


while True:
    print("Available products:")
    for i in products.keys():
        print(i)
    print()
    option = input("Please enter product name (-1 for EXIT):")
    while option != "-1" and (option not in products.keys()):
        option = input("Please re-enter product name (-1 for EXIT):")
    if option == "-1":
        print()
        print("Your bill:")
        print("Product\t\tQuantity\t")
        for i in basket.keys():
            print(i + "\t\t" + str(basket[i]) + "\t")
        print()
        total = get_total(basket)
        print("Total:\t\t" + str(total))
        if 1000 <= total <= 5000:
            discount = discounts[6 + random.randrange(0, 3)]
            print(f"Discount applied: " + discount)
            percentage = int(discount.split("ONE")[1])
            discounted_total = total - (total * (percentage / 100))
            print("Total with discount:\t\t" + str(discounted_total))
        elif 5000 < total <= 10000:
            discount = discounts[3 + random.randrange(0, 3)]
            print(f"Discount applied: " + discount)
            percentage = int(discount.split("FIVE")[1])
            discounted_total = total - (total * (percentage / 100))
            print("Total with discount:\t\t" + str(discounted_total))
        elif total > 10000:
            discount = discounts[random.randrange(0, 3)]
            print(f"Discount applied: " + discount)
            percentage = int(discount.split("TEN")[1])
            discounted_total = total - (total * (percentage / 100))
            print("Total with discount:\t\t" + str(discounted_total))
        break
    else:
        quantity = int(input("Please enter product quantity:"))
        while quantity < 1:
            quantity = input("Please enter product quantity:")
        if option not in basket.keys():
            basket[option] = quantity
        else:
            basket[option] += quantity
