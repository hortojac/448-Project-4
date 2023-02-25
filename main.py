from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial
from turtle import delay   
from PIL import ImageTk, Image
import time
import os
import sys
from wordle import Wordle
import tictactoe

def show_frame(frame):
    frame.tkraise()

def run_wordle():
    wordle = Tk()
    wordle.title("Wordle")

    wordle_width = 550 
    wordle_height = 800 

    # get screen width and height to help calculate where to put the wordle window
    screen_width = wordle.winfo_screenwidth() 
    screen_height = wordle.winfo_screenheight() 

    # calculate x and y coordinates for the wordle game
    x = (screen_width/4)  - (wordle_width/2)
    y = (screen_height/2) - (wordle_height/2)

    # set height/width + x/y coords 
    wordle.geometry('%dx%d+%d+%d' % (wordle_width, wordle_height, x, y))

    # set game colors
    wordle.call("source", "Assets/Wordle/SunValley/sun-valley.tcl")
    wordle.call("set_theme", "dark")

    # open window + start game (passing in the screen width/height to help calculate where to put the keyboard window)
    window = Wordle(wordle, screen_width, screen_height)

    # required to make tkinter programs work
    wordle.mainloop()

def runTests():
    tests = ["connect4.py", "rpsls.py", "tictactoe.py", "blackjack.py", "wordle.py"] 
    verdict = "PASSED" # default value
    
    
    print("\nTesting Suite Activated")
    for t in tests: #iterates through every test file and provides info about it

        print("Testing " + t + ":")
        
        start = time.clock_gettime(0)
        if t == "tictactoe.py":
            tictactoe.playGame()
        elif t == "wordle.py":
            run_wordle()
        else:
            os.system("python3 " + t)

        end = time.clock_gettime(0)
        
        runtime = end - start #calculates runtime of program

        if(runtime > 5): #fails if runtime is longer than 5 seconds
            verdict = "FAILED"

        print("program runtime: " + str(runtime) + " seconds")
        print(t  + " runs properly and exits within 5 seconds: " + verdict + "\n\n")
       


root = Tk()
root.state('zoomed') #puts the window mode in zoomed
root.title("Game Suite") #labels our frame
root.rowconfigure(0, weight=1) #configures rows to a weight of 1
root.columnconfigure(0, weight=1) #configures columns to weight of 1


frame1 = Frame(root)

#for frame in (frame1):
frame1.place(relx=0, rely=0, relwidth=1, relheight=1) #frame initialized properly

connect4_button  = Button(frame1, text="Connect 4",font=("Arial",20, BOLD), padx=25, pady=25, command=lambda: os.system('python3 connect4.py')).place(relx=.5,rely=.3,anchor= CENTER) 
rpsls_button = Button(frame1, text="RPSLS",font=("Arial",20, BOLD), padx=25, pady=25, command=lambda: os.system('python3 rpsls.py')).place(relx=.5,rely=.4,anchor= CENTER)
blackjack_button = Button(frame1, text="BlackJack",font=("Arial",20, BOLD), padx=25, pady=25, command=lambda: os.system('python3 blackjack.py')).place(relx=.5,rely=.5,anchor= CENTER)
tictactoe_button = Button(frame1, text="Tic Tac Toe",font=("Arial",20, BOLD), padx=25, pady=25, command=lambda: tictactoe.playGame()).place(relx=.5,rely=.6,anchor= CENTER)
wordle_button = Button(frame1, text="Wordle",font=("Arial",20, BOLD), padx=25, pady=25, command=lambda: run_wordle()).place(relx=.5,rely=.7,anchor= CENTER) 

quit_button = Button(frame1, text="Quit",font=("Arial",30, BOLD), command=partial(root.destroy)) #exits the game, thus goes back to the game suite menu
quit_button.place(relx=.5, rely=.9, anchor=CENTER)


test_button = Button(frame1, text="Test Suite",font=("Arial",20, BOLD), command=partial(runTests)).place(relx=.05,rely=.9,anchor= CENTER) 



show_frame(frame1)



root.mainloop()
