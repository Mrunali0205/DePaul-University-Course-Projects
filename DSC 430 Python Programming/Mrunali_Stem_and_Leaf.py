# -- ASSIGNMENT 2 --
#Author - Mrunali Vikas Patil
#Student ID - 2134049
#Date - 01/24/2024
#Video_Link - https://www.youtube.com/watch?v=Sr9MOVwhCe4
#Honor Statement - "I have not given or received any unauthorized assistance on this assignment.”


def loadSortedData(fileNumber):
    '''
    Loads and sorts data from the text file.

    Args:
        fileNumber (int): Number indicating which file to read (1, 2, or 3).
    
    Returns:
        sortedData (list): Sorted list of integer values from the file.
    '''
    pathToFile = f"/Users/mrunalipatil/Downloads/StemAndLeaf{fileNumber}.txt" #This function reads a file named "StemAndLeaf{fileNumber}.txt" from a predefined path. 
    with open(pathToFile, "r") as file:                                       #Reads and sorts integers from the file.
        sortedData = sorted([int(line.strip()) for line in file])
    return sortedData

def createStemLeafStructure(data):
    '''
    Creates a stem-and-leaf structure from the given data.
 It divides each number into a stem (the tens place) and a leaf (the units place), and organizes these into a dictionary where each stem is a key and the corresponding leaves are values in a list.

    Args:
        data (list): Sorted list of integers.
    
    Returns:
        stemLeafDict (dict): Dictionary with stems as keys and leaves as values.
    '''
    stemLeafDict = {}                                  #This function iterates over each number in the provided sorted list of integers.
    for number in data:                            
        stem = number // 10
        leaf = number % 10
        stemLeafDict.setdefault(stem, []).append(leaf) # Splits numbers into stems and leaves, storing them in a dictionary.
    return stemLeafDict

def visualizeStemAndLeaf(stemLeaf):
    '''
    Visualizes the stem-and-leaf plot from the given structure.

    Args:
        stemLeaf (dict): Stem-and-leaf structure.
    '''
    for stem, leaves in stemLeaf.items():            # This function takes a stem-and-leaf structure (a dictionary) and prints it in a formatted manner to represent a stem-and-leaf plot.
        leavesFormatted = ' '.join(map(str, leaves)) #Each line of output represents a stem and its corresponding leaves.
        print(f'{stem} | {leavesFormatted}')
    print('----------------------------------------------------------------------------')

def ExecuteStemAndLeafProgram():
    '''
    Main function to run the Stem and Leaf Plot program.

    '''
    print("Hello! Let's explore some Stem and Leaf plots, I hope you are doing great!") 
    while True:
        print("Choose 1, 2, or 3 to view a plot, or 0 to exit.") #This function initiates an interactive session where the user can choose to visualize stem-and-leaf plots based on data from different files.
                                                                 
        try:
            selection = int(input('Your choice: '))              #The user inputs a number corresponding to the file they wish to visualize, and the program displays the stem-and-leaf plot.
            if selection == 0:                                   #  The user can exit the program by entering 0.
                break
            elif 1 <= selection <= 3:
                data = loadSortedData(selection)
                stemLeaf = createStemLeafStructure(data)
                visualizeStemAndLeaf(stemLeaf)
            else:
                print('Enter a valid number (0, 1, 2, or 3)!')
                print('----------------------------------------------------------------------------')
        except ValueError:
            print("Input must be an integer.")
            print('----------------------------------------------------------------------------')

ExecuteStemAndLeafProgram()
