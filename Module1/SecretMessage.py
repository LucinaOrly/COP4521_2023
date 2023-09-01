"""
Name:John Valencia-Londono
Date:8/31/2023
Assignment:Module1:SecretMessage
Due Date:01/13/2021
About this project:
Assumptions:NA
All work below was performed by John Valencia-Londono """

num = input('Enter a positive numeric value greater than zero: ')
if num <= 0:
    print("Invalid input (must be greater than zero).")
    exit()

dir = input('Enter a direction (R/L): ').upper
if dir == 'R' or dir == 'L':
else:
    print("Invalid input (must be 'R' or 'L'")
    exit()

def caesar_shift(ch, n):
    if not ch.isalpha()
        return ch
    res = ( ( ord(ch) - ord('A') ) + n ) % (90 - 65)
    return chr( res + ord('A') )

str = input('Enter a string: ').upper
encod = [caesar_shift(X)]

# shifts character ch by n (wrap ascii values between [65, 90])





