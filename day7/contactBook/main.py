from Person import Person
import math


def check_credentials(phone_number, email):
    if math.log10(phone_number) <= 9:
        return False
    second_part = email.split("@")
    if len(second_part) > 2:
        return False
    ending = second_part[1].split(".")[1]
    endings = ("co", "com", "in", "org")
    for i in endings:
        if ending == i:
            return True
    return False


def print_row(start_contact, end_contact):
    if end_contact - start_contact == 3:
        print("{:<8} {:<20} {:<25} {:<1} {:<8} {:<20} {:<25} {:<1} {:<8} {:<20} {:<25} {:<1}"
              "\n{:<8} {:<20} {:<25} {:<1} {:<8} {:<20} {:<25} {:<1} {:<8} {:<20} {:<25} {:<1}\n"
              "{:<8} {:<20} {:<25} {:<1} {:<8} {:<20} {:<25} {:<1} {:<8} {:<20} {:<25} {:<1}\n"
              .format(phone_book[start_contact].id,
                      'Contact name:', phone_book[start_contact].name, "|", phone_book[start_contact + 1].id,
                      'Contact name:', phone_book[start_contact + 1].name, "|", phone_book[start_contact + 2].id,
                      'Contact name:', phone_book[start_contact + 2].name, "|", " ", 'Contact number:',
                      phone_book[start_contact].phone_number, "|", " ", 'Contact number:',
                      phone_book[start_contact + 1].phone_number, "|", " ", 'Contact number:',
                      phone_book[start_contact + 2].phone_number, "|", " ", 'Email:', phone_book[start_contact].email,
                      "|", " ", 'Email:', phone_book[start_contact + 1].email,
                      "|", " ", 'Email:', phone_book[start_contact + 2].email,
                      "|"))
    elif end_contact - start_contact == 2:
        print("{:<8} {:<20} {:<25} {:<1} {:<8} {:<20} {:<25} {:<1}"
              "\n{:<8} {:<20} {:<25} {:<1} {:<8} {:<20} {:<25} {:<1}\n"
              "{:<8} {:<20} {:<25} {:<1} {:<8} {:<20} {:<25} {:<1}\n"
              .format(phone_book[start_contact].id,
                      'Contact name:', phone_book[start_contact].name, "|", phone_book[start_contact + 1].id,
                      'Contact name:', phone_book[start_contact + 1].name, "|", " ", 'Contact number:',
                      phone_book[start_contact].phone_number, "|", " ", 'Contact number:',
                      phone_book[start_contact + 1].phone_number, "|", " ", 'Email:', phone_book[start_contact].email,
                      "|", " ", 'Email:', phone_book[start_contact + 1].email,
                      "|"))
    elif end_contact - start_contact == 1:
        print("{:<8} {:<20} {:<25} {:<1}\n{:<8} {:<20} {:<25} {:<1}\n{:<8} {:<20} {:<25} {:<1}\n"
              .format(phone_book[start_contact].id,
                'Contact name:', phone_book[start_contact].name, "|", " ", 'Contact number:',
                phone_book[start_contact].phone_number, "|", " ", 'Email:', phone_book[start_contact].email,
              "|"))


def display():
    if len(phone_book) == 0:
        print("No elements.")
        return
    else:
        counter = 0
        last_els = len(phone_book) % 3
        for i in range(0, len(phone_book) // 3, 3):
            print_row(i, i + 3)
            print("_" * 168)
            counter += 3
        print_row(counter, counter + last_els)
        if last_els != 0:
            print("_" * 168)


def insert(name, phone_number, email):
    new_contact = Person(len(phone_book) + 1, name, phone_number, email)
    if search(new_contact) is not None:
        print("Contact already exists")
    phone_book.append(new_contact)


def search(phone_number):
    for i in phone_book:
        if phone_number == i.phone_number:
            return i
    return None


def delete(phone_number):
    for i in phone_book:
        if phone_number == i.phone_number:
            phone_book.remove(i)
            break


phone_book = []

while True:
    option = int(input("Please select the option: \n1. Insert. \n2. Delete. \n3. Search. \n4. Update. "
                       "\n5. Display. \n6. Exit. "))
    while type(option) != int and 1 > option > 6:
        option = int(input("Please re-enter the option: \n1. Insert. \n2. Insert. \n3. Insert. \n4. Insert. "
                           "\n5. Display. \n6. Exit. "))
    if option == 1:
        print("Please enter contact credentials:")
        name = input("Contact name: ")
        phone_number = int(input("Contact number: "))
        email = input("Email: ")
        while not check_credentials(phone_number, email):
            phone_number = int(input("Re-enter contact number: "))
            email = input("Re-enter email: ")
        insert(name, phone_number, email)
    elif option == 2:
        phone_number = int(input("Enter phone number of contact you wish to delete: "))
        delete(phone_number)
    elif option == 3:
        phone_number = int(input("Enter phone number of contact you wish to find: "))
        found = search(phone_number)
        if found is None:
            print("There's no such contact.")
        else:
            print("Here's searched contact:")
            print_row(found.id - 1, found.id)
    elif option == 4:
        phone_number = int(input("Enter phone number of contact you wish to update: "))
        found = search(phone_number)
        print("Please enter contact credentials:")
        name = input("Contact name: ")
        phone_number = int(input("Contact number: "))
        email = input("Email: ")
        while not check_credentials(phone_number, email):
            phone_number = int(input("Re-enter contact number: "))
            email = input("Re-enter email: ")
        phone_book[found.id - 1] = Person(found.id, name, phone_number, email)
        print("Contact after update:")
        print_row(found.id - 1, found.id)
    elif option == 5:
        print("Your contact book:")
        display()
    else:
        break
