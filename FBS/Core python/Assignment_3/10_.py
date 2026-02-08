gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if (gender in ["male","m","M","MALE"] and age >= 21) or (gender in["female","f","F","FEMALE"] and age >= 18):
    print("Eligible for marriage")
else:
    print("Not eligible for marriage")
