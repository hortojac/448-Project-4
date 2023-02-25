# import tkinter module
from array import array
from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial     
from itertools import product
from PIL import ImageTk, Image
 

root = Tk() # Create Object
root.title("Connect 4") # main title of game
root.state('zoomed') # take up all of the screen

def show_frame(frame): #raises a frame when called
    frame.tkraise()

frame1 = Frame(root) #create frame 1
frame2 = Frame(root) #create frame 2
for frame in (frame1, frame2): #loop from frame 1 to frame 2
    frame.grid(row=0, column=0, sticky = 'nsew') #frame 1 and 2 rows and columns initiliazed to 0 and widgets are sticky



image = Image.open('Assets/Connect4/red_token.png')# call red image and store it in a variable
image_2 = Image.open('Assets/Connect4/blue_token.png')#call blue image and store it in a variable
photo = ImageTk.PhotoImage(image.resize((50, 50), Image.ANTIALIAS))#resize red image
photo_2 = ImageTk.PhotoImage(image_2.resize((43, 43), Image.ANTIALIAS))#resize blue image



show_frame(frame1)#initially show frame 1

#each column of connect 4 can only fit 6 tokens. Keep track of how many tokens are currently in each column by initializing them all to 5 and subtracting 1 everytime a token is placed.
count_column1 = 5
count_column2 = 5
count_column3 = 5
count_column4 = 5
count_column5 = 5
count_column6 = 5
count_column7 = 5

main_count = 0 #count how many times a token is placed to determine what players turn it is and/or if the game ends an a stalemate

def disable():#When disable function is called all buttons become disabled because the game is over.
    #call all global variables
    global btn_column1
    global btn_column2
    global btn_column3
    global btn_column4
    global btn_column5
    global btn_column6
    global btn_column7
    btn_column1.configure(state=DISABLED)
    btn_column2.configure(state=DISABLED)
    btn_column3.configure(state=DISABLED)
    btn_column4.configure(state=DISABLED)
    btn_column5.configure(state=DISABLED)
    btn_column6.configure(state=DISABLED)
    btn_column7.configure(state=DISABLED)


def check_win(row, col):#function accepts the index of most recently placed token as a parameter to see if the player has won the game.
    #call all global variables
    global main_count
    global label_frame2
    global win_frame
    if(main_count==41):#if all columns are full and a player still has not won, the game has ended in a stalement
        win_frame.configure(text="STALEMATE!")#notify the players that there was a stalemate
        win_frame.grid(row=0, column=0)#place the frame on screen
        label_frame2.destroy()#destroy other label that notified player what turn it was since the game is over.
    elif(main_count%2==1):#every time a token is placed, flip between it being player 1 and player 2's turn
        label_frame2.configure(text="Player 1 place your piece")
    else:
        label_frame2.configure(text="Player 2 place your piece")

    #check if the player won by 4 in a row vertical
    if(row<3):#players winning token must be in row 0, 1, or 2 (top row is row 0 / bottom row is row 5)
        #(x is the winning token position)
        #x
        #o
        #o
        #o
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row+1][col].cget('fg')=='red' and label_ids[row+2][col].cget('fg')=='red' and label_ids[row+3][col].cget('fg')=='red' ):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row+1][col].cget('fg')=='blue' and label_ids[row+2][col].cget('fg')=='blue' and label_ids[row+3][col].cget('fg')=='blue' ): 
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
    
    #check if the player won by 4 in a row horizontal
    if(col<4):#check if the token placed has three tokens of the same color to the right of it
        #(x is the winning token position)
        #xooo
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row][col+1].cget('fg')=='red' and label_ids[row][col+2].cget('fg')=='red' and label_ids[row][col+3].cget('fg')=='red' ):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row][col+1].cget('fg')=='blue' and label_ids[row][col+2].cget('fg')=='blue' and label_ids[row][col+3].cget('fg')=='blue' ):
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            disable()#disable all buttons since the game is over
    if(col>2):#check if the token placed has three tokens of the same color to the left of it
        #(x is the winning token position)
        #ooox
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row][col-1].cget('fg')=='red' and label_ids[row][col-2].cget('fg')=='red' and label_ids[row][col-3].cget('fg')=='red' ):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row][col-1].cget('fg')=='blue' and label_ids[row][col-2].cget('fg')=='blue' and label_ids[row][col-3].cget('fg')=='blue' ):
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            disable()#disable all buttons since the game is over
    if(col<5 and col>0):#check if the token placed has two tokens of the same color to the right of it and one token of the same color to the left of it
        #(x is the winning token position)
        #oxoo
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row][col+1].cget('fg')=='red' and label_ids[row][col+2].cget('fg')=='red' and label_ids[row][col-1].cget('fg')=='red' ):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row][col+1].cget('fg')=='blue' and label_ids[row][col+2].cget('fg')=='blue' and label_ids[row][col-1].cget('fg')=='blue' ):
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            disable()#disable all buttons since the game is over
    if(col<6 and col>1):#check if the token placed has one token of the same color to the right of it and two tokens of the same color to the left of it
        #(x is the winning token position)
        #ooxo
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row][col+1].cget('fg')=='red' and label_ids[row][col-1].cget('fg')=='red' and label_ids[row][col-2].cget('fg')=='red' ):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row][col+1].cget('fg')=='blue' and label_ids[row][col-1].cget('fg')=='blue' and label_ids[row][col-2].cget('fg')=='blue' ):
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            disable()#disable all buttons since the game is over
    
    #check if the player won by 4 in a row diagonal
    if(row<3 and col<4):#check if the token placed has three tokens of the same color in a negative slope below it
        #(x is the winning token position)
        #x
        # o
        #  o
        #   o
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row+1][col+1].cget('fg')=='red' and label_ids[row+2][col+2].cget('fg')=='red' and label_ids[row+3][col+3].cget('fg')=='red'):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row+1][col+1].cget('fg')=='blue' and label_ids[row+2][col+2].cget('fg')=='blue' and label_ids[row+3][col+3].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            disable()#disable all buttons since the game is over
    if(row>2 and col>2):#check if the token placed has three tokens of the same color in a negative slope above it
        #(x is the winning token position)
        #o
        # o
        #  o
        #   x
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row-1][col-1].cget('fg')=='red' and label_ids[row-2][col-2].cget('fg')=='red' and label_ids[row-3][col-3].cget('fg')=='red'):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row-1][col-1].cget('fg')=='blue' and label_ids[row-2][col-2].cget('fg')=='blue' and label_ids[row-3][col-3].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            disable()#disable all buttons since the game is over
    if(row>2 and col<4):#check if the token placed has three tokens of the same color in a positive slope above it
        #(x is the winning token position)
        #   o
        #  o
        # o 
        #x
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row-1][col+1].cget('fg')=='red' and label_ids[row-2][col+2].cget('fg')=='red' and label_ids[row-3][col+3].cget('fg')=='red'):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row-1][col+1].cget('fg')=='blue' and label_ids[row-2][col+2].cget('fg')=='blue' and label_ids[row-3][col+3].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            disable()#disable all buttons since the game is over
    if(row>0 and row<4 and col<6 and col>1):#check if the token placed has one token of the same color above it and two tokens of the same color below it and overall has a positve slope
        #(x is the winning token position)
        #   o
        #  x
        # o 
        #o
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row-1][col+1].cget('fg')=='red' and label_ids[row+1][col-1].cget('fg')=='red' and label_ids[row+2][col-2].cget('fg')=='red'):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row-1][col+1].cget('fg')=='blue' and label_ids[row+1][col-1].cget('fg')=='blue' and label_ids[row+2][col-2].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            disable()#disable all buttons since the game is over
    if(row>1 and row<5 and col<5 and col>0):#check if the token placed has two tokens of the same color above it and one token of the same color below it and overall has a positve slope
        #(x is the winning token position)
        #   o
        #  o
        # x 
        #o
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row-1][col+1].cget('fg')=='red' and label_ids[row-2][col+2].cget('fg')=='red' and label_ids[row+1][col-1].cget('fg')=='red'):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row-1][col+1].cget('fg')=='blue' and label_ids[row-2][col+2].cget('fg')=='blue' and label_ids[row+1][col-1].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            label_frame2.destroy()  #destroy label that notified player what turn it was since the game is over.
            disable() #disable all buttons since the game is over
    if(row<3 and col>2 ):#check if the token placed has three tokens of the same color in a positve slope below it
        #(x is the winning token position)
        #   x
        #  o
        # o 
        #o
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row+1][col-1].cget('fg')=='red' and label_ids[row+2][col-2].cget('fg')=='red' and label_ids[row+3][col-3].cget('fg')=='red'):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row+1][col-1].cget('fg')=='blue' and label_ids[row+2][col-2].cget('fg')=='blue' and label_ids[row+3][col-3].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            disable()#disable all buttons since the game is over
    if(row<4 and row>0 and col>0 and col<5 ):#check if the token placed has two tokens of the same color below it and one token of the same color above it and overall has a negative slope
        #(x is the winning token position)
        #o
        # x
        #  o
        #   o
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row+1][col+1].cget('fg')=='red' and label_ids[row+2][col+2].cget('fg')=='red' and label_ids[row-1][col-1].cget('fg')=='red'):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row+1][col+1].cget('fg')=='blue' and label_ids[row+2][col+2].cget('fg')=='blue' and label_ids[row-1][col-1].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            disable()#disable all buttons since the game is over
    if(row<5 and row>1 and col>1 and col<6 ):#check if the token placed has one token of the same color below it and two tokens of the same color above it and overall has a negative slope
        #(x is the winning token position)
        #o
        # o
        #  x
        #   o
        if (label_ids[row][col].cget('fg')=='red' and label_ids[row+1][col+1].cget('fg')=='red' and label_ids[row-1][col-1].cget('fg')=='red' and label_ids[row-2][col-2].cget('fg')=='red'):
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            win_frame.grid(row=0, column=0)#place winning label on screen
            disable()#disable all buttons since the game is over
        if (label_ids[row][col].cget('fg')=='blue' and label_ids[row+1][col+1].cget('fg')=='blue' and label_ids[row-1][col-1].cget('fg')=='blue' and label_ids[row-2][col-2].cget('fg')=='blue'):
            win_frame.configure(text="Player 2 wins!!!")#edit winning label to say player 2 instead of player 1
            win_frame.grid(row=0, column=0)#place winning label on screen
            label_frame2.destroy()#destroy label that notified player what turn it was since the game is over.
            disable()#disable all buttons since the game is over

def counting_column(column):#function keeps track of how many tokens are in each column, how many overall turns have been taken, places the correct colored token, and checks if that token caused a win
    #call all global variables
    global count_column1
    global count_column2
    global count_column3
    global count_column4
    global count_column5
    global count_column6
    global count_column7
    global label_ids #game board
    global main_count #keeps track of how many times a token has been placed
    if(column==0):#if token is placed in column 0
        if(main_count%2==0):#if it is player 1's turn
            label_ids[count_column1][0].configure(fg='red', image=photo)#change lowest available space to be red 
        else:#if it is player 2's turn
            label_ids[count_column1][0].configure(fg='blue', image=photo_2)#change lowest available space to be blue
        check_win(count_column1, 0)#check if the index the token was just placed in caused a win
        count_column1 = count_column1 - 1 #there is now one less available space in the column
    elif(column==1):#if token is placed in column 1
        if(main_count%2==0):#if it is player 1's turn
            label_ids[count_column2][1].configure(fg='red', image=photo)#change lowest available space to be red 
        else:#if it is player 2's turn
            label_ids[count_column2][1].configure(fg='blue', image=photo_2)#change lowest available space to be blue 
        check_win(count_column2, 1)#check if the index the token was just placed in caused a win
        count_column2 = count_column2 - 1 #there is now one less available space in the column
    elif(column==2):#if token is placed in column 2
        if(main_count%2==0):#if it is player 1's turn
            label_ids[count_column3][2].configure(fg='red', image=photo)#change lowest available space to be red 
        else:#if it is player 2's turn
            label_ids[count_column3][2].configure(fg='blue', image=photo_2)#change lowest available space to be blue 
        check_win(count_column3, 2)#check if the index the token was just placed in caused a win
        count_column3 = count_column3 - 1 #there is now one less available space in the column
    elif(column==3):#if token is placed in column 3
        if(main_count%2==0):#if it is player 1's turn
            label_ids[count_column4][3].configure(fg='red', image=photo)#change lowest available space to be red 
        else:#if it is player 2's turn
            label_ids[count_column4][3].configure(fg='blue', image=photo_2)#change lowest available space to be blue
        check_win(count_column4, 3)#check if the index the token was just placed in caused a win
        count_column4 = count_column4 - 1 #there is now one less available space in the column
    elif(column==4):#if token is placed in column 4
        if(main_count%2==0):#if it is player 1's turn
            label_ids[count_column5][4].configure(fg='red', image=photo)#change lowest available space to be red
        else:#if it is player 2's turn
            label_ids[count_column5][4].configure(fg='blue', image=photo_2)#change lowest available space to be blue
        check_win(count_column5, 4)#check if the index the token was just placed in caused a win
        count_column5 = count_column5 - 1 #there is now one less available space in the column
    elif(column==5):#if token is placed in column 5
        if(main_count%2==0):#if it is player 1's turn
            label_ids[count_column6][5].configure(fg='red', image=photo)#change lowest available space to be red 
        else:#if it is player 2's turn
            label_ids[count_column6][5].configure(fg='blue', image=photo_2)#change lowest available space to be blue
        check_win(count_column6, 5)#check if the index the token was just placed in caused a win
        count_column6 = count_column6 - 1 #there is now one less available space in the column
    elif(column==6):#if token is placed in column 6
        if(main_count%2==0):#if it is player 1's turn
            label_ids[count_column7][6].configure(fg='red', image=photo)#change lowest available space to be red 
        else:#if it is player 2's turn
            label_ids[count_column7][6].configure(fg='blue', image=photo_2)#change lowest available space to be blue
        check_win(count_column7, 6)#check if the index the token was just placed in caused a win
        count_column7 = count_column7 - 1 #there is now one less available space in the column
    main_count = main_count + 1 #there is now one less available space in the entire board
    

def enable_player(column):#function called when a token is placed to check if that column is currently full than passes the rest of the work to another function. Takes in the column that the token was placed in as a parameter.
    #call all global variables 
    global btn_column1
    global btn_column2
    global btn_column3
    global btn_column4
    global btn_column5
    global btn_column6
    global btn_column7
    global label_frame2
    global count_column1
    global count_column2
    global count_column3
    global count_column4
    global count_column5
    global count_column6
    global count_column7
    global main_count
    counting_column(column)#pass the column of the token that was just placed to the counting_column function
    #The next lines of code disables the button to place a token in a specific column if that column no longer has any available spaces.
    if(count_column1<0):
        btn_column1.configure(state=DISABLED)
    if(count_column2<0):
        btn_column2.configure(state=DISABLED)
    if(count_column3<0):
        btn_column3.configure(state=DISABLED)
    if(count_column4<0):
        btn_column4.configure(state=DISABLED)
    if(count_column5<0):
        btn_column5.configure(state=DISABLED)
    if(count_column6<0):
        btn_column6.configure(state=DISABLED)
    if(count_column7<0):
        btn_column7.configure(state=DISABLED)

#the next lines of code creates a button for each column of the connect 4 board and places it on the screen. When a column is pressed a token is placed in the lowest available spot. Pressing one of these buttons places a token and immediately goes to the next player's turn as long as the game isn't over yet.
btn_column1 = Button(frame2, text = 'Column 1', command=partial(enable_player, 0), padx=5,pady=5)
btn_column1.grid(row=3, column = 1)
btn_column2 = Button(frame2, text = 'Column 2', command=partial(enable_player, 1), padx=5,pady=5)
btn_column2.grid(row=3, column=2)
btn_column3 = Button(frame2, text = 'Column 3', command=partial(enable_player, 2), padx=5,pady=5)
btn_column3.grid(row=3, column=3)
btn_column4 = Button(frame2, text = 'Column 4', command=partial(enable_player, 3), padx=5,pady=5)
btn_column4.grid(row=3, column=4)
btn_column5 = Button(frame2, text = 'Column 5', command=partial(enable_player, 4), padx=5,pady=5)
btn_column5.grid(row=3, column=5)
btn_column6 = Button(frame2, text = 'Column 6', command=partial(enable_player, 5), padx=5,pady=5)
btn_column6.grid(row=3, column=6)
btn_column7 = Button(frame2, text = 'Column 7', command=partial(enable_player, 6), padx=5,pady=5)
btn_column7.grid(row=3, column=7)

label_frame1 = Label(frame1, text="Connect 4!\nPress start to begin playing.",font=("Arial", 25)) #label on the welcome frame
label_frame1.place(relx=.5, rely=.1,anchor= CENTER)#place the welcome message on the screen
btn_frame1 = Button(frame1, text="Start", font=("Arial",50, BOLD), command=partial(show_frame,frame2), padx=20,pady=20, compound=CENTER) #Big button to start the game. When pressed it calls frame 2 where the game is actually played.
btn_frame1.place(relx=.5, rely=.5, anchor=CENTER)#place the button on the screen
button_quit_game = Button(frame1, text="Quit",font=("Arial",30, BOLD), command=partial(root.destroy)) #exits the program 
button_quit_game.place(relx=.5, rely=.9, anchor=CENTER)#place the exit button on the screen


label_frame2 = Label(frame2, text="Player 1 place your piece", font=('Helvatical bold',30))#label that notifies the players whose turn it is. Initially it is player 1's turn but for every token placed this message is edited to go back and forth between player 1 and 2.
label_frame2.grid(row=0, column=0)#place the message on the screen
button_quit_game = Button(frame2, text="Press to Quit" , command=root.destroy).grid(row=0, column=40) #press to quit button, closes program

w, h = 7, 6 #the game board has 7 columns and 6 rows
label_ids = [[0 for x in range(w)] for y in range(h)] #create a 2D array to store all the game spaces and their information

for i in range(6):#create 6 rows
    for j in range(7):#create 7 columns
        game_board = Label(frame2, text="O", fg='black', font=('Helvatical bold',50), padx=10,pady=10)#creates empty game board where the tokens will be placed
        game_board.grid(row=4+i, column=j+1)#places game board on the screen
        label_ids[i][j] = game_board#stores the game board in the 2D array so they can be accessed by calling their location in the 2D array (row/column of space)

win_frame = Label(frame2, text="Player 1 wins!!!", font=('Helvatical bold',50))#label that notifies the players that a player has won the game. This label is edited to say player 2 if player 2 wins (in the check_win function)

root.mainloop()#loop through all the frames
