#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            value = my_list[i]
            if type(value) == int:
                print("{:d}".format(value), end=" ")
                count += 1
    except IndexError:
        pass  # Catching IndexError when x is greater than the length of my_list

    print()  # Print a new line after printing integers
    return count
