import sys

def inventory_master():
    if len(sys.argv) < 2:
        print("Usage: python3 script.py item:qty item:qty ...")
        sys.exit(1)
    inventory = {}
    for arg in sys.argv[1:]:
        try:
            item, qty = arg.split(":")
            inventory[item] = int(qty)
        except ValueError:
            print(f"Error: Invalid format '{arg}'. Use item:quantity")
            sys.exit(1)
    
    return inventory

def inventory_analysis(inventory):
    total = sum(inventory.values())
    quantity = len(inventory.keys())
    print("=== Inventory System Analysis ===\n")
    print(f"Total items in the inventory: {total}")
    print(f"Unique item type: {quantity}") 
    
def current_inventory(inventory):
    print("=== Current Inventory ===\n")
    total = sum(inventory.values())
    for items, values in inventory.items():
        percent = (values / total) * 100
        if values > 1:
            print(f"{items}: {values} units ({percent:.1f}%)")
        else:
            print(f"{items}: {values} unit ({percent:.1f}%)")
             
def inventory_statistics(inventory):
    print("=== Inventory Statistics ===\n")
    
    most_item = max(inventory, key=inventory.get)
    most_value = inventory[most_item]
    
    least_item = min(inventory, key=inventory.get)
    least_value = inventory[least_item]         
    if most_value > 1:
        print(f"Most abundant: {most_item} ({most_value} units)")
    else:
        print(f"Most abundant: {most_item} ({most_value} unit)")
    if least_value > 1:
        print(f"Least abundant: {least_item} ({least_value} units)")
    else:
        print(f"Least abundant: {least_item} ({least_value} unit)")

def item_category(inventory):
    print("=== Item Categories ===\n")
    categories = {
            "Moderate": {},
            "Scarce": {}
        }
    for item, value in inventory.items():
        if value >= 5:
            categories['Moderate'][item] = value
        else:
            categories['Scarce'][item] = value
    print(f"Moderate: {categories["Moderate"]}")
    print(f"Scarce: {categories["Scarce"]}")
            
def management_suggestions(inventory):
    print("=== Management Suggestions ===\n")
    restock = []
    for items, values in inventory.items():
        if values == 1:
            restock.append(items)
            
    print(f"Restock needed: {restock}")

def dictionary_properties(inventory):
    print("=== Dictionary Properties Demo ===\n")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    item_to_check = "sword"
    exists = item_to_check in inventory
    print(f"Sample lookup - '{item_to_check}' in inventory: {exists}")

if __name__ == "__main__":
    inventory = inventory_master()
    inventory_analysis(inventory)
    print("")
    current_inventory(inventory)
    print("")
    inventory_statistics(inventory)
    print("")
    item_category(inventory)
    print("")
    management_suggestions(inventory)
    print("")
    dictionary_properties(inventory)