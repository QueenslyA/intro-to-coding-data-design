#Write a program that takes a list of numbers as input and prints the largest and smallest numbers in the list.
#numbers = [12, 3, 5, 19, 7, 3, 1, 5]

numbers = [12, 3, 5, 19, 7, 3, 1, 5]

largest= numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print(f"The largest number is {largest}. ")
print(f"The smallest number is {smallest}. ")