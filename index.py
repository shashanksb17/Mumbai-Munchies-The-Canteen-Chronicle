import os
import json

# Function to clear the terminal screen
def clear_screen():
    if os.name == "nt":  # for Windows
        _ = os.system("cls")
    else:  # for other platforms
        _ = os.system("clear")

# Function to display the main menu
def display_menu():
    print("=== Mumbai Munchies: The Canteen Chronicle ===")
    print("1. View Snack Inventory")
    print("2. Add Snack to Inventory")
    print("3. Remove Snack from Inventory")
    print("4. Update Snack Availability")
    print("5. Record Snack Sale")
    print("6. Exit")

# Function to get the user's choice from the main menu
def get_user_choice():
    return input("Enter your choice (1-6): ")

# Function to save inventory to a file
def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(inventory, file)

# Function to load inventory from a file
def load_inventory():
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            return json.load(file)
    else:
        return {}

# Function to save sales record to a file
def save_sales_record():
    with open("sales_record.json", "w") as file:
        json.dump(sales_record, file)

# Function to load sales record from a file
def load_sales_record():
    if os.path.exists("sales_record.json"):
        with open("sales_record.json", "r") as file:
            return json.load(file)
    else:
        return []

# Initialize snack inventory and sales record
inventory = load_inventory()
sales_record = load_sales_record()

# Main loop to run the application
while True:
    clear_screen()
    display_menu()
    user_choice = get_user_choice()

    # Option 1: View Snack Inventory
    if user_choice == "1":
        print("\n=== Snack Inventory ===")
        if inventory:
            for snack_id, snack_details in inventory.items():
                snack_name = snack_details["name"]
                snack_price = snack_details["price"]
                snack_availability = snack_details["availability"]
                availability_status = "Available" if snack_availability else "Not available"
                print(f"ID: {snack_id}, Name: {snack_name}, Price: ${snack_price}, Availability: {availability_status}")
        else:
            print("Inventory is empty.")

    # Option 2: Add Snack to Inventory
    elif user_choice == "2":
        print("\n=== Add Snack to Inventory ===")
        snack_name = input("Enter the snack name: ")
        snack_price = input("Enter the snack price: ")
        snack_availability = input("Enter the snack availability (True/False): ")
        snack_id = max(inventory.keys(), default=0) + 1
        inventory[snack_id] = {"name": snack_name, "price": snack_price, "availability": snack_availability}
        print(f"Snack '{snack_name}' added to inventory with ID: {snack_id}")
        save_inventory()

    # Option 3: Remove Snack from Inventory
    elif user_choice == "3":
        print("\n=== Remove Snack from Inventory ===")
        snack_id = int(input("Enter the ID of the snack to remove: "))
        if snack_id in inventory:
            snack_name = inventory[snack_id]["name"]
            del inventory[snack_id]
            print(f"Snack '{snack_name}' with ID {snack_id} removed from inventory.")
            save_inventory()
        else:
            print(f"Snack with ID {snack_id} does not exist in the inventory.")

    # Option 4: Update Snack Availability
    elif user_choice == "4":
        print("\n=== Update Snack Availability ===")
        snack_id = int(input("Enter the ID of the snack to update: "))
        if snack_id in inventory:
            new_availability = input("Enter the new availability (True/False): ")
            if new_availability.lower() in ["true", "false"]:
                inventory[snack_id]["availability"] = new_availability.lower() == "true"
                print("Snack availability updated successfully.")
                save_inventory()
            else:
                print("Invalid availability value! Please enter True or False.")
        else:
            print(f"Snack with ID {snack_id} does not exist in the inventory.")

    # Option 5: Record Snack Sale
    elif user_choice == "5":
        print("\n=== Record Snack Sale ===")
        snack_id = int(input("Enter the ID of the snack sold: "))
        if snack_id in inventory:
            if inventory[snack_id]["availability"]:
                sales_record.append(snack_id)
                inventory[snack_id]["availability"] = False
                print("Snack sale recorded successfully.")
                save_inventory()
                save_sales_record()
            else:
                print("The snack is not available.")
        else:
            print(f"Snack with ID {snack_id} does not exist in the inventory.")

    # Option 6: Exit
    elif user_choice == "6":
        print("\nThank you for using Mumbai Munchies: The Canteen Chronicle. Goodbye!")
        save_inventory()
        save_sales_record()
        break

    # Invalid choice
    else:
        print("\nInvalid choice! Please enter a number from 1 to 6.")

    input("Press Enter to continue...")
