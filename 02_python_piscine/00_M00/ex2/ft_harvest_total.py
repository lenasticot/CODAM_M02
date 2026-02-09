def ft_harvest_total():
	total = 0
	for x in range(1, 4):
		weight = int(input(f"Day {x} harvest: "))
		total += weight
	print(f"Total harvest: {total}")
