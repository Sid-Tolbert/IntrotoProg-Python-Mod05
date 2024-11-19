# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

# Importing JSON
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = []  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
# Error handling to see if there is a JSON file.
try:
    file = open(FILE_NAME, "r")
    for row in file:
        data: list = row.split(",")
        row = {"First Name": data[0], "Last Name": data[1], "Course Name": data[2].strip()}
        students.append(row)
    file.close()
except FileNotFoundError as e:
    print("JSON File with content must exist before running this script.")
# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    # Error handling if the user tries to use numbers in the first name.
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")

            # Student name can't have numbers
            if student_first_name.isnumeric():
                raise ValueError("Student Name can't have numbers in it.")

            student_last_name = input("Enter the student's last name: ")

            # Student name can't have numbers
            if student_last_name.isnumeric():
                raise ValueError("Student Name can't have numbers in it.")

            course_name = input("Please enter the name of the course: ")
            student_data = {"First Name": student_first_name, "Last Name": student_last_name,"Course Name": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            continue
        except ValueError as e:
            print("There can't be numbers in a student's name.")
    # Present the current data
    elif menu_choice == "2":

    # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['First Name']} {student['Last Name']} is enrolled in {student['Course Name']}")
        print("-"*50)
        # Data collected for menu choice 1 is added to a two-dimensional list table (list of dictionaries)

        continue

    # Save the data to a file
    # Error handling for all error types
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                json_data = f"{student['First Name']},{student['Last Name']},{student['Course Name']}\n"
                file.write(json_data)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['First Name']} {student['Last Name']} is enrolled in {student['Course Name']}")
            continue
        except Exception as e:
            print("Erroneous Behavior!")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
