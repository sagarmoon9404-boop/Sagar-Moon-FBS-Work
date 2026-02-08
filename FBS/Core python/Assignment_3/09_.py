sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))

total = sub1 + sub2 + sub3 + sub4+ sub4
average = (total / 500) * 100

if average >= 80:
    print("First Class")
elif average >= 60:
    print("Second Class")
elif average >= 40:
    print("Pass Class")
else:
    print("Fail")
