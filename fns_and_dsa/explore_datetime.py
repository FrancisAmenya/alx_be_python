# explore_datetime.py

# Import necessary components from the datetime module
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Part 1: Gets and displays the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    # Obtain the current date and time
    current_date = datetime.now()
    
    # Format and print the current date and time
    # The format codes are: %Y (Year), %m (Month), %d (Day), %H (Hour), %M (Minute), %S (Second)
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    
    # Return the date object for potential reuse in Part 2, though not strictly required by the prompt
    return current_date

def calculate_future_date(current_date):
    """
    Part 2: Prompts the user for a number of days and calculates the future date.

    :param current_date: The starting datetime object (usually the current date).
    """
    while True:
        try:
            # Prompt the user for the number of days
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number (integer) for the number of days.")

    # Create a timedelta object representing the duration
    time_difference = timedelta(days=days_to_add)
    
    # Calculate the future date by adding the timedelta to the current datetime
    future_date = current_date + time_difference
    
    # Format and print the future date in YYYY-MM-DD format (we only want the date part)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    """
    The main execution function to run both parts of the task.
    """
    # Part 1 execution
    print("--- Part 1: Current Date and Time ---")
    start_date = display_current_datetime()
    
    print("\n--- Part 2: Calculate Future Date ---")
    # Part 2 execution, passing the current date as the starting point
    calculate_future_date(start_date)

if __name__ == "__main__":
    main()
