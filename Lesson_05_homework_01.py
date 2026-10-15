#This dictionary will store all cities.
#Key = city name, Value = another dictionary with the details.

cities = {}
city = input("Please enter the name of a city: ")
while city != "exit":
    unit = input("Would you like to enter the temperature in Fahrenheit or Celcius?: ")
    if unit.lower() == "celcius":
        temp_c = float(input(f"Please enter the current temperature in Celcius in {city}: "))
        temp_f = (temp_c * 9/5) + 32
    else:
        temp_f = float(input(f"Please enter the current temperature in Fahrenheit in {city}: "))
        temp_c = (temp_f - 32) * 5/9

    raining = input(f"Is it raining in{city}? (yes/no): ")
    sunny = input(f"Is the sun shining in {city}? (yes/no): ")

    #Store everything about this city in its own dictionary
    cities[city] = {
        "celsius": temp_c,
        "Fahrenheit": temp_f,
        "raining": raining,
        "sunny": sunny,
    }

    print("-----------")
    city = input("Please enter the name of a city: ")

#Print the summary for every city
print("---------")
print("Summary:")

for city in cities:
    info = cities[city]

    if info["sunny"] == "yes":
        sun_text = "sun"
    else:
        sun_text = "no sun"

    if info["raining"] == "yes":
        rain_text = "rain"
    else:
        rain_text = "no rain"

    print(f"{city}: {info['celsius']:.1f}°C, {info['Fahrenheit']:.1f}°F, {sun_text} and {rain_text}")

    if info["celsius"] < 0:
        print(f"Warning: The temperature in {city} is below the freezing point")

    if info["raining"] == "yes" and info["sunny"] == "yes":
        print(f"There is a rainbow in {city}.")
    print("-------")
