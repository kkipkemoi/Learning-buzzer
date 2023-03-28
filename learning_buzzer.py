"""A buzzer that goes of every few minutes to iniate a micro break to enable you to learn faster"""
import os
import time
import random
from playsound import playsound # version 1.2.2 of this module had to be installed, version 1.3.0 does not work (consistantly)

MICRO_BREAK_DURATION = 10
AVERAGE_INTERVAL_SIZE = 300 # the average interval between buzzers in seconds
DEVIATION = 0.2 # the deviation from the average interval used to introduce randomness of when buzzer goes off 
SPEED_UP_FACTOR_FOR_TESTS = 40 # the factor by which the duration and intervals are shortened for testing purposes

SOUND_START = os.path.join(os.path.dirname(__file__), "sounds/aurora_trimmed_4seconds.mp3")
SOUND_BUZZER = os.path.join(os.path.dirname(__file__), "sounds/notification_sound_1second.mp3")
SOUND_END = SOUND_START       

def micro_break(sound, duration):
    """A buzzer goes of to indicate the start & stop of micro break"""
    duration = random.uniform(duration, duration * 2) # make the duration of the micro break unpredictable
    playsound(sound)
    time.sleep(duration)
    playsound(sound)

def user_input():
    """Get the duration of the learning session from the user"""
    duration = input("How long would you like to learn for (in minutes)? ")
    try:
        duration = int(duration)
    except ValueError:
        print("Please enter a number")
        duration = user_input()
    try: 
        if (duration < 3) or (duration > 600):
            raise ValueError ("The duration is out of range:")
    except ValueError as error:
        print(error)
        print("- The minimun learning session is 3 minutes and the maximum is 600 minutes (10 hours).")
        print("-- Please enter a value between those (in minutes)")
        print("-- You entered: " + str(duration) + " minute(s)")
        print("- Tip: research shows that ~90 min is the longest period we can expect to maintain intense focus and effort toward learning. - Huberman, 2022")
        duration = user_input()
    return duration

def generate_interval_times(duration, average_interval_size, deviation):
    """Generate a list of interval times in seconds"""
    interval_amount = int((duration * 60) // (average_interval_size * (1 + deviation)))  # calculate the number of intervals to generate
    random_deviations = [random.uniform(-deviation, deviation) for _ in range(interval_amount)]

    intervals = [average_interval_size * (1 + random_deviations[0])]
    for i in range(1, interval_amount):
        intervals.append(intervals[i-1]  + average_interval_size * (1 + random_deviations[i]))
    return intervals


def trigger_at_interval(intervals, duration, trigger_function, trigger_parameter_1, trigger_parameter_2):
    """The buzzer that will go off at the set intervals"""
    time_start = time.time()
    time_end = time_start + (duration * 60)
    i = 0
    while((time.time() < time_end) and (i < len(intervals))):
        if(time.time() - time_start >= intervals[i]):
            print(f"Trigger: {i+1}/{len(intervals)} [Debug log]") # TO DO: comment out, this is for debugging purposes
            time_trigger_start = time.time()
            trigger_function(trigger_parameter_1, trigger_parameter_2) # The function to be triggered at the interval
            time_trigger_finished = time.time()
            i += 1

            if(i < len(intervals)):
                time_sleep = intervals[i] - (time_trigger_finished - time_start)
                try:
                    if time_sleep <= 0:
                        raise AssertionError("Error: intervals are timed too close together or the trigger function is taking too long")
                except AssertionError as error:
                    print(error)
                    print(f"-- Time between this interval and the next is: {intervals[i] - intervals[i-1]} seconds [Debug log]") # TO DO: comment out, this is for debugging purposes
                    print(f"-- The trigger function took: {time_trigger_finished - time_trigger_start} seconds [Debug log]") # TO DO: comment out, this is for debugging purposes
                    return False
                time.sleep(time_sleep)
    return True

def main():
    """The main function"""
    duration = user_input()
    intervals = generate_interval_times(duration/SPEED_UP_FACTOR_FOR_TESTS, AVERAGE_INTERVAL_SIZE/SPEED_UP_FACTOR_FOR_TESTS, DEVIATION)
    print(intervals) #TO DO: remove later, this is for debugging
    
    playsound(SOUND_START)
    session_finished = trigger_at_interval(intervals, duration/SPEED_UP_FACTOR_FOR_TESTS, trigger_function=micro_break, trigger_parameter_1=SOUND_BUZZER, trigger_parameter_2=MICRO_BREAK_DURATION)
    if(session_finished == True):
        print("Good job! You have finished your learning session.")
        playsound(SOUND_END)
    else:
        print("The session was stopped due to an error.")

main()
