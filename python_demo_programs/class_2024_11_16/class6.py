def greet(name):
    return "hello " + name


def display_greeting():
    # name = input('Enter your name:')
    msg = greet("Tom")
    print(msg)


# display_greeting()

def get_user_input():
    shape = input('Choose a shape (circle, rectangle)')
    if shape == "circle":
        radius = float(input('Enter the radius of the circle:'))
        return shape, radius
    elif shape == 'rectangle':
        length = float(input('Enter the length of the rectangle:'))
        width = float(input('Enter the width of the rectangle:'))
        return shape, length, width


# def calculate_area():
#     user_input = get_user_input()
#     # user_input[0], user_input[1], user_input[2]
#     if user_input[0] == 'circle':
#
#     elif user_input[0] == 'rectangle':

'''
Shopping cart program

Options:
1. Add item to cart
2. View cart
3. Calculate total
4. Exit
Choose an option: 1
Enter the item name: Apple
Enter the price of Apple: 0.5
Enter the quantity of Apple: 4
4 Apple(s) added to cart.

Options:
1. Add item to cart
2. View cart
3. Calculate total
4. Exit
Choose an option: 2

Shopping Cart:
Apple: $0.50 x 4 = $2.00

Options:
1. Add item to cart
2. View cart
3. Calculate total
4. Exit
Choose an option: 3
The total cost of your shopping cart is: $2.00

'''

def shopping_cart_program():
    cart = []

    while True:
        print("\nOptions:")
        print("1. Add item to cart")
        print("2. View cart")
        print("3. Calculate total")
        print("4. Exit")

        choice = input('Choose an option:')
        if choice == '1':
            item = input("Enter the item name: ")
            price = float(input(f"Enter the price of {item}: "))
            quantity = int(input(f"Enter the quantity of {item}: "))

            # finish following function
            add_item_to_cart(cart, item, price, quantity)
        elif choice == '2':
            # finish following function
            display_cart(cart)
        elif choice == '3':
            # finish following function
            calculate_total(cart)
        elif choice == '4':
            break