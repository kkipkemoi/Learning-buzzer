# Learning-buzzer
A program that buzzes randomly every few minutes to tell you to take a micro-rest so that you can learn faster.

- Supposedly you learn faster if you do nothing for about 10-20 seconds every ~2 minutes at random while learning
    - Source: [Huberman Lab, #5](https://hubermanlab.com/teach-and-learn-better-with-a-neuroplasticity-super-protocol/)
 
# How to use the learning buzzer
1. Run the program (learning_buzzer.py).
2. Choose for how long you would like to study for (in minutes).
- Tip: research shows that ~90 min is the longest period we can expect to maintain intense focus and effort toward learning 
    - Source: [Huberman Lab, #7](https://hubermanlab.com/teach-and-learn-better-with-a-neuroplasticity-super-protocol/)
3. The program makes a sound (4 seconds long) to indicate the session has started. 
4. At random intervals, you will hear a short buzzer at both the start and end of the micro-rest.
- During the micro-rest, you should stop whatever you are doing and think of nothing. 
- Closing your eyes can help.
5. When the study session has ended, the same sound as the starting sound will be produced, and the program will stop.

# Settings
You can adjust the average interval times, micro-rest times and which sounds to play in the [settings file](https://github.com/kkipkemoi/Learning-buzzer/blob/main/utils/settings.py).

Default settings:
- Buzzer goes off randomly, but on average, the interval is around ~2 minutes. 
- Micro-rests have a random duration between 10 and 20 seconds
