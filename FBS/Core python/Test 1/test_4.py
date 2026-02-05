interior_area = float(input("Enter interior wall area: "))
interior_cost = float(input("enter cost per unit for interior wall: "))

exterior_area = float(input("enter exterior wall area: "))
exterior_cost = float(input("enter cost per unit for exterior wall: "))

total_cost = (interior_area * interior_cost) + (exterior_area * exterior_cost)

print(f"Total painting cost: {total_cost}")
