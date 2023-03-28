"""A buzzer that goes of every few minutes to iniate a micro break to enable you to learn faster"""

from utils.input_utils import user_input, validate_learning_duration
from utils.interval_utils import generate_interval_times, trigger_at_interval
from utils.sound_utils import micro_break, playsound
from utils.settings import AVERAGE_INTERVAL_SIZE, DEVIATION, SPEED_UP_FACTOR_FOR_TESTS, SOUND_START, SOUND_BUZZER, SOUND_END

def main():
    """The main function"""
    
    prompt = "How long would you like to learn for (in minutes)? "
    duration = user_input(prompt, validation_function=validate_learning_duration)

    intervals = generate_interval_times(duration/SPEED_UP_FACTOR_FOR_TESTS, AVERAGE_INTERVAL_SIZE/SPEED_UP_FACTOR_FOR_TESTS, DEVIATION)
    print(f"{intervals} [Debug log]") # comment in/out for debugging log

    playsound(SOUND_START)
    session_finished = trigger_at_interval(intervals, duration/SPEED_UP_FACTOR_FOR_TESTS, trigger_function=micro_break, trigger_parameter=SOUND_BUZZER)
    if session_finished:
        print("Good job! You have finished your learning session.")
        playsound(SOUND_END)
    else:
        print("The session was stopped due to an error.")

if __name__ == "__main__":
    main()
