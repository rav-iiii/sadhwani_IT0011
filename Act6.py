class Item:
    item_counter = 1

    def __init__(self, name: str, description: str, price: float):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if description and not isinstance(description, str):
            raise ValueError("Description must be a string.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        
        self.id = Item.item_counter
        self.name = name
        self.description = description
        self.price = price
        Item.item_counter += 1

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: ${self.price:.2f}, Description: {self.description}"


class ItemManager:
    def __init__(self):
        self.items = {}
    
    def create_item(self, name, description, price):
        try:
            item = Item(name, description, price)
            self.items[item.id] = item
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)
    
    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            print("Item not found!")
            return
        try:
            if name:
                if not isinstance(name, str) or not name:
                    raise ValueError("Name must be a non-empty string.")
                self.items[item_id].name = name
            if description:
                if not isinstance(description, str):
                    raise ValueError("Description must be a string.")
                self.items[item_id].description = description
            if price is not None:
                if not isinstance(price, (int, float)) or price <= 0:
                    raise ValueError("Price must be a positive number.")
                self.items[item_id].price = price
            print("Item updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Item not found!")


def main():
    manager = ItemManager()
    while True:
        print("\nItem Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            try:
                price = float(input("Enter item price: "))
                manager.create_item(name, description, price)
            except ValueError:
                print("Invalid price. Please enter a valid number.")
        elif choice == '2':
            manager.read_items()
        elif choice == '3':
            try:
                item_id = int(input("Enter item ID to update: "))
                name = input("Enter new name (press enter to skip): ") or None
                description = input("Enter new description (press enter to skip): ") or None
                price = input("Enter new price (press enter to skip): ")
                price = float(price) if price else None
                manager.update_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            try:
                item_id = int(input("Enter item ID to delete: "))
                manager.delete_item(item_id)
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()