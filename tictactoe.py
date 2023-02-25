from cgitb import text
#from distutils import command
from email import message
from functools import partial
from glob import glob
from itertools import count
from pickle import GLOBAL
from tkinter import *
import tkinter as tk
from tkinter import messagebox



count = 0 ## Keeps tracks of user click
player = ' ' ##Player 1 or 2 string
p1Score = list() #list of magic numbers that player 1 click
p2Score = list() #list of magic numbers that player 2 click


def playGame(): ##Game fuction
    gameWindow = Toplevel() ## this creates a new window rather than changing frames
    gameWindow.title("Tic-Tac-Toe") ##Titles the window to Tic Tac Toe
    gameWindow.geometry("370x350") ## Game window size 

    global count ## count needs to be called ever everytime change is about to be made, python thing
    count=0 ##initialization


    ##BUTTON_CLICK will deal with user interaction
    def button_click(passedButton):   ## when button is clicked, that button will be passed in here
        global count, player ##calling to modify
        count = count+1 #increases the count by 1 everytime, a button is passed
        ##print(count)
    
        if(count%2==0): ##Player 2 #when count is modded by 2 that will be counted as player 2's click
            player = "Player 2" ##player 2 initialization
            p2Score.append(buttonValues.get(passedButton)) ##adding the values from button dictionary corresponding to the button clicked
            #print("player2: ",p2Score)
            win = checkWin(p2Score) #this calls the checkWin function to see if their click makes made a win and saves it to variable win
            if(win == 1): ##checkWin returns 1 or 0, if 1 is returned it will go inside the if statement (Check win comment for it's description)
                ##Anounces that player 2 is the winner and asks if they want to play again or not and saves the response
                response = messagebox.askquestion(player, player + " Won. \n Play Again?") 
                if(response == "yes"): ##if the response is yes
                    gameExit() ##it will close the current game window 
                    playGame() ## and open a new game window 
                elif(response == "no"): ##if the response is no
                    gameExit() ##it will close the current game window 
            else:
                ##if win returns anything else, it will modify the button to show a red X and disable the button so that it can't be clicked again
                passedButton.config(text = "X", fg='red', state = "disable", disabledforeground='red')
            
        else: #Player 1 ##Player 2 #when count modded by 2 is not 0, that will be counted as player 1's click
            player = "Player 1" ##player 1 initialization
            p1Score.append(buttonValues.get(passedButton)) ##adding the values from button dictionary corresponding to the button clicked
            #print("player1: ",p1Score)
            win = checkWin(p1Score) ##checkWin returns 1 or 0, if 1 is returned it will go inside the if statement (Check win comment for it's description)
            ##this checks for a tie, We know there's only 9 clicks and each player can either have 4 or 5 clicks, and that checkWin returns either a 0 or a 1 
            ##so put all that and you get the if statement below len(p1Score) is the length of p1score so basically p1's # of clicks
            if(count == 9 and len(p1Score) == 5 and win !=1): ##if it's a tie
                win = 2 ##set win to 2
            if(win == 1 or win == 2): ##either way (tie or p1 win) we need to go inside this if statement to get user input
                if(win == 1): ## if it's a win, it will show that p1 won and ask if they'd like to play again
                    response = messagebox.askquestion(player, player + " Won. \n Play Again?") ## records response to if they want to play again
                else:
                    response = messagebox.askquestion(player, "Game Tied. Play Again?") ##if it's a tie, outputs it's a tie and asks if they want to play another game
                if(response == "yes"): ##if their response is yes
                    gameExit()  ##it will close the current game window 
                    playGame() ## and open a new game window 
                elif(response == "no"):
                    gameExit() ##it will close the current game window 
            else:
                ##if win returns anything else, it will modify the button to show a red X and disable the button so that it can't be clicked again
                passedButton.config(text = "O", fg='blue', state = "disable", disabledforeground='blue')

    ##Buttons

    
    #All these buttons follow the same format, they have text initialized to " " so that it can be replaced with X or O when clicked by the button_click function
    #fg= is the background color (gray)
    #padx pady == size of the buttons
    #state normal means they can click, disable-cannot click
    #command passes the button to button click for modication and recording player's click

    button_1 = Button(gameWindow, text=" ", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_1))
    button_1.grid(row=3, column=0)
    button_2 = Button(gameWindow, text=" ", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_2))
    button_2.grid(row=3, column=1)
    button_3 = Button(gameWindow, text=" ", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_3))
    button_3.grid(row=3, column=2)
    button_4 = Button(gameWindow, text=" ", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_4))
    button_4.grid(row=2, column=0)
    button_5 = Button(gameWindow, text=" ", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_5))
    button_5.grid(row=2, column=1)
    button_6 = Button(gameWindow, text=" ", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_6))
    button_6.grid(row=2, column=2)
    button_7 = Button(gameWindow, text=" ", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_7))
    button_7.grid(row=1, column=0)
    button_8 = Button(gameWindow, text=" ", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_8))
    button_8.grid(row=1, column=1)
    button_9 = Button(gameWindow, text=" ", padx=40,pady=20, fg='#f0f0f0', state = "normal", command=lambda: button_click(button_9))
    button_9.grid(row=1, column=2)

    #exit button to close the window anytime, it will call the gameExit function to clear all player's data
    button_close = Button(gameWindow, text="Exit Game", command= lambda: gameExit())
    button_close.grid(row=4, column=2)

    ##Game information: p1 is O and p2 is X
    gameInfo = Label(gameWindow, text="Game by Group 11 \n Player 1: 'O' \nPlayer 2: X")
    gameInfo.grid(row=5, column= 0)

    ##to end the game, when gameExit is called 
    def gameExit():
        p1Score.clear() #It will clear p1's data
        p2Score.clear() #then p2's data
        gameWindow.destroy() #close the window

    
    ##Button - Value Dictionary
    ##these are the magic numbers for the game, each button corresponds to a certain value
    ##that can be accessed anywhere in the program
    buttonValues = {button_1:4, button_2:3, button_3:8,
                    button_4:9, button_5:5, button_6:1,
                    button_7:2, button_8:7, button_9:6                   
                    }

    #check if there's the magic number 15 in player's data list
    def checkWin(scores): ##scores is player's score list passed from button_click function
        place = len(scores) ##gets the length's of p1's data
        if(place<3): ##we know there cannot be any winner if there is less than 3 clicks so we return 0 for it
            return 0
        else:
            ##after 3 clicks we need to check to make sure we have a tie or a winner
            for i in range(place): ## use for i to look through player's data [i1, i2, i3, i4, i5]
                for j in range(place): ## then use j to look through the same data 
                    for k in range(place):## and then use k to look through the same data
                            total = scores[i] + scores[j] + scores[k] ## add the each index each loop is looking at to see if it's the magic number 15

                            ##If it's 15, it's good but we need to make sure that i,j, and k are looking at different indices to get 15 and not the same one
                            ##hence all the and conditions
                            if(total == 15 and (scores[i] != scores[j]) and (scores[j] != scores[k]) and (scores[i] != scores[k])):
                                return 1 ##if it matches all the conditions, it will return 1 otherwise, nothing
