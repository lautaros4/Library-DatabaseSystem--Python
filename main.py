from Classes.LoansRegister import LoansRegister
from Classes.UserRegister import UserRegister
from Classes.Inventary import Inventary
     
def show_menu():
    print("\n --- Library's menu ---")
    print("1. Register User")
    print("2. Register Book")
    print("3. Register Loan")
    print("4. Register Return")
    print("5. Show Information about Users")
    print("6. Book's Inventary")
    print("7. Exit")

def main():
    loans_register = LoansRegister()
    user_register = UserRegister()
    inventary = Inventary()
    
    while True:
        show_menu()
        option = input("Choose an option from menu: ")

        if option == "1":
            user_register.register_user()

        elif option == "2":
            inventary.register_book()

        elif option == "3":
            loans_register.register_loan(user_register.UR, inventary.books)
            
        elif option == "4":
            loans_register.register_return(loans_register.LR, inventary.books)

        elif option == "5":
            user_register.show_information()
            
        elif option == "6":
            inventary.show_information()

        elif option == "7":
            print ("Exiting from database system.")
            break

if __name__ == "__main__":
    main()
            


        


