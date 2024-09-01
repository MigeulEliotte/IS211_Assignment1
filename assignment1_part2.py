class Book:
    def __init__(self, author='', title=''):
        self.author = author
        self.title = title

    def display(self):
        print(f"{self.title}, written by {self.author}")


book1 = Book(author="J.K. Rowling", title="Harry Potter and the Goblet of Fire")
book2 = Book(author="Walter Scott", title="Ivanhoe: A Romance")

book1.display()
book2.display()
