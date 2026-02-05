l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
r = float(input("Enter radius: "))

pi = 3.14

area = (l * b) + (0.5 * pi * r * r)
perimeter = (2 * l) + b + (pi * r)

print(f"Area : {area}")
print(f"Perimeter: {perimeter}")
