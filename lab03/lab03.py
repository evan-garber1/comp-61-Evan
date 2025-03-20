my_list = []
while True:
    print("Menu: \n1. Add a number to the list \n2. Remove a number from the list \n3. Insert a number at a specific position \n4. Pop a number from the list \n5. Find the sum, average, and maximum of the list \n6. Search for a number in the list \n7. Remove all odd numbers from the list \n8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num = int(input("Enter a number to add: "))
        my_list.append(num)
        print("Number added to the list. ")
    elif choice == 2:
        num = int(input("Enter a number to remove: "))
        if num in my_list:
            my_list.remove(num)
            print("Number removed from the list.")
        else:
            print("Number not found in the list.")
    elif choice == 3:
        num = int(input("Enter a number to insert: "))
        position = int(input("Enter an index to instert the number: "))
        if 0 <= position <= len(my_list):
            my_list.insert(position - 1, num)
            print("Number inserted to the list.")
        else:
            print("Invalid index")
    elif choice == 4:
        position = int(input("Enter an index to pop the number: "))
        if 0 <= position < len(my_list):
            my_list.pop(position - 1)
            print("Number popped from the list.")
        else:
            print("invalid index")
    elif choice == 5:
        total = sum(my_list)
        average = sum(my_list)/len(my_list)
        maximum = max(my_list)
        print(f"Sum: , {total}, Average: , {average}, Maximum: , {maximum}")
    elif choice == 6:
        num = int(input("Enter a number to search for: "))
        if num in my_list:
            index = my_list.index(num)
            print(f"{num},  is at index , {index}")
        else:
            print("Number not found in the list.")
    elif choice == 7:
       my_list = [num for num in my_list if num % 2 == 0]
       print("All odd numbers removed from the list.")
    elif choice == 8:
        print("Bye")
        break
    show_list = input("Would you like to print the current list? (yes/no): ")
    if show_list == "yes":
        print("Current list:", my_list)



    

