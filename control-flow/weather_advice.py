# Prompt the user to enter their current weather
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Providing a recommendation
recommendation = ""

if weather == "sunny":
	recommendation = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
	recommendation = "Don't forget your umbrella and raincoat."
elif weather == "cold":
	recommendation = "Make sure to wear a warm coat and scarf."
else:
	recommendation = "Sorry, I don't hae recommendations for this weather."

# Printing the user's recommendation in the format
print(f"{recommendation}")
