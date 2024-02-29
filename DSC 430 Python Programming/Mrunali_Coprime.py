# -- ASSIGNMENT 1 --
#Author - Mrunali Vikas Patil
#Student ID - 2134049 
#Date - 01/18/2024
#Video_Link - https://www.youtube.com/watch?v=2KxbV2A8GpY&t=105s
#Honor Statement - "I have not given or received any unauthorized assistance on this assignment.”

def coprime(a, b):
    """
    Determinining if two integers a and b are coprime.
    
    Parameters:
    a (int): First integer
    b (int): Second integer

    Returns:
    bool: True if a and b are coprime, False otherwise
    """
    # Using Euclidean algorithm to find the GCD(greatest common divisor)
    while b != 0:                                           #The while loop continues its execution as long as the variable b is not zero.
        a, b = b, a % b                                     #The value of a is updated to the current value of b, and b is updated to the remainder when a is divided by b.
    return a == 1                                           # If GCD is 1, numbers are coprime

def coprime_test_loop():
    """
    Interactive loop to test if pairs of numbers are coprime.
    
    Continues until the user decides to exit.
    """
    while True:                                         # This comment in the code marks where the program is set to receive and handle the input provided by the user, capturing the numbers they enter for coprime evaluation.
        input_str = input("Enter two numbers separated by a space (or type 'exit' to quit): ")
        if input_str.lower() == 'exit':                 #This part of the code checks if the user input is 'exit', and if so, it terminates the loop to end the program.
            break
        try:
            a, b = map(int, input_str.split())              #This code section takes the user's input string, which is expected to contain two numbers separated by a space, and divides it into two separate numerical values for further processing.
            
            if coprime(a, b):                               # Checking if numbers are coprime
                print("The given 2 numbers are coprime")
            else:
                print("The given 2 numbers are not coprime")
        except ValueError:
                # Error handling for invalid input
            print("Please enter valid integers.")
 # Running the loop function
coprime_test_loop()
