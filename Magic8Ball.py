# Title: Magic 8 Ball
# Author: Twazanga Mugala
# Purpose: Simulate a magic 8-ball

# Requirements: Take in user input, display in progress message, allow user to keep asking questions or quit.

import time
import random

answers = ["Definitely", "I'm not sure try again in 5 seconds", "No", "I don't know, I'm not psychic",
           "Yes", "It's not a good idea", "Maybe", "Possibly", "Ask your mom? She probably knows better than me",
           "Take a walk and think about it first",
           "Meditate on it then try again", "You should probably take a nap first", "You're not ready yet young padowan",
           "What would Samuel L. Jackson say", "Idk google it", "Idk bing it", "Ask Bill Gates", "My mind is blurry",
           "I'm not sure", "Maybe tomorrow", "Definitely next week"]

phrases = ["Hold on, I'm thinking...", "Thinking...", "Discussing with the ancestors...", "Umm...",
           "Calling Alex Trebek...", "Looking that up..."]


def eight_ball(n):
    if n.lower() == "x":
        exit()
    p_num = random.randint(0, 5)
    print(phrases[p_num])
    time.sleep(4)
    a_num = random.randint(0, 19)
    answer = answers[a_num]
    return answer


if __name__ == '__main__':
    asking = True
    while asking:
        print(eight_ball(input("Ask the Magic 8 Ball the question on your mind or enter X to exit: ")))
