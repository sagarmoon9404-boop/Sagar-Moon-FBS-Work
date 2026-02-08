cost = float(input("Enter Cost Price: "))
selling = float(input("Enter Selling Price: "))

if selling > cost:
    print(f"Profit = {selling -cost} ")
elif cost > selling:
    print(f"Loss =  {cost - selling}")
else:
    print("No Profit No Loss")
