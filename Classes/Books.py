class Books:

    def __init__(self, title, cover, initial_state, quantity):
        self.title = title
        self.cover = cover
        self.initial_state = initial_state
        self.quantity = quantity

    def __eq__(self, another):
        return self.title == another.title and self.cover == another.cover
    
    def add_qty(self):
        self.quantity += 1

    def substract_qty(self):
        self.quantity -= 1

    def show_information(self):
        return f"Book: {self.title}, Cover: {self.cover}, State: {self.initial_state}, Qty: {self.quantity}"
    
