def isPasswordInvalid(password):
    if len(password) <= 4:
        return True
    elif "!" not in password:
        return True
    elif password == "12345":
        return True
    else:
        return False


password = input("enter password: ")

while isPasswordInvalid(password):
    print("invalid password!")
    password = input("enter password: ")

print("password created successfully!")


password = input("enter password: ")

while len(password) <= 4 or "!" not in password or password == "12345":
    print("invalid password!")
    password = input("enter password: ")

print("password created successfully!")