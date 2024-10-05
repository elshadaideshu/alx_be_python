# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32  # Fahrenheit offset for conversion

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_OFFSET

# Main function for user interaction and input validation
def main():
    try:
        # Get temperature input from the user
        temp_input = input("Enter the temperature to convert: ")
        
        # Attempt to convert the input to a float (to handle numeric validation)
        try:
            temp = float(temp_input)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        # Ask the user which unit the input temperature is in (Celsius or Fahrenheit)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Convert based on the unit provided
        if unit == 'C':
            # Celsius to Fahrenheit conversion
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
        elif unit == 'F':
            # Fahrenheit to Celsius conversion
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
        else:
            # Handle invalid unit input
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as ve:
        # Handle invalid numeric input
        print(ve)

# Entry point for the script
if __name__ == "__main__":
    main()