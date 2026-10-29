# Ask the user for the city name
    
city = input("Please enter the name of a city: ")
while city.lower() != "exit":
    # Ask the user for the current temperature in Fahrenheit
    temp_f = input(f"Please enter the current temperature in fahrenheit in {city}: ")
    temp_f = float(temp_f)

    # Convert the temperature to Celsius
    temp_c = (temp_f - 32) * 5/9

    # Print the user input in a formatted string
    print(f"The current temperature in {city} is {temp_f:.1f}°F or {temp_c:.1f}°C.")

    # Check if the temperature is below freezing point
    if temp_f < 32:
        print("Warning: The temperature is below freezing point. ")
    print("")

    # Ask the user for the city name
    city = input("Please enter the name of a city: ")

