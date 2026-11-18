#Random Password Generator first Draft
#Step 1: Import the random library
import random

#Step 2: Create the characters the password can be made of
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Small_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%&*()-_=+?^"

#Put all characters together in one string
all_characters = capital_letters + Small_letters + numbers + symbols

print("Welcome to the Random Password Generator!")
again = "yes"

while again == "yes":
#Step 3: Ask the user for the lenght of the password
    length = int(input("How long should your password be (4 to 50)?"))

#Step 4: Keep asking until the length is between 4 and 50
while length < 4 or length > 50:
    print("Sorry, please choose a lenght betwween 4 and 50.")
    length = int(input("How long should your password be (4 to 50)?"))

#Step 4: generate the password
password = ""
for i in range(length):


    
