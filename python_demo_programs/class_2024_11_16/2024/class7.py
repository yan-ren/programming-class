# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print(f'Hello, my name is {self.name}')
#
#
# # object
# p1 = Person('Tom', 14)
# p2 = Person('Jerry', 15)
#
# print(p1.name)
# print(p1.age)
#
# p1.name = 'Tommy'
#
#
# print(p2.name)
# print(p2.age)

'''
Create a class called Book, contains variable: book name, author, description
'''
class Book:
    def __init__(self, name, author, description, price):
        self.name = name
        self.author = author
        self.description = description
        self.price = price

    def get_name_and_author(self):
        return self.name + " was written by " + self.author

    def __str__(self):
        return self.get_name_and_author()

    def __repr__(self):
        return self.name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_most_expensive_book(self):
        highest_price = -1
        most_expensive_book = None

        for book in self.books:
            if book.price > highest_price:
                highest_price = book.price
                most_expensive_book = book

        return most_expensive_book.name


book1 = Book('Travel', 'Tom', "Written in 2021", 20)
print(book1.name)
print(book1)

# print(book1.get_name_and_author())
library = Library()
library.add_book(book1)
print(library.books)
print(library.get_most_expensive_book())


