# Second Brain Mirror App
# Class 12 Python Project

memory = {}

while True:
    print("\n===== SECOND BRAIN MIRROR =====")
    print("1. Add Memory")
    print("2. View All Memories")
    print("3. Search Memory")
    print("4. Delete Memory")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Memory
    if choice == "1":
        title = input("Enter memory title: ")
        detail = input("Enter memory detail: ")

        memory[title] = detail
        print("Memory Saved Successfully!")

    # View All Memories
    elif choice == "2":

        if len(memory) == 0:
            print("No memories saved.")

        else:
            print("\nSaved Memories:")
            for title in memory:
                print(title, ":", memory[title])

    # Search Memory
    elif choice == "3":

        search = input("Enter title to search: ")

        if search in memory:
            print("Memory Found!")
            print(search, ":", memory[search])

        else:
            print("Memory not found.")

    # Delete Memory
    elif choice == "4":

        delete = input("Enter title to delete: ")

        if delete in memory:
            del memory[delete]
            print("Memory Deleted Successfully!")

        else:
            print("Memory not found.")

    # Exit
    elif choice == "5":
        print("Thank You for Using Second Brain Mirror!")
        break

    else:
        print("Invalid Choice")