class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")
    
    @classmethod
    def class_method(cls):
        print(f"Called Class Method {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")


ClassTest.class_method()

ClassTest.static_method()

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"


    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)

print(Book.TYPES)

book_hardcover = Book.hardcover("Harry Potter",  1500)

print(book_hardcover)

book_paperback = Book.paperback("Harry Potter",  1500)

print(book_paperback)