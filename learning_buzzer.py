"""A buzzer that goes of every few minutes to iniate a micro break to enable you to learn faster"""
import os
import time
import numpy as np
from playsound import playsound

DURATION = 10 # The duration of the buzzer in minutes
MIN_INTERVAL_SIZE = 1 # The minimum interval between buzzers in seconds
RECURSION_LOG = 0 # Log to know the amount of recursions for testing purposes

    # TO DO: use this "notification_sound_vivo_2seconds.mp3" sound to start and end program 
def buzzer():
    """The buzzer / sound that will go off every few minutes"""
    sound_file = os.path.join(os.path.dirname(__file__), "sounds/notification_sound_1second.mp3")
    playsound(sound_file)
    print("Buzzing") # TO DO: replace with a buzzer counter or something to show that program is alive incase user's sound is off

def interval_times(duration, min_interval_size, recursion_times):
    """The time intervals that the buzzer will go off"""
    interval_amount = int(duration / 2) # An average of one interval per two minutes
    intervals = np.random.uniform(0, duration, interval_amount)
    intervals = np.sort(intervals)
    if np.all(np.diff(intervals) >= min_interval_size):
        print(f"Recursions: {recursion_times}") # TO DO: remove this line later, when done with testing
        return intervals
    else:
        return interval_times(duration, min_interval_size, recursion_times+1)

def main():
    print(interval_times(DURATION, MIN_INTERVAL_SIZE, RECURSION_LOG))
    buzzer()

main()
