class Users:
    def __init__(self, full_name, age, address, cellphone):
        self.full_name = full_name
        self.age = age
        self.address = address
        self.cellphone = cellphone
        self.loans_history = []
    
    def register_loans(self, loan):
        self.loans_history.append(loan)
    
    def show_information(self):
        return f"Name: {self.full_name}, age: {self.age}, address: {self.address}, cellphone: {self.cellphone}"
    