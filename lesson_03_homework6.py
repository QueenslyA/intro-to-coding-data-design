# Init variables for the highest and lowest temperatures and the corresponding city names
highest_temp = None
highest_city = ""
lowest_temp = None
lowest_city = ""

city = input("Please enter the name of a city: ")

while city.lower() != "exit":
    # Ask the user for the current temperature in Fahrenheit
    temp_f = input(f"Please enter the current temperature in Fahrenheit in {city}: ")
    temp_f = float(temp_f)

    # Convert the temperature to Celsius
    temp_c = (temp_f -32) * 5/9

    # Print the user input in a formatted string
    print(f"The current temperature in {city} is {temp_f:.1f}°F or {temp_c:.1f}°C")

    # Check if the temperature is below freezing point
    if temp_f < 32:
        print("Warning: The temperature is below freezing point.")

    # Check if the current temperature is the highest 
    if highest_temp is None or temp_c > highest_temp:
        highest_temp = temp_c
        highest_city = city

    # Check if the current temperature is the lowest 
    if lowest_temp is None or temp_c < lowest_temp:
        lowest_temp = temp_c
        lowest_city = city

    print("")

    # Ask the user for the city name
    city = input("Please enter the name of a city: ")

# Print the summary
print("Summary:")
print(f"the highest temperature is {highest_temp:.1f}°F in {highest_city}.")
print(f"the lowest temperature is {lowest_temp:.1f}°F in {lowest_city}.")



