class Publisher():
    def __init__(self, name):
        self.name = name

    def display(self):
        print("NAME:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        self.title = title
        self.author = author
        super().__init__(name)

    def display(self):
        print("NAME:", self.name, ",", "TITLE:", self.title, ",", "AUTHOR:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        self.price = price
        self.noofpages = no_of_pages
        super().__init__(name, title, author)

    def display(self):
        print(
            "NAME:", self.name, ",",
            "TITLE:", self.title, ",",
            "AUTHOR:", self.author, ",",
            "PRICE:", self.price, ",",
            "PAGES:", self.noofpages
        )


a = input("Enter the name:")
x = input("Enter the title:")
c = input("Enter the name of author:")
d = int(input("Enter the price:"))
e = int(input("Enter the no of pages:"))

t = Publisher(a)
b = Book(a, x, c)
p = Python(a, x, c, d, e)


t.display()
b.display()
p.display()
