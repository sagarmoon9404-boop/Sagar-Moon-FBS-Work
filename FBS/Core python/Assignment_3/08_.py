
import random
correct_userid = "admin"
correct_password = "1234"

# Take user input
userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Verify 
if userid == correct_userid and password == correct_password:
    # Generate 4-digit random number
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)

    user_captcha = int(input("Enter the captcha number: "))

    # Verify captcha
    if user_captcha == captcha:
        print("Login Successful ✅")
    else:
        print("Captcha Verification Failed ")
else:
    print("Invalid User ID or Password ")
