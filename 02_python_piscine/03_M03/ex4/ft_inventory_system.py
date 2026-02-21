def inventory_master():
	inventory = {
		"potions": 5,
		"armor": 3,
		"shield": 2,
		"sword": 1,
		"helmet": 1
	}
	# def inventory_analysis(inventory):
	total = sum(inventory.values())
	quantity = len(inventory.keys())
	print("=== Inventory System Analysis ===\n")
	print(f"Total items in the inventory:{total}")
	print(f"Unique item type: {quantity}")

	# def current_inventory(inventory):
	print("\n=== Current Inventory ===\n")
	for items, values in inventory.items():
		percent = (values / total) * 100
		if values > 1:
			print(f"{items}: {values} units ({percent:.1f}%)")
		else:
			print(f"{items}: {values} unit ({percent:.1f}%)")

	# def inventory_statistics(inventory):
	print("\n=== Inventory Statistics ===\n")
	print(f"Most abundant: ")
	



if __name__ == "__main__":
	inventory_master()