def ft_count_harvest_recursive():
    days = int(input("Days until harvest: ")) 
    counting(1, days)
    
def counting(i, days):
    if i <= days:
        print(f"Day {i}")
        counting(i+1, days)
    else:
        print("Harvest day")
        return
    