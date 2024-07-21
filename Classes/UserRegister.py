from Classes.Users import Users

class UserRegister:

    def __init__(self):
        self.UR = []

    def register_user(self):
        full_name = input("Insert full name: ")
        age = int(input("Insert age: "))
        address = input("Insert address: ")
        cellphone = input("Insert cellphone number: ")
        user = Users(full_name, age, address, cellphone)
        self.UR.append(user)
        print(f"User {user.full_name} now on system")
        
    def delete_user(self,user):
        self.UR.remove(user)

    def show_information(self):
        for u in self.UR:
           print(u.show_information())

    
