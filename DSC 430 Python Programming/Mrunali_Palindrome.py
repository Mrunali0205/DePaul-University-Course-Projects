# Name:- Mrunali Vikas Patil
# Date:- 02-22-24
# Vide Link - https://www.youtube.com/watch?v=VLF_hUJqSTw&t=2s
# “I have not given or received any unauthorized assistance on this assignment.”  

def is_valid_date(day, month):
    """
    Check if the given day and month form a valid date, assuming all months have 30 days for simplicity.

    Args:
        day (int): The day part of the date.
        month (int): The month part of the date.

    Returns:
        bool: True if the day and month form a valid date, False otherwise.
    """
    return 1 <= day <= 30 and 1 <= month <= 12

def find_palindrome_dates():
    """
    Identify and save all palindrome dates in the 21st century in the DD/MM/YYYY format.
    A palindrome date is a date that reads the same backward as forward.

    This function iterates through each year in the 21st century, constructs a date by reversing the digits of the year,
    and checks for its validity. Valid palindrome dates are saved to a file named 'unique_palindrome_dates.txt'.
    """
    palindrome_dates = []

    for year in range(2001, 2101):
        # Construct the date in DD/MM format by reversing the last two digits of the year
        # and using the last but one (and the one before it if needed) as the month
        day = int(str(year)[2:])
        month = int(str(year)[1::-1])  # Reverse the first two digits to get the month

        if is_valid_date(day, month):
            date_str = f"{day:02d}/{month:02d}/{year}"
            palindrome_dates.append(date_str)

    # Write palindrome dates to a file
    with open('unique_palindrome_dates.txt', 'w') as file:
        for date in palindrome_dates:
            file.write(date + '\n')

    print(f"Found {len(palindrome_dates)} palindrome dates.")

if __name__ == "__main__":
    # Run the function to find palindrome dates
    find_palindrome_dates()
