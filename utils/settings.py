""" Settings for the learning buzzer"""

import os

#The settings for the learning buzzer
MICRO_BREAK_DURATION_MIN = 10 # in seconds
MICRO_BREAK_DURATION_MAX = 20 # in seconds
AVERAGE_INTERVAL_SIZE = 300 # the average interval between buzzers in seconds
DEVIATION = 0.2 # introduce randomness to the intervals of when the buzzer goes off
SPEED_UP_FACTOR_FOR_TESTS = 1 # shorten the duration and intervals for testing purposes


def get_sound_path(sound_filename):
    """Get the path to the sound file"""
    return os.path.join(os.path.dirname(__file__), '..', 'sounds', sound_filename)

#Different sounds that can be used can be found in the sounds folder
SOUND_START = get_sound_path("aurora_trimmed_4seconds.mp3")
SOUND_BUZZER = get_sound_path("notification_sound_1second.mp3")
SOUND_END = SOUND_START # change it to a different sound if desired
