my_list = []
while True:
    print("Menu")
    print("1. Add an item to the end of the list.")
    print("2. Remove an item from the end of the list")
    print("3. Exit")
    choice = (int(input("Select an option: ")))
    if choice == 1:
        my_list.append(input("Choose a value to add: "))
        print("Value added to the end of the list.")
        print("Your list is", my_list)
    elif choice == 2:
        my_list.pop(-1)
        print("Value at the end of the list has been removed.")
        print("Your list is", my_list)
    elif choice == 3:
        break
    else:
        print("Invalid option. Please enter a number 1-3.")
        
    
class MenuProgram:
    def __init__(self):
         self.my_list = []
         self.choice = 0
    def show_menu():
        print("Menu")
        print("1. Add an item to the end of the list.")
        print("2. Remove an item from the end of the list")
        print("3. Exit")
        self.choice = (int(input("Select an option: ")))
    def run(self):
         while True:
             if self.choice == 1:
                 self.my_list.append(input("Choose a value to add: "))
                 print("Value added to the end of the list.")
             elif self.choice == 2:
                self.my_list.pop(-1)
                print("Value at the end of the list has been removed.")
             elif choice == 3:
                 break
             else:
                 print("Invalid option. Please enter a nubmer 1-3.")
    def print():
        print("Your list is", my_list)


menu_program = MenuProgram()
menu_program.show_menu()
menu_program.run()
menu_program.print()




              
    
       

    