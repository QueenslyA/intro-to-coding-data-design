#Ask the user for the city name
city= input("Enter the name of a city: ")
#Ask the user for the current temperature in Fahrenheit
temperature_f= input("Enter the current temperature in Fahrenheit: ")
#Convert the temperature to float
temperature_f= float(temperature_f)
#Convert the temperature to Celcius
temperature_c= (temperature_f - 32) * 5/9
#Check if the temperature is below freezing point
if temperature_c < 0:
    print("Alert: The temperature is below freezing point. ")
else:
    print("The temperature is above the freezing point. ")    
#Print the user input in a formatted string
print(f"The current temperature in {city} is {temperature_c:.1f} degree Celcius. ")