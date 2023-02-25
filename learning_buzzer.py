"""A buzzer that goes of every few minutes to iniate a micro break to enable you to learn faster"""
import os
import time
import random
import numpy as np
from playsound import playsound

DURATION = 10 # The duration of the buzzer in minutes
MIN_INTERVAL_SIZE = 10 # The minimum interval between buzzers in seconds
RECURSION_LOG = 0 # Log to know the amount of recursions for testing purposes
SOUND_FILE = os.path.join(os.path.dirname(__file__), "sounds/notification_sound_1second.mp3")

# TO DO: use this "notification_sound_vivo_2seconds.mp3" sound to start and end program 
def buzzer():
    """The buzzer / sound that will go off every few minutes"""
    playsound(SOUND_FILE)
    print("Buzzing") # TO DO: replace with a buzzer counter or something to show that program is alive incase user's sound is off

def generate_interval_times(duration, z):
    """Generate a list of interval times in seconds"""
    interval_amount = int(duration / 3)  # calculate the number of intervals to generate
    interval_amount += random.randint(int(-0.2*interval_amount), int(0.2*interval_amount)) # add a random amount of intervals to the base amount
    min_interval_time = 120   
    max_interval_time = 180  
    intervals = []
    
    for i in range(interval_amount):
        interval_time = random.uniform(min_interval_time, max_interval_time)
        intervals.append(interval_time)
        min_interval_time = interval_time + z
        max_interval_time = min_interval_time + random.uniform(min_interval_time, max_interval_time)
    
    return intervals  # convert intervals to seconds and return as list

def interval_buzzer(intervals):
    """The buzzer that will go off at the intervals"""
    time_start = time.time()
    time_end = time_start + (DURATION * 60)
    i = 0
    while((time.time() < time_end) and (i < len(intervals))):
        if((time.time() - time_start <= intervals[i] + 1) and (time.time() - time_start >= intervals[i])):
            print(f"The time is: {time.time() - time_start}")
            temp_time_start = time.time()
            buzzer()
            temp_time_end = time.time()
            print(f"Time taken to buzz: {temp_time_end - temp_time_start}")
            i += 1

def main():
    intervals = generate_interval_times(DURATION, MIN_INTERVAL_SIZE)
    print(intervals)
    interval_buzzer(intervals)

main()
