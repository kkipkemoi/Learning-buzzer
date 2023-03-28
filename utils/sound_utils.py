"""This module contains the functions that play the sound files for the learning buzzer"""

import time
import random
from playsound import playsound # version 1.2.2 of this module had to be installed, version 1.3.0 does not work (consistantly)
from utils.settings import MICRO_BREAK_DURATION_MIN, MICRO_BREAK_DURATION_MAX

def micro_break(sound):
    """A buzzer goes of to indicate the start & stop of micro break"""
    duration = random.uniform(MICRO_BREAK_DURATION_MIN, MICRO_BREAK_DURATION_MAX ) # micro break duration should be unpredictable
    playsound(sound)
    time.sleep(duration)
    playsound(sound)
