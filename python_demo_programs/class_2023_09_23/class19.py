# def apply(fn, a, b):
#     result = fn(a, b)
#     return result

# def my_function(x, y):
#     z = x + y
#     return z

# print(type(my_function))
# my_sum = my_function
# print(type(my_sum))

# print(my_sum(1, 2))
# print(my_function(1, 2))

# print(apply(my_function, 1, 2))

# def increase_by_two(x):
#     return x + 2

# def apply_to_list(f, input_list):
#     result = []
#     for element in input_list:
#         result.append(f(element))

#     return result

# numbers = [1, 2, 3]
# print(apply_to_list(increase_by_two, numbers))

# def create_greet(message):
#     def greet(name):
#         print(message + ":" + name)

#     return greet

# my_greet = create_greet("welcome back")
# my_greet("Sam")

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def apply(fn, x, y):
    return fn(x, y)


print(apply(add, 1, 2))
print(apply(multiply, 1, 2))