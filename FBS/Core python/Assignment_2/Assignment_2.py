### 1. Convert the time entered in hh,min and sec into seconds.
#take input
hour = int (input("Enter Hours:"))
minute = int(input("Enter Minutes:"))
second = int(input("Enter Seconds:"))
#perform operation
convert_all_to_seconds = (hour * 3600) + (minute * 60) + second
#display result
print(f"total second is: {convert_all_to_seconds} seconds")



### 2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)
#take input
celsius = float (input("Enter temperature in Celsius: "))
#perform operation
fahrenheit =(celsius * 9/5) + 32
#display result
print(f"Temparature in Fahrenheit is : {fahrenheit} F")



### 3. Convert distant given in feet and inches into meter and centimeter.
#take input
feets= float(input("enter feet: "))
inches = float(input("enter inches: "))
#perform operation
meters = (feets * 0.3048) + (inches * 0.0254)
centimeters = (meters * 100) + (inches * 2.54)
#display result
print(f"Length in meters is: {meters} m")
print(f"Length in centimeters is: {centimeters} cm")    


### 4. WAP to calculate area of triangle and rectangle
#take input
length_1 = int (input("Enter length of rectangle: "))
length_2 = int (input("Enter length of triangle: "))
breadth = int (input("Enter breadth of rectangle: "))
height = int (input("Enter height of triangle: "))
#perform operation
area_of_rectangle = length_1 * breadth
area_of_triangle = 0.5 * length_2 * height
#display result
print(f"Area of rectangle is : {area_of_rectangle} Sq")
print(f"Area of triangle is : {area_of_triangle} Sq")


### 5. WAP to calculate selling price of book based on cost price and discount.
#take input
cost_price = int (input("Enter cost price: "))
discount_percentage =int ( input("Enter discount percentage: "))
#perform operation
selling_price = cost_price - (cost_price * discount_percentage / 100)
#display result
print(f"Selling price is : {selling_price} ")



### 6. WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.
# take input
basic = int(input("Enter basic salary: "))
da = (10 / 100) * basic 
ta = (12 / 100) * basic
hra = (15 / 100) * basic
total_salary = basic + da + ta + hra    
#display result
print(f"DA is : {da} ")
print(f"TA is : {ta} ")
print(f"HRA is : {hra} ")
print(f"Total salary of employee is : {total_salary} ")



# 7. Find the sum of three-digit number.
# take input
number = int(input ("Enter the three digit number:"))
# perform operation
hundreds = number // 100
tens = (number // 10) % 10              
units = number % 10
sum_of_digits = (hundreds + tens + units)
# display result
print(f"The sum of digits in {number} is: {sum_of_digits}")



### 8. Write a program to swap two numbers using third variable.
# take input
x = 10
y = 20
# perform operation
z =x
x=y
y=z
# display result
print(f'after swapping- x:{x}, y:{y}')



### 9. write a program to swap two number without using third variable.
#take input
a=20
b=50
print(f'Before swapping- a:{a}, b:{b}')
#perform operation
a,b=b,a
#display result
print(f'After swapping- a:{a}, b:{b}')



### 10. Write a program to reverse three-digit number.
# take input
num =  int(input('Enter three digit Number:'))
# perform operation
hundreds = num // 100
tens = (num // 10) % 10 
units = num % 10
reverse_number = (units * 100) + (tens * 10) + hundreds
# display result
print(f'Reverse of {num} is: {reverse_number}')



# 11. Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.
# take input
integer_amount = int(input("Enter amount: "))
# perform operation
Five_hundred = integer_amount // 500
integer_amount = integer_amount % 500
Two_hundred = integer_amount // 200
integer_amount = integer_amount % 200
One_hundred = integer_amount // 100
integer_amount = integer_amount % 100
Fifty = integer_amount // 50
integer_amount = integer_amount % 50
Twenty = integer_amount // 20
integer_amount = integer_amount % 20
Ten = integer_amount // 10
integer_amount = integer_amount % 10
Five = integer_amount // 5
integer_amount = integer_amount % 5
Two = integer_amount // 2
integer_amount = integer_amount % 2
One = integer_amount // 1
# display result
print(f"500 : {Five_hundred}")
print(f"200 : {Two_hundred}")
print(f"100 : {One_hundred}")
print(f"50 : {Fifty}")
print(f"20 : {Twenty}")
print(f"10 : {Ten}")
print(f"5 : {Five}")
print(f"2 : {Two}")
print(f"1 : {One}")