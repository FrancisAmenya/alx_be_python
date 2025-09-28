# temp_conversion_tool.py

# Define Global Conversion Factors
# Note: It's important to use floating-point numbers (e.g., 5.0/9.0) for accurate division.
# Global variables are automatically available for reading inside functions.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_DIFFERENCE = 32

# The formulas are:
# C = (F - 32) * (5/9)
# F = (C * (9/5)) + 32

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.

    :param fahrenheit: Temperature in degrees Fahrenheit (float).
    :return: Temperature in degrees Celsius (float).
    """
    # The function reads the global variable FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - FREEZING_POINT_DIFFERENCE) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.

    :param celsius: Temperature in degrees Celsius (float).
    :return: Temperature in degrees Fahrenheit (float).
    """
    # The function reads the global variable CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_DIFFERENCE
    return fahrenheit

def main():
    """
    Handles user interaction, input validation, and calls the appropriate conversion function.
    """
    print("--- Temperature Conversion Tool ---")
    
    # --- 1. Get and Validate Temperature Input ---
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)
    except ValueError:
        # Raise the specific error required for non-numeric input
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    # --- 2. Get and Validate Unit Input ---
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    # --- 3. Perform and Display Conversion ---
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        # Display output as specified in the example
        print(f"{temperature}°F is {converted_temp}°C")
    
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        # Display output as specified in the example
        print(f"{temperature}°C is {converted_temp}°F")
    
    else:
        # Handle invalid unit input
        print("Invalid unit input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)
