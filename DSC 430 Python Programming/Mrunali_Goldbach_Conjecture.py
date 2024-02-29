# Name:- Mrunali Vikas Patil
# Date:- 02-01-24
# Video Link:- https://www.youtube.com/watch?v=ZWH3QOOqT70
# “I have not given or received any unauthorized assistance on this assignment.”  

def isPrime(pnum):
    """
    Determine if a given integer is a prime number.

    Args:
        pnum (int): The integer to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if pnum <= 1:
        return False
    if pnum <= 3:
        return True
    if pnum % 2 == 0 or pnum % 3 == 0:
        return False
    i = 5
    while i * i <= pnum:
        if pnum % i == 0 or pnum % (i + 2) == 0:
            return False
        i += 6
    return True

def Goldbachs_Conjecture_Less_Than100():
    """
    Verify Goldbach's Conjecture for all even integers less than 100.

    Prints:
        Each even integer followed by a pair of prime numbers that sum up to it.
    """
    for total in range(4, 100, 2):  # Main loop iterating over even integers from 4 to 98
        for p1num in range(2, total//2 + 1):  # Nested loop to find two primes that sum up to 'total'
            p2num = total - p1num
            if isPrime(p1num) and isPrime(p2num):  # Check if both numbers are prime
                print(f"{total} = {p1num} + {p2num}")
                break  # Exit the loop once a valid pair of primes is found

Goldbachs_Conjecture_Less_Than100()  # Function call to execute the verification
