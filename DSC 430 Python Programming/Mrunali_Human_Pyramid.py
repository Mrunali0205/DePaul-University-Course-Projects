# Name:- Mrunali Vikas Patil
# Date:- 02-08-24
# Video Link:- https://www.youtube.com/watch?v=jQjoTLEzP5o
# “I have not given or received any unauthorized assistance on this assignment.”  


def humanPyramid(row, column):
    """
    Calculate the total weight on a person's back in a human pyramid.

    Args:
        row (int): The zero-indexed row number of the person in the pyramid, where 0 is the top row.
        column (int): The zero-indexed column number of the person in the pyramid, where 0 is the leftmost position in the row.

    Returns:
        float: The total weight on the person's back in pounds, including their own weight and half the weight of any people directly above them.
    """
    # Base case: If we are at the top of the pyramid, there's no weight on the person's back
    if row == 0:
        return 0

    # Weight of the person themselves
    own_weight = 128

    # Recursive case: Calculate the weight on the person's back from the people above
    weight_above = 0
    if column > 0:  # There's a person directly above to the left
        weight_above += (humanPyramid(row - 1, column - 1) + own_weight) / 2
    if column < row:  # There's a person directly above to the right
        weight_above += (humanPyramid(row - 1, column) + own_weight) / 2

    # The total weight includes the weight from above
    return weight_above  # The person's own weight is included in the recursive call from above

def main():
    """
    Main function to run the human pyramid weight calculation. It prompts the user for row and column numbers, then calculates and prints the total weight on that person's back.
    """
    while True:
        try:
            # Ask the user for the row and column, with error handling
            row = int(input("Enter the row number (starting from 0): "))
            column = int(input("Enter the column number (starting from 0): "))
            if row < 0 or column < 0:
                raise ValueError("Row and column numbers must be non-negative.")
            if column > row:
                raise ValueError("Column number cannot be greater than row number in a human pyramid.")
            break  # Input is valid, break the loop
        except ValueError as e:
            print(f"Invalid input: {e}")

    # Calculate and print the total weight on the person's back
    total_weight = humanPyramid(row, column)
    print(f"The total weight on the person's back at row {row}, column {column} is {total_weight} pounds.")

# Run the main function
if __name__ == "__main__":
    main()
