from Classes.Loans import Loans

class LoansRegister:
    
    def __init__(self):
        self.LR = []

    def register_loan(self, users, inventary):
        user_name = input ("Insert user's name: ")
        user = next((u for u in users if u.full_name == user_name), None)
        if not user:
            print("User not founded. Register it first")
            return
    
        loaned_books = []
        while True:
            book_title = input("Insert book (leave it empty for ending it): ")
            if not book_title:
                break
            book = next((t for t in inventary if t.title == book_title), None)
            if not book:
                print("Book not founded")
                return
            else:
                loaned_books.append(book)
    
        loan = Loans(user, loaned_books)
        self.LR.append(loan)
        print(loan.register_loan())

        for b in inventary:
            for l in loan.list_of_books:
                if l == b and b.quantity > 0:
                        b.substract_qty()

    def register_return(self, loans, inventary):
        user_name = input ("Insert user's name: ")
        loan = next((lo for lo in loans if lo.user.full_name == user_name), None)
        self.LR.remove(loan)
        for b in inventary:
            for lr in loan.list_of_books:
                if lr == b:
                    b.add_qty()