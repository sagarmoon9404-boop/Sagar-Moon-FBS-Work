# take input

triangle_1 = float(input(' Enter the first side of triangle: '))
triangle_2 = float(input(' Enter the second side of triangle: '))
triangle_3 = float(input(' Enter the third side of triangle: '))
if (triangle_1 + triangle_2  > triangle_3) and (triangle_2 + triangle_3 > triangle_1) and (triangle_3 + triangle_1 > triangle_2):
    print("The triangle is valid")
else:
    print("The triangle is not valid")