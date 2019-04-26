class Book:
    books_amount = 0

    def __init__(self, name="Kolobook", pages_amount=100, author="Ronaldo", price_in_euros=20,
                    genre="Drama", publishment_country="Ukraine"):
        self.name = name
        self.pages_amount = pages_amount
        self.author = author
        self.price_in_euros = price_in_euros
        self.genre = genre
        self.publishment_country = publishment_country
        Book.books_amount += 1

    @staticmethod
    def get_static_field():
        return Book.books_amount

    def __del__(self):
        print(self.name + " deleted")

    def __str__(self):
        return str(self.__dict__)

def main():
    kolobook = Book()
    tom_sawyer = Book("Tom Sawyer", 200, "Mark Twain", 50)
    king_kong = Book("King Kong", 300, "Erzhan", 80, "Fantasy", "Russia")

    print(kolobook)
    print(tom_sawyer)
    print(king_kong)
    print(Book.books_amount)

if __name__ == '__main__':
    main()
    sys
