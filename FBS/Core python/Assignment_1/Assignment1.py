### 1.Write a program to calculate the percentage of student based on marks of any 5
# Subjects.
# take input
sub1=float(input('Enter mark of subject 1:'))
sub2=float(input('Enter mark of subject 2:'))
sub3=float(input('Enter mark of subject 3:'))   
sub4=float(input('Enter mark of subject 4:'))
sub5=float(input('Enter mark of subject 5:'))

#perform operation
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100

#display result
print(f'Student percentage is: {percentage}%')



### 2. Write a program to calculate area of rectangle based on length and breadth.
# take input
length = int(input('Enter length of Rectangle:'))
breadth = int(input('Enter breadth of Rectangle:'))

# perform operation
area = length * breadth

# display result
print(f'Area of Rectangle is: {area}')



### 3. Program to find quotient and remainder of two numbers
# take input
num1 = int(input('enter first number:'))
num2 = int(input('enter second number:'))

# perform operation
quotient = num1 // num2
remainder = num1 % num2

# display result
print(f'Quotient is: {quotient}')
print(f'Remainder is: {remainder}')



### 4. Write a program to enter P, T, R and calculate simple Interest
# take input
principal = int(input('Enter principal amount:'))
time = int(input( 'enter time in year:'))
rate = int(input('enter rate in percentage: ' ))

# perform operation
simple_interest= (principal * time * rate) / 100
# display result
print(f'Simple Interest is: {simple_interest}')



### 5. Write a program to enter P, T, R and calculate Compound Interest
# take input
prin =int(input('Enter principal amount:'))
time = int(input('Enter time in year:'))
rate = int(input('Enter rate in percentage: '))

# perform operation
compound_interest = prin * (1 + rate/100)**time - prin
# display result
print(f'Compound Interest is: {compound_interest}')



### 6. Write a Program to input two angles from user and find third angle of the triangle.
# take input
Angle1= int(input('Enter first angle of triangle:'))
Angle2= int(input('Enter second angle of triangle:'))

# perform operation
Angle3 = 180 - (Angle1 + Angle2)

# display result
print(f'Third angle of triangle is: {Angle3}')



### 7. Program to Find the Roots of a Quadratic Equation
# take input
a = int(input('Enter number a:'))
b = int(input('Enter number b:'))
c = int(input('Enter number c:'))

# perform operation
d = (b**2) - (4*a*c)
sqrt_d = d**0.5
root1 = (-b + sqrt_d) / (2*a)   
root2 = (-b - sqrt_d) / (2*a)
# display result
print(f'Roots of the quadratic equation are: {root1} and {root2}')



### 8. Write a program to convert days into years, weeks and days.
# take input
Total_days = int(input('Enter total number od days:'))
# perform operation
years = Total_days // 365
remaining_days_after_years = Total_days % 365
weeks = remaining_days_after_years // 7
remaining_days = remaining_days_after_years % 7

# display result
print(f'{Total_days} days is equal to {years} years, {weeks} weeks and {remaining_days} days.')



### 9.Write a program to enter base and height of a triangle and find its area.
# take input
base = int(input('Enter base of triangle:'))
height = int(input('Enter height of triangle:'))
# perform operation
area = 0.5 * base * height
# display result
print(f'Area of triangle is: {area}')



###10. Write a program to calculate area of an equilateral triangle
# take input
side = int(input('Enter side of equilateral triangle:'))
# perform operation
area = (3**0.5 / 4) * side**2
# display result
print(f'Area of equilateral triangle is: {area}')



### 11. Find the area and circumference of circle.
# take input
radius = int(input('Enter radius of circle:'))
# perform operation
area = 3.14 * radius**2
circumference = 2 * 3.14 * radius
# display result
print(f'Area of circle is: {area}')
print(f'Circumference of circle is: {circumference}')



### 12. Find the volume of sphere.
# take input
radius = int(input('Enter radius of sphere:'))
# perform operation
volume = (4/3) * 3.14 * radius**3
# display result
print(f'Volume of sphere is: {volume}')