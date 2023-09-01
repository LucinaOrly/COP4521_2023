"""
Name:John Valencia-Londono
Date:8/31/2023
Assignment:Module1:SecretMessage
Due Date:01/13/2021
About this project:
Assumptions:NA
All work below was performed by John Valencia-Londono """

num = int(input('Enter a positive numeric value greater than zero: '))
if num <= 0:
    print("Invalid input (must be greater than zero).")
    exit(1)

direction = input('Enter a direction (R/L): ').upper().strip()
multiplier = 0
if direction == 'R':
    multiplier = 1
else:
    if direction == 'L':
        multiplier = -1
    else:
        print("Invalid input (must be 'R' or 'L'")
        exit(1)


# shifts character ch by n (wrap ascii values between [65, 90])
def caesar_shift(ch, n):
    if not ch.isalpha():
        return ch
    res = ((ord(ch) - 65) + n) % (91 - 65)
    return chr(res + 65)


string = input('Enter a string: ').upper()

result = ''
for i in [c for c in string]:
    result += (caesar_shift(i, num * multiplier))

print(result)
