# shopping_list_manager.py

def display_menu():
    """Prints the main menu options to the console."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Initialize an empty list to store the shopping items
    shopping_list = []
    
    # Start the main application loop
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        # --- 1. Add Item ---
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item: # Ensure the user didn't enter an empty string
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
        
        # --- 2. Remove Item ---
        elif choice == '2':
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove:
                # Use a try-except block to gracefully handle the case where the item is not in the list
                try:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' removed from the list.")
                except ValueError:
                    # The ValueError is raised by list.remove() if the item is not found
                    print(f"'{item_to_remove}' was not found in the list.")
            else:
                print("Item name cannot be empty.")
        
        # --- 3. View List ---
        elif choice == '3':
            print("\n--- Current Shopping List ---")
            if shopping_list:
                # Use enumerate to display a numbered list for better readability
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty! Time to add some items.")
            print("---------------------------")
        
        # --- 4. Exit ---
        elif choice == '4':
            print("Goodbye! Happy shopping!")
            break
        
        # --- Invalid Choice Handling ---
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
