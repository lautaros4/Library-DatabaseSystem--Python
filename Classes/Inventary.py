from Classes.Books import Books

class Inventary:

    def __init__(self):
        self.books = []

    def register_book(self):
        title = input("Insert Title: ")
        cover = input("Insert cover's type (soft/hard): ").strip().lower()
        initial_state = input("Insert book's state (bad/good/excelent): ").strip().lower()
        quantity = int(input("Insert quantity: "))
        book = Books(title, cover, initial_state, quantity)
        self.books.append(book)
        print(f"{book.title} now on system")

    def show_information(self):
        for book in self.books:
            print(f"Book: {book.title}, Cover: {book.cover}, Qty: {book.quantity}")
        
    
