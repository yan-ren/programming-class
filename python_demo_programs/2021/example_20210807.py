
def read_int():
    while True:
        try:
            x = int(input("please enter an integer:"))
            1/0
            break
        except ValueError:
            print("Invalid input, try again")
        except ZeroDivisionError:
            print("division by zero, invalid")
    return x


# read_int()

try:
    int(input("enter an integer:"))
except:
    print("invalid input")
else:
    print("good input")
