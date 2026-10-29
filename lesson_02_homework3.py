#Ask the user for a numeric grade
grade= input("Enter a numeric grade (0 to 100): ")
#Convert the input to an integer
grade= int(grade)
#Classify the grade
if grade >= 90:
    classification = "A"
elif grade >= 80:
    classification = "B"
elif grade >= 70:
    classification = "C"
elif grade >= 60:
    classification = "D"
else:
    classification = "F"
#Print the classification
print(f"The grade classification is : {classification}")

#Ask the user for their age
age= input("Please enter your age: ")
#Convert the  input to an integer
age= int(age)
#Determine the ticket price based on age
if age <= 3:
    price = "Free"
elif age <= 12:
    price = "$10" 
elif age <= 64:
    price = "$15"
else:
    price = "$5"
#Print the ticket price
print(f"The ticket price is: {price}")

#Ask the user for an integer
number = input("Please enter an integer: ")
#Convert the input to an integer
number = int(number)
#Check the condition
result = (10 <= number <= 50) or (number < 0)
#Print the result
print(f"The condition is: {result}")




    

