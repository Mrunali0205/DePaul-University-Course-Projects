# Name:- Mrunali Vikas Patil
# Date:- 02-08-24
# Video Link:- https://www.youtube.com/watch?v=AnzkBcRILrM
# “I have not given or received any unauthorized assistance on this assignment.”  

import random

def get_input(prompt, min_val=1, max_val=100):
    """Prompt the user for an integer input with specified range and error handling."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def binary_search(arr, x, start):
    """Perform binary search for x in arr starting from index start to the end of the array."""
    low = start
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

def find_pair_with_sum(arr, target_sum):
    """Determine if any two numbers in the sorted array sum up to the target sum."""
    for i in range(len(arr)):
        complement = target_sum - arr[i]
        if binary_search(arr, complement, i + 1):
            return (arr[i], complement)
    return None

def main():
    length = get_input("Enter the length of the list (1-100): ")
    target_sum = get_input("Enter the target sum (1-100): ")

    # Generate a list of `length` random numbers between 0 and 100
    random_list = [random.randint(0, 100) for _ in range(length)]
    random_list.sort()  # Sort the list as a preprocessing step

    print(f"Sorted list of random numbers: {random_list}")  # Print the generated list

    result = find_pair_with_sum(random_list, target_sum)
    if result:
        print(f"Pair found that sums to {target_sum}: {result}")
    else:
        print(f"No pair found that sums to {target_sum}.")

if __name__ == "__main__":
    main()
