"""
Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []


Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and 
                                                   adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

 
Also, the book class should have a class variable which holds the amount of all existing books

class Library:
    pass

class Book:
    pass

class Author:
    pass
"""


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return f"Library: <{self.name}, All books: {[b.name for b in self.books]}, All authors: {[a.name for a in self.authors]}>"

    def __str__(self):
        return self.name

    def new_book(self, name, year, author):
        added_book = Book(name, year, author)
        self.books.append(added_book)
        if author not in self.authors:
            self.authors.append(author)
        return added_book

    def group_by_author(self, author):
        return [b for b in self.books if b.author == author]

    def group_by_year(self, year):
        return [b for b in self.books if b.year == year]


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)

    def __repr__(self):
        return f"Book: <{self.name}, {self.year}, {repr(self.author)}>"

    def __str__(self):
        return f"Title: {self.name}"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author: <{self.name}, {self.country}, {self.birthday}, all books by this author: {[b.name for b in self.books]}>"

    def __str__(self):
        return f"Name: {self.name}"


buecherei = Library("buecherei")
author_haller = Author("Haller", "Germany", "2000")
new_book = buecherei.new_book("Die Hutmaenner", 2007, author_haller)
new_second_book = buecherei.new_book("Die Hutmaenner 2", 2008, author_haller)

for book in buecherei.group_by_author(author_haller):
    print(book)
