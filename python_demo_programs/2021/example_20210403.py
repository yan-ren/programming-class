class MyClass:
    num = 12345 # <- class variable

    # construct method receives the passed in value when creating object
    def __init__(self, name, age):
        self.name = name # <- instance variable
        self.age = age

    # class method
    def greet(self):
        return "hello"


a = MyClass("Tom", 1)
print(a.name)
