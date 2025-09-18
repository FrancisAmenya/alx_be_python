# Prompt the user to enter their current weather
current_weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Providing a recommendation
recommendation = ""

if current_weather == "sunny":
	recommendation = "Wear a t-shirt and sunglasses."
elif current_weather == "rainy":
	recommendation = "Don't forget your umbrellaand raincoat"
elif current_weather == "cold":
	recommendation = "Make sure to wear a warm coat and scarf"
else:
	recommendation = "Sorry, I don't hae recommendations for this weather."

# Printing the user's recommendation in the format
print(f"{recommendation}")
