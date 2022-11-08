class MyClass:
    # variable and method/function
    # variable: static variable / instance(non-static) variable
    # method: instance method
    # static variable
    num = 1234

    # constructor is a special instance method
    def __init__(self, name):
        self.name = name

    def print(self, msg):
        print('hello world:', msg)