#Ask the user for the city names
city1= input("Enter the name of the first city: ")
city2= input("Enter the name of the second city: ")

#Ask the user for the current temperatures in Fahrenheit
temperature1_f= input(f" Enter the current temperature for {city1} in Fahrenheit: ")
temperature2_f= input(f"Enter tne current temperature for {city2} in Fahrenheit: ")

#Convert the temperatures to float
temperature1_f= float(temperature1_f)
temperature2_f= float(temperature2_f)

#Convert the temperatures to Celcius
temperature1_c= (temperature1_f - 32) * 5/9
temperature2_c= (temperature2_f - 32) * 5/9

#Check if the temperatures are below freezing point
if temperature1_f < 32 and temperature2_f < 32:
    print("Alert: The temperatures in both cities are below freezing point. ")
elif temperature1_f < 32 or temperature2_f < 32:
    print("Alert: the temperature in one of the cities is below freezing point. ")
else:
    print(" The temperature in both cities are above  the freezing point. ")
    
#Print the user input in a formatted string
print(f"the current temperature in {city1} is {temperature1_c:.1f} degree Celcius. ")
print(f"The current temperature in {city2} is {temperature2_c:.1f} degree Celcius. ")