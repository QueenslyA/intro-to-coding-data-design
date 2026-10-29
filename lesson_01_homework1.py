city=input("Enter the name of a city: ")
temperature=input(f"Enter the current temperature in celsius in {city}: ")
temperature=float(temperature)
print(f"the current temperature in {city} is {temperature} Degrees Celsius. ")

city_1=input("Enter the name of the first city: ")
city_2=input("Enter the name of the second city: ")
temperature_1=input(f"Enter the current temperature for {city_1}: ")
temperature_2=input(f"Enter the current temperature for {city_2}: ")
temperature_1=float(temperature_1)
temperature_2=float(temperature_2)
average_temperature=(temperature_1 + temperature_2) / 2
print(f"the average temperature between {city_1} and {city_2} is {average_temperature} Degree Celsius. ")

average_temperature_fahrenheit= average_temperature * 9/5 + 32
print(f"That's {average_temperature_fahrenheit} degrees Fahrenheit. ")