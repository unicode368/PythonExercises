from HiSayer import HiSayer


def print_hi():
    my_hi_sayer = HiSayer("Hi,", "Python")
    my_hi_sayer.print_name()
    print(my_hi_sayer.public_var)
    my_hi_sayer.name = ""
    print(my_hi_sayer.public_var)
    ar1 = [1, 2, 3]
    ar2 = [4, 5, 6]
    zr = zip(ar1, ar2)
    print(set(zr))


if __name__ == '__main__':
    print_hi()
