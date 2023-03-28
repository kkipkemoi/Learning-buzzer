"""Functions to generate interval times and trigger a function at a set of intervals"""

import random
import time

def generate_interval_times(duration, average_interval_size, deviation):
    """Generate a list of interval times in seconds"""
    interval_amount = int((duration * 60) // (average_interval_size * (1 + deviation)))
    random_deviations = [random.uniform(-deviation, deviation) for _ in range(interval_amount)]

    intervals = [average_interval_size * (1 + random_deviations[0])]
    for i in range(1, interval_amount):
        intervals.append(intervals[i-1]  + average_interval_size * (1 + random_deviations[i]))
    return intervals

def trigger_at_interval(intervals, duration, trigger_function, trigger_parameter):
    """The buzzer that will go off at the set intervals"""
    time_start = time.time()
    time_end = time_start + (duration * 60)
    i = 0
    while((time.time() < time_end) and (i < len(intervals))):
        if(time.time() - time_start >= intervals[i]):
            print(f"Trigger: {i+1}/{len(intervals)} [Debug log]") # comment in/out for debugging log
            time_trigger_start = time.time()
            trigger_function(trigger_parameter) # the function to be triggered at the interval
            time_trigger_finished = time.time()
            i += 1

            if(i < len(intervals)):
                time_sleep = intervals[i] - (time_trigger_finished - time_start)
                try:
                    if time_sleep <= 0:
                        raise AssertionError("Error: intervals are timed too close together or the trigger function is taking too long")
                except AssertionError as error:
                    print(error)
                    print(f"-- Time between this interval and the next is: {intervals[i] - intervals[i-1]} seconds [Debug log]") # comment in/out for debugging log
                    print(f"-- The trigger function took: {time_trigger_finished - time_trigger_start} seconds [Debug log]") # comment in/out for debugging log
                    return False
                time.sleep(time_sleep)
    return True
    