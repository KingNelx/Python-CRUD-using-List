# initialize empty list
items = []


# function to display all items in the list
def display_items():
    if len(items) == 0:
        print("No items found")
    else:
        for index, item in enumerate(items):
            print(f"{index + 1}. {item}")


# function to add a new item to the list
def add_item():
    item = input("Enter item: ")
    items.append(item)
    print(f"{item} added to the list.")


# function to update an existing item in the list
def update_item():
    display_items()
    index = int(input("Enter the index of the item you want to update: ")) - 1
    new_item = input("Enter new item: ")
    items[index] = new_item
    print("Item updated.")


# function to delete an item from the list
def delete_item():
    display_items()
    index = int(input("Enter the index of the item you want to delete: ")) - 1
    item = items.pop(index)
    print(f"{item} deleted from the list.")


# main function to run the application
def main():
    while True:
        print("\n==== MENU ====")
        print("1. Display items")
        print("2. Add item")
        print("3. Update item")
        print("4. Delete item")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_items()
        elif choice == 2:
            add_item()
        elif choice == 3:
            update_item()
        elif choice == 4:
            delete_item()
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
