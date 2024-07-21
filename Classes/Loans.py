from datetime import datetime

class Loans:
    def __init__(self, user, list_of_books):
        self.user = user
        self.list_of_books = list_of_books
        self.from_date = datetime.now()

    def register_loan(self):
        self.user.register_loans(self)
        return f"Loan successfully registered \n {self.show_information()}"
    
    def show_information(self):
        books = " ,".join([b.title for b in self.list_of_books])
        return f"User: {self.user.full_name}, Books: {books}, Date: {self.from_date}"

    



