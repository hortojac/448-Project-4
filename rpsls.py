from ctypes import alignment
from curses import textpad
from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial   
from PIL import ImageTk, Image
import random

root = Tk()
root.state('zoomed') #puts the window mode in zoomed
root.title("Rock Paper Scissors Lizard Spock") #labels our frame

root.rowconfigure(0, weight=1) #configures rows to a weight of 1
root.columnconfigure(0, weight=1) #configures columns to weight of 1

### GLOBAL VARIABLES
choice_player = ""
choice_ai = ""  
score_player = 0
score_ai = 0
font_size = 30
###

### Initialize Images

image=Image.open("assets/rpsls/start.jpeg") 
#img=image.resize((160,160))
img_start=ImageTk.PhotoImage(image) #image for just the start button

image=Image.open("assets/rpsls/rock.jpeg") 
img=image.resize((160,160))
img_rock=ImageTk.PhotoImage(img) #image for just the start button

image=Image.open("assets/rpsls/paper.jpeg") 
img=image.resize((160,160))
img_paper=ImageTk.PhotoImage(img) #image for just the start button

image=Image.open("assets/rpsls/scissors.jpeg") 
img=image.resize((160,160))
img_scissors=ImageTk.PhotoImage(img) #image for just the start button

image=Image.open("assets/rpsls/lizard.jpeg") 
img=image.resize((160,160))
img_lizard=ImageTk.PhotoImage(img) #image for just the start button

image=Image.open("assets/rpsls/spock.jpeg") 
img=image.resize((160,160))
img_spock=ImageTk.PhotoImage(img) #image for just the start button

image=Image.open("assets/rpsls/rules.jpeg") 
img=image.resize((460,460))
img_rules=ImageTk.PhotoImage(img) #image for just the start button

###

def show_frame(frame):
    frame.tkraise()
    
def show_rules(prevFrame): #displays the rules page for RPSLS

    #image of rules
    rules_img = Button(frame_rules, image=img_rules, compound=CENTER, state=DISABLED)
    rules_img.place(relx=.5, rely=.3, anchor=CENTER)

    #Label of Rules
    txt = "- scissors cuts paper. \n- Paper covers rock. \n- Rock crushes lizard. \n- Lizard poisons Spock. \n- Spock smashes scissors. \n- Scissors decapitates lizard. \n- Lizard eats paper. \n- Paper disproves Spock. \n- Spock vaporizes rock. \n- And as it always has, rock crushes scissors."
    rules_txt = Label(frame_rules, width=70, text=txt, font=("Arial",15),justify=LEFT)

    rules_txt.place(relx=.45, rely=.65, anchor=CENTER)

    #rule frame back button
    rules_replayBtn = Button(frame_rules, text="Back",font=("Arial",30, BOLD), command=partial(show_frame,prevFrame)) #replays the game for the player
    rules_replayBtn.place(relx=.5, rely=.8, anchor=CENTER)

    #rule frame quit button
    rules_exitBtn = Button(frame_rules, text="Quit",font=("Arial",30, BOLD), command=partial(root.destroy)) #exits the game, thus goes back to the game suite menu
    rules_exitBtn.place(relx=.5, rely=.9, anchor=CENTER)

    #goes back to the previous frame
    show_frame(frame_rules)

def getResult(): #RETURNS W, L, or T, for Win, Lose, or Tie
    #checks win conditions for game
    global choice_ai
    global choice_player

    if choice_player == choice_ai:
        return 'T'
    elif choice_player == "Rock":
        if choice_ai == "Lizard" or choice_ai == "scissors":
            return 'W'
        else:
            return 'L'
    elif choice_player == "Paper":
        if choice_ai == "Rock" or choice_ai == "Spock":
            return 'W'
        else:
            return 'L'
    elif choice_player == "Scissors":
        if choice_ai == "Paper" or choice_ai == "Lizard":
            return 'W'
        else:
            return 'L'
    elif choice_player == "Lizard":
        if choice_ai == "Paper" or choice_ai == "Spock":
            return 'W'
        else:
            return 'L'
    elif choice_player == "Spock":
        if choice_ai == "Rock" or choice_ai == "Scissors":
            return 'W'
        else:
            return 'L'

def setup_frame3(choice): #sets up the necessary widgets and data for frame 3
    global choice_player
    global choice_ai

    #set player choice
    choice_player = choice

    #set AI choice (random)
    
    choices = ["Rock","Paper","Scissors","Lizard","Spock"]

    choice_ai = random.choice(choices)
    ##DEBUG

    frame3_txt1.configure(text="You picked...\n" + choice_player)

    #setup image of player choice
    frame3_playerBtn = Button(frame3, compound=CENTER, state=DISABLED)

    if choice_player == "Rock":
        frame3_playerBtn.configure(image=img_rock)
    elif choice_player  == "Paper":
         frame3_playerBtn.configure(image=img_paper)
    elif choice_player == "Scissors":
         frame3_playerBtn.configure(image=img_scissors)
    elif choice_player == "Lizard":
         frame3_playerBtn.configure(image=img_lizard)
    elif choice_player== "Spock":
         frame3_playerBtn.configure(image=img_spock)
    
    frame3_playerBtn.place(relx=.5, rely=.18, anchor=CENTER)
    #

    frame3_txt2.configure(text="Enemy picked ...\n" + choice_ai)
    
    #setup image of player choice
    frame3_aiBtn = Button(frame3, padx=10, pady=10, compound=CENTER, state=DISABLED) #player chooses rock

    if choice_ai == "Rock":
        frame3_aiBtn.configure(image=img_rock)
    elif choice_ai  == "Paper":
         frame3_aiBtn.configure(image=img_paper)
    elif choice_ai == "Scissors":
         frame3_aiBtn.configure(image=img_scissors)
    elif choice_ai == "Lizard":
         frame3_aiBtn.configure(image=img_lizard)
    elif choice_ai == "Spock":
         frame3_aiBtn.configure(image=img_spock)

    frame3_aiBtn.place(relx=.5, rely=.48, anchor=CENTER)
    #

    result = getResult() # will either be 'W', 'L', or 'W'
    new_text = ""
    if result == 'W':
        global score_player
        score_player = score_player + 1
        new_text = "You Win!"
    elif result == 'L':
        global score_ai
        score_ai = score_ai + 1
        new_text = "You Lose!"
    else:
         new_text = "Tie! Nobody Wins"
        

    frame3_txt3.configure(text=new_text)

    show_frame(frame3)# now skip to frame 3

def play(): #jumps to player's turn while updating scoreboard
    global score_player
    global score_ai

    #scoreboard code
    frame2_score = Label(frame2, text="Score",font=Font(family="Arial", size=30, weight=BOLD, underline=1))
    frame2_score.place(relx=.9, rely=.05, anchor=CENTER)

    frame2_scorePlayer = Label(frame2, text="You: " + str(score_player),font=("Arial", 25, BOLD))
    frame2_scorePlayer.place(relx=.9, rely=.1, anchor=CENTER)

    frame2_scoreAI = Label(frame2, text="Enemy: " + str(score_ai),font=("Arial", 25, BOLD))
    frame2_scoreAI.place(relx=.9, rely=.15, anchor=CENTER)
    #
    show_frame(frame2)


frame1 = Frame(root) #welcome menu frame
frame2 = Frame(root) # player pick screen
frame3 = Frame(root) # result screen
frame_rules = Frame(root) # rules screen

for frame in (frame1, frame2, frame3, frame_rules):
    frame.place(relx=0, rely=0, relwidth=1, relheight=1) #frames initialized properly


show_frame(frame1)

##frame_rules code

##frame1 code
frame1_welcomeTxt = Label(frame1, text="Rock Paper Scissors Lizard Spock!\nPress start to begin playing.",font=("Arial", 25)) #welcome text 
frame1_welcomeTxt.place(relx=.5, rely=.1,anchor= CENTER)


frame1_startBtn = Button(frame1, text="Start",fg="white", font=("Arial",50, BOLD), command=partial(play), bg="white", padx=20,pady=20, image=img_start, compound=CENTER) #Big button to start the game
frame1_startBtn.place(relx=.5, rely=.5, anchor=CENTER)

#frame1 quit button
frame1_exitBtn = Button(frame1, text="Quit",font=("Arial",30, BOLD), command=partial(root.destroy)) #exits the program
frame1_exitBtn.place(relx=.5, rely=.9, anchor=CENTER)
##

##frame2 code
frame2_txt = Label(frame2, text="What will you throw?",font=("Arial", 40))
frame2_txt.place(relx=.5, rely=.1, anchor=CENTER)

#frame2 button for rock
frame2_rockBtn = Button(frame2, text="ROCK",font=("Arial",font_size, BOLD), image=img_rock, compound=CENTER, command=partial(setup_frame3, "Rock")) #player chooses rock
frame2_rockBtn.place(relx=.3, rely=.3, anchor=CENTER)

#frame2 button for paper
frame2_paperBtn = Button(frame2, text="PAPER",font=("Arial",font_size, BOLD), image=img_paper, compound=CENTER, command=partial(setup_frame3, "Paper")) #player chooses paper
frame2_paperBtn.place(relx=.5, rely=.3, anchor=CENTER)

#frame2 button for scissors
frame2_scissorsBtn = Button(frame2, text="SCISSORS",font=("Arial",font_size, BOLD), image=img_scissors, compound=CENTER, command=partial(setup_frame3, "Scissors")) #player chooses scissors
frame2_scissorsBtn.place(relx=.7, rely=.3, anchor=CENTER)

#frame2 button for lizard
frame2_lizardBtn = Button(frame2, text="LIZARD",font=("Arial",font_size, BOLD), image=img_lizard, compound=CENTER, command=partial(setup_frame3, "Lizard")) #player chooses lizard
frame2_lizardBtn.place(relx=.4, rely=.55, anchor=CENTER)

#frame2 button for spcok
frame2_spockBtn = Button(frame2, text="SPOCK",font=("Arial",font_size, BOLD), image=img_spock, compound=CENTER, command=partial(setup_frame3, "Spock")) #player chooses spock
frame2_spockBtn.place(relx=.6, rely=.55, anchor=CENTER)

#frame2 rules button
frame2_rulesBtn = Button(frame2, text="Rules",font=("Arial",30, BOLD), command=partial(show_rules, frame2)) #exits the game, thus goes back to the game suite menu
frame2_rulesBtn.place(relx=.1, rely=.9, anchor=CENTER)
##

#frame2 quit button
frame2_exitBtn = Button(frame2, text="Quit",font=("Arial",font_size, BOLD), command=partial(root.destroy)) #exits the program
frame2_exitBtn.place(relx=.5, rely=.9, anchor=CENTER)
##

##frame3 code

#scoreboard labels code
frame3_txt1 = Label(frame3, text="", font=("Arial", 25))
frame3_txt1.place(relx=.5, rely=.05,anchor= CENTER)

frame3_txt2 = Label(frame3, text="", font=("Arial", 25))
frame3_txt2.place(relx=.5, rely=.35,anchor= CENTER)

frame3_txt3 = Label(frame3, text="",font=("Arial", 40))
frame3_txt3.place(relx=.5, rely=.65,anchor= CENTER)
#

#frame3 play again button
frame2_replayBtn = Button(frame3, text="Play Again",font=("Arial",30, BOLD), command=partial(play)) #replays the game for the player
frame2_replayBtn.place(relx=.5, rely=.8, anchor=CENTER)

#frame3 quit button
frame2_exitBtn = Button(frame3, text="Quit",font=("Arial",30, BOLD), command=partial(root.destroy)) #exits the game, thus goes back to the game suite menu
frame2_exitBtn.place(relx=.5, rely=.9, anchor=CENTER)

#frame3 rules button
frame_rulesBtn = Button(frame3, text="Rules",font=("Arial",30, BOLD), command=partial(show_rules, frame3)) #exits the game, thus goes back to the game suite menu
frame_rulesBtn.place(relx=.1, rely=.9, anchor=CENTER)
##



root.mainloop() #keeps game running, part of basic Tkinter game structure
