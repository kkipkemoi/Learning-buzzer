"""A buzzer that goes of every few minutes to iniate a micro break to enable you to learn faster"""
import os
import time
import random
import numpy as np
from playsound import playsound

MIN_INTERVAL_SIZE = 20 # The minimum interval between buzzers in seconds (the micro break)
SOUND_START = os.path.join(os.path.dirname(__file__), "sounds/aurora_trimmed_4seconds.mp3")
SOUND_BUZZER = os.path.join(os.path.dirname(__file__), "sounds/notification_sound_1second.mp3")
SOUND_END = os.path.join(os.path.dirname(__file__), "sounds/aurora_trimmed_15seconds.mp3")

def user_input():
    """Get the duration of the learning session from the user"""
    duration = input("How long would you like to learn for? (in minutes) ")
    try:
        duration = int(duration)
    except ValueError:
        print("Please enter a number")
        duration = user_input()
    if (duration < 3) or (duration > 180):
        print("- The minimun learning session is 3 minutes and the maximum is 180 minutes (3 hours).")
        print("- Please enter a value between those.")
        print("- You entered: " + str(duration) + " minute(s)\n")
        print("- Tip: research shows that ~90 min is the longest period we can expect to maintain intense focus and effort toward learning. - Huberman, 2022")
        duration = user_input()
    return duration

def generate_interval_times(duration, min_interval_size):
    """Generate a list of interval times in seconds"""
    interval_amount = int(duration / 3)  # calculate the number of intervals to generate
    interval_amount += random.randint(int(-0.2*interval_amount), int(0.2*interval_amount)) # add a random amount of intervals to the base amount
    min_interval_time = 120   
    max_interval_time = 180  
    intervals = []
    
    for i in range(interval_amount): #TO DO: make sure that the intervals don't exceed the duration
        interval_time = random.uniform(min_interval_time, max_interval_time)
        intervals.append(interval_time)
        min_interval_time = interval_time + min_interval_size
        max_interval_time = min_interval_time + random.uniform(min_interval_time, max_interval_time)
    
    return intervals  # convert intervals to seconds and return as list

def interval_buzzer(intervals, duration):
    """The buzzer that will go off at the set intervals"""
    time_start = time.time()
    time_end = time_start + (duration * 60)
    i = 0
    while((time.time() < time_end) and (i < len(intervals))):
        if((time.time() - time_start <= intervals[i] + 1) and (time.time() - time_start >= intervals[i])):
            print(f"{int((time.time() - time_start/60))} minutes have passed in total") #TO DO: consider adding like a proper timer
            playsound(SOUND_BUZZER)
            print(f"Buzzer: {i+1}/{len(intervals)}") #TO DO: remove later, this is for debugging
            i += 1

def main():
    """The main function"""
    duration = user_input()
    intervals = generate_interval_times(duration, MIN_INTERVAL_SIZE)
    print(intervals)
    playsound(SOUND_START)
    interval_buzzer(intervals, duration)
    playsound(SOUND_END)

main()
