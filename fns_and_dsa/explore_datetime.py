from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in a readable format.
    """
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days: int):
    """
    Calculates and displays the future date after adding the specified number of days to the current date.

    Parameters:
    days (int): The number of days to add.
    """
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date
    future_date = current_date + timedelta(days=days)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate a future date
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days_to_add)

if __name__ == "__main__":
    main()