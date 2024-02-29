# Name:- Mrunali Vikas Patil
# Date:- 02-01-24
# Video Link:- https://www.youtube.com/watch?v=VlCE9BMg4RA
# “I have not given or received any unauthorized assistance on this assignment.”  

def sum_of_squares(n):
    """
    Compute the sum of the squares of each digit in a given number.

    Args:
        n (int): The number to be processed.

    Returns:
        int: The sum of the squares of each digit in n.
    
    This function converts the number to a string to iterate over each digit, 
    squares each digit, and then sums these squared values to return the result.
    """
    return sum(int(digit) ** 2 for digit in str(n))

def is_happy_number(n):
    """
    Determine whether a number is happy or sad based on the happy number definition.

    Args:
        n (int): The number to be evaluated.

    Returns:
        tuple: A tuple containing a string ('happy' or 'sad') indicating the number's status,
               and a list of integers representing the sequence of numbers visited during the evaluation process.
    
    The function iterates through the process of replacing the number with the sum of the squares of its digits,
    tracking each result in a list. The process ends when it either reaches 1 (happy) or enters a loop (sad).
    """
    visited = [n]
    while n != 1 and n not in visited[:-1]:
        n = sum_of_squares(n)
        visited.append(n)
    return ('happy' if n == 1 else 'sad', visited)

def main():
    """
    Main function to interact with the user, evaluating and recording the happiness of entered numbers.

    Continuously prompts the user to enter positive numbers, evaluating each for happiness.
    Upon receiving a finish flag ('end'), the function terminates and prints a summary of results.
    
    The function handles invalid inputs gracefully, requesting valid numbers again without terminating.
    """
    results = {}
    while True:
        try:
            num_input = input("Enter a positive number (or 'end' to finish): ")
            if num_input.lower() == 'end':  # Finish flag
                break
            num = int(num_input)
            if num <= 0:
                raise ValueError  # Ensure the number is positive
            status, sequence = is_happy_number(num)
            results[num] = (status, sequence)
            print(f"{num} is a {status} number: {sequence}")
        except ValueError:
            print("Please enter a valid positive integer.")

    print("\nSumming up the results:")
    print(results)

if __name__ == "__main__":
    main()
