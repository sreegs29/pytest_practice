# Formatting Numbers

"""
1. Take a number as an input.
2. Check if it is a negative number.
3. If yes, prompt to enter positive number.
4. Convert the numbers into string datatype and add comma as a thousand seperator.
"""


def format_number():
    str1 = ''
    while True:
        num = input("Enter a number: ")
        if num < '0':
            print("Please enter a non-negative number!")
        else:
            counter = 0
            for i in num[::-1]:
                if counter == 3:
                    str1 = str1 + ','
                    counter = 0
                str1 += i
                counter += 1
        break

    return str1[::-1]


result = format_number()
print(result)
