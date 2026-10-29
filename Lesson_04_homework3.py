#Ask the user for their favourite colors(up to 5), store them in a list, then print a sentence using joint.
colours = []

amount = int(input("How many favorite colours do you want to enter (max5)? "))

if amount > 5: 
    amount = 5

for i in range(amount):
    colour = input("Enter a favourite colour: ")
    colours.append(colour)

sentence = ",".join(colours)

print(f"Your favorite colours are: {sentence}")