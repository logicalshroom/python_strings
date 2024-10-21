# 2. User Input Data Processor
# Objective: The aim of this assignment is to process and format user input data.
# 
# Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

def namecheck():
    first_name = input("Hello, User. Please input your name.")
    last_name = input("Please input your last name.")
    if len(first_name) < 2:
        print("Error: your name must contain at least 2 characters")
    elif len(last_name) < 2:
        print("Error: your name must contain at least 2 characters")
    else:
        print(f"You entered the name {first_name} {last_name}")

namecheck()