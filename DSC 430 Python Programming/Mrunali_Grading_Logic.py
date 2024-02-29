# -- ASSIGNMENT 1 --
#Author - Mrunali Vikas Patil
#Student ID - 2134049
#Date - 01/18/2024
#Video_Link - https://www.youtube.com/watch?v=CYBEm6DwP3E&t=1s 
#Honor Statement - "I have not given or received any unauthorized assistance on this assignment.”

#Creating a Function to grade a student's assignment based on specific criteria.
#Returns the total score if all conditions are met, otherwise returns 0.

def grade_assignment():

#CONDITION 1
    # This section of the code is responsible for verifying the format of the submitted assignment.
    # It specifically checks if the assignment has been provided as a single, uncompressed Python file (.py).
    # If the student has not adhered to this format requirement, the function will immediately return  0,
    if input("Is the assignment submitted as a single uncompressed .py file? (yes/no): ").lower() != 'yes':
        return 0


#CONDITION 2
    # This section of the code verifies if the submitted assignment includes the author's name and the date of submission.
    # These details are essential for identifying the student and tracking the assignment's submission time.
    # If either the author's name or the date is missing, the assignment does not meet the basic submission criteria, the function will return 0
    if input("Does the assignment include the author's name and date? (yes/no): ").lower() != 'yes':
        return 0

#CONDITION 3
    # Verifying the inclusion of the academic integrity declaration
    if input("Does the assignment include the honor statement? (yes/no): ").lower() != 'yes':
        return 0

#CONDITION 4
    #This part of the code is crucial as it ensures that the student has adhered to the requirement of including a link to a YouTube video. 
    # The video is supposed to be a 3-minute presentation explaining their code and answering the assigned questions. 
    if input("Does the assignment include a link to an unlisted 3-minute YouTube video? (yes/no): ").lower() != 'yes':
        return 0

# If all above conditions are satisfied, proceed to grading
    correctness = int(input("Out of ten points, how would you evaluate the correctness of the code? "))
    elegance = int(input("Out of ten points, how would you evaluate the elegance of the code? "))
    hygiene = int(input("Out of ten points, how would you evaluate the code hygiene? "))
    video_quality = int(input("Out of ten points, how would you evaluate the quality of the discussion in the YouTube video? "))

# Calculating the total score
    total_score = correctness + elegance + hygiene + video_quality

    late_submission = input("Is Assignment Late ? (yes/no): ")

    if late_submission.lower() == 'yes':  # Converts the input to lowercase and checks if it's 'yes'

    # Check for lateness
        delayed_submission_duration = int(input("How many hours late was the assignment submitted? "))  #The student is asked to input the number of hours by which their assignment was submitted late.
        
        total_score -= delayed_submission_duration * 0.01 * total_score  # 1% of the total possible score is deducted for each hour the assignment is late.

        return max(0, int(total_score))  #Max function is used to ensure that the score does not fall below 0.

    return total_score

#Demonstration of Use
Score = grade_assignment()
print(f"The student's total score is: {Score}")


