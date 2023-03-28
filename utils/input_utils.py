"""This module contains functions to get user input and validate it"""

def user_input(prompt, validation_function=None):
    """Get the duration of the learning session from the user"""
    value = input(prompt)

    if validation_function:
        if validation_function(value) is False:
            value = user_input(prompt, validation_function)
    return int(value)

def validate_learning_duration(value):
    """Validate the duration of the learning session"""
    duration = value
    try:
        duration = int(duration)
    except ValueError:
        print("Error: please enter a number \n")
        return False
    try:
        if (duration < 3) or (duration > 600):
            raise ValueError ("Error: the duration is out of range. \n")
    except ValueError as error:
        print(error)
        print("- The minimun learning session is 3 min and the maximum is 600 min (10 hours).")
        print("-- Please enter a value between those (in minutes)")
        print("-- You entered: " + str(duration) + " minute(s)")
        print("- Tip: research shows that ~90 min is the longest period we can expect to maintain intense focus and effort toward learning. - Huberman, 2022 \n")
        return False
    return True
