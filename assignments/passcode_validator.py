import re


def password_validator():
    # Created a Regex object to valid a pattern.
    pattern = re.compile("(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@])(?=.*[0-9])")

    flag = 0  # created a flag to later check if none of the entered passwords were valid.

    # Getting inputs from users and creating a list.
    password = input("Enter passcodes: ")
    password = password.split(",")

    # Created a list to store valid length of passwords.
    passcode_list = []

    # Checking the length of passwords.
    for code in password:
        if 12 >= len(code) >= 6:
            passcode_list.append(code)

    # Checking if the passwords matches the pattern.
    for code in passcode_list:
        result = pattern.search(code)
        if result != None:
            flag = 1
            print(f"{code} is a valid password!")

    if flag == 0:
        print("None of the provide passwords were valid.")


password_validator()
