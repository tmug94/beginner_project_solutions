# Title: Magic 8 Ball
# Author: Twazanga Mugala
# Purpose: Simulate a magic 8-ball

# Requirements: Take in user input, display in progress message, allow user to keep asking questions or quit.

import time
import random
from tkinter import *

# List of answers
answers = ["Definitely", "I'm not sure try again in 5 seconds", "No", "I don't know, I'm not psychic",
           "Yes", "It's not a good idea", "Maybe", "Possibly", "Ask your mom? She probably knows better than me",
           "Take a walk and think about it first",
           "Meditate on it then try again", "You should probably take a nap first", "You're not ready yet young padowan",
           "What would Samuel L. Jackson say", "Idk google it", "Idk bing it", "Ask Bill Gates", "My mind is blurry",
           "I'm not sure", "Maybe tomorrow", "Definitely next week"]

# In progress outputs
phrases = ["Hold on, I'm thinking...", "Thinking...", "Discussing with the ancestors...", "Umm...",
           "Calling Alex Trebek...", "Looking that up..."]

p_num = random.randint(0, 5)
#a_num = random.randint(0, 19)


# Function that picks random phrase and answer
def eight_ball(n):
    if n.lower() == "x":
        exit()
    print(phrases[p_num])
    time.sleep(4)
    answer = answers[a_num]
    return answer


# Clear entrybox

def clear():
    entrybox.delete(0, END)

#Retrieve answer from entry box
def click():
    question = entrybox.get()
    if question.lower() == "":
        output.delete(0.0, END)
        output.insert(END, "Are you going to ask an actually question, or just waste my time?")
    else:
        a_num = random.randint(0, 19)
        output.delete(0.0, END)
        output.insert(END, answers[a_num])


# Set up to play again
def repeat():
    clear()
    output.delete(0.0, END)
    output.insert(END, "More questions? Well I have more answers.")

# Quit window
def close():
    window.destroy()


if __name__ == '__main__':



    window = Tk()
    window.configure(bg="black")
    window.title("Magic 8 Ball")
    Label(window, text="Ask the Magic 8 Ball the question on your mind or enter X to exit: ", bg="black", fg="white")\
        .grid(row=0, column=0)

    # Create entry box to type question
    entrybox = Entry(window, width=30, bg="white")
    entrybox.grid(row=1, column=0)

    # Create output box at below buttons
    output = Text(window, bg="white", fg="black", width=40, height=5)
    output.grid(row=4, column=0)
    #output.pack()

    # Create 4 button: Ask, Clear, Play Again, Quit
    button_frame = Frame(window)
    button_frame.configure(bg="black")
    button_frame.grid(row=2, column=0)
    #button_frame.pack(fill=X, side=BOTTOM)
    Button(button_frame, text="Ask", width=10, bg="black", fg="white", command=click).grid(row=2, column=0)
    Button(button_frame, text="Clear", width=10, command=clear).grid(row=2, column=1)
    Button(button_frame, text="Play Again", width=10,command=repeat).grid(row=3, column=0)
    Button(button_frame, text="Quit", width=10, command=close).grid(row=3, column=1)



    # w = Label(root, text="Hello World")
    # w.pack()

    window.mainloop()
    #asking = True
   # while asking:
        #print(eight_ball(input("Ask the Magic 8 Ball the question on your mind or enter X to exit: ")))
