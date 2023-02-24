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
"""
def generate_interval_times(x, y, z):
    intervals = []
    min_time = 0
    y = y * 60 # Convert minutes to seconds

    for i in range(x):
        max_time = y - (x - i - 1) * z
        if min_time >= max_time:
            break
        interval_time = random.uniform(min_time, max_time)
        intervals.append(interval_time)
        min_time = interval_time + z
    return intervals
"""

def generate_interval_times(y, z):
    """
    Returns a list of x interval times (in seconds) between 0 and y minutes, with a minimum distance of z seconds between each interval time.
    """
    interval_amount = int(y / 2)  # calculate the number of intervals to generate
    #interval_amount += random.randint(-0.2*interval_amount, 0.2*interval_amount) # add a random amount of intervals to the base amount
    min_interval_time = 120   
    max_interval_time = 180  
    intervals = []
    
    for i in range(interval_amount):
        interval_time = random.uniform(min_interval_time, max_interval_time)
        intervals.append(interval_time)
        min_interval_time = interval_time + z
        max_interval_time = min_interval_time + random.uniform(min_interval_time, max_interval_time)
    
    return [t * 60 for t in intervals]  # convert intervals to seconds and return as list

"""
def generate_interval_times(duration, z):
    intervals = []
    x = int(duration/2) # The amount of intervals
    #x = 10 # The amount of intervals
    min_time = 0

    for i in range(x):
        max_time = duration - (x - i - 1) * z
        if min_time >= max_time:
            break
        interval_time = random.uniform(min_time, max_time)
        intervals.append(interval_time)
        min_time = interval_time + z
    return intervals
"""

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

def interval_buzzer(intervals):
    """The buzzer that will go off at the intervals"""
    interval_iter = iter(intervals)
    for interval in interval_iter:
        pass
        #print(f"interval: {interval} seconds")
        #next_interval = next(interval_iter)
        #print(f"next interval: {next_interval} seconds")
        #time.sleep(next_interval-interval)
        #start_time = time.time()
        #buzzer()
        #end_time = time.time()
        #print(f"Time taken: {end_time-start_time} seconds")

def main():
    intervals = generate_interval_times(DURATION, MIN_INTERVAL_SIZE)
    #intervals = interval_times(DURATION, MIN_INTERVAL_SIZE, RECURSION_LOG)
    #buzzer()
    print(intervals)
   # interval_buzzer(intervals)

main()
