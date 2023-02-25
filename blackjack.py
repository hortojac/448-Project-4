from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.font import BOLD, Font

root = Tk()
root.title('BlackJack')
root.geometry("1920x1080")
root.configure(bg="green")

#Frame for Dealer LabelFrame
frame1 = Frame(root, bg="green", bd=0)
frame1.pack(pady=20)

#Button Frame
button_frame = Frame(root, bg="green", bd=0)
button_frame.pack(pady=20)

#Frame for Player LabelFrame
frame2 = Frame(root, bg="green", bd=0)
frame2.pack(pady=20)

#Message Popup for Welcome
messagebox.showinfo("Welcome!", "Welcome to BlackJack!")

#Rules function for rules Popup
def rules():
    messagebox.showinfo("Rules!", "Player attempts to beat the dealer by getting a count as close to 21 as possible without busting. \
Face cards are worth 10. Aces are worth 1 or 11. Numbered Cards are worth their number value. \
Click the Deal button to be dealt new cards. Click the Hit button to be dealt a card. Click the Stand button to hold your total.")

#Message Function for outputing scores of winner
def message(winner):
    global player_total
    global dealer_total
    btn_hit.config(state="disabled")
    btn_stand.config(state="disabled")
    root.update()
    root.after(500)
    if winner == "player": #outputs that player wins
        messagebox.showinfo("Player Wins!", f"Player Wins!  Player: {player_total}  Dealer: {dealer_total}")
    elif winner == "dealer": #outputs that dealer wins
        messagebox.showinfo("Dealer Wins!", f"Dealer Wins!  Dealer: {dealer_total}  Player: {player_total}")
    elif winner == "push": #outputs that there's a push
        messagebox.showinfo("Push!", f"Push!  Dealer: {dealer_total}  Player: {player_total}")
    elif winner == "bust": #outputs that player busts
        messagebox.showinfo("Player Busts!", f"Player Busts!  Player: {player_total}")

#Stand function
def stand():
    global player_total 
    global dealer_total 
    global player_card_index 
    global dealer_card_index
    player_total = 0 #player score total
    dealer_total = 0 #dealer score total

    for total in dealer_card_index:
        dealer_total += total #dealer_total

    for total in player_card_index:
        player_total += total #player total

    if dealer_total >= 17:
        if dealer_total > 21:
            message("player") #player wins when dealer total greater than 21
        elif dealer_total == player_total:
            message("push") #push or tie when totals are the same
        elif dealer_total > player_total:
            message("dealer") #dealer wins when dealer total greater then player total
        else:
            message("player") #else player wins
    else:
        dealer_hit() #hits again for dealer when less than 17
        stand() #calls stand again

def blackjack_on_shuffle(user):
    global player_total 
    global dealer_total 
    global player_card_index 
    global dealer_card_index
    player_total = 0 #player score total
    dealer_total = 0 #dealer score total
    if user == "dealer":
        if len(dealer_card_index) == 2: #first two cards
            if dealer_card_index[0] + dealer_card_index[1] == 21: #if two dealt cards equal 21
                win_status["dealer"] = "true" #dealer wins on dealt 21
                dealer_total = 21 #dealer total equals 21
                player_total = player_card_index[0] + player_card_index[1] #player total is equal to its two dealt cards

    elif user == "player":
        if len(player_card_index) == 2: #first two cards
            if player_card_index[0] + player_card_index[1] == 21: #if two dealt cards equal 21
                win_status["player"] = "true" #player wins on dealt 21
                player_total = 21 #player total equals 21
                dealer_total = dealer_card_index[0] + dealer_card_index[1] #dealer total is equal to its two dealt cards
        else:
            for total in player_card_index:
                player_total += total #adds up player total

            if player_total == 21:
                win_status["player"] = "true" #if total equals 21 then player wins
            
            elif player_total > 21:
                for card_number, card in enumerate(player_card_index):
                    if card == 11: #Ace conversion 
                        player_card_index[card_number] = 1
                        player_total = 0 #new player total set to zero
                        for total in player_card_index:
                            player_total += total #adds up new total
                        if player_total > 21:
                            win_status["player"] = "bust" #player busts if new total is greater than 21
                else:
                    if player_total == 21: #if player total is 21 then player wins
                        win_status["player"] = "true"
                    elif player_total > 21: #if player total id greater than 21 then player busts
                        win_status["player"] = "bust"

    if len(dealer_card_index) == 2 and len(player_card_index) == 2:
        if win_status["dealer"] == "true" and win_status["player"] == "true":
            message("push") #push when first two dealt cards are 21
        elif win_status["dealer"] == "true":
            message("dealer") #dealer wins when first two dealt cards are 21
        elif win_status["player"] == "true":
            message("player") #player wins when first two dealt cards are 21
    else:
        if win_status["dealer"] == "true" and win_status["player"] == "true":
            message("push") #push when cards are equal to 21
        elif win_status["dealer"] == "true":
            message("dealer") #dealer wins when cards are equal to 21
        elif win_status["player"] == "true":
            message("player") #player wins when cards are equal to 21
    if win_status["player"] == "bust":
        message("bust") #player busts

def resize_cards(card): #function for resizing cards
    global final_image
    card_image = Image.open(card)
    image_resize = card_image.resize((150, 218))
    final_image = ImageTk.PhotoImage(image_resize)
    return final_image

def deal_cards():
    global win_status
    global player_total
    global dealer_total
    global dealer 
    global player
    global dealer_index 
    global player_index
    global dealer_card_index 
    global player_card_index
    global card_deck
    card_deck = [] #card_deck list
    dealer = [] #dealer list
    player = [] #player list
    dealer_card_index = [] #dealer score list
    player_card_index = [] #player score list
    dealer_index = 0
    player_index = 0
    player_total = 0 #player score total
    dealer_total = 0 #dealer score total
    win_status = {"dealer":"false", "player":"false"} #win status of player and dealer
    btn_hit.config(state="normal") #enable hit button
    btn_stand.config(state="normal") #enable stand button

    dealer_image_1.config(image='') #clears dealer image 1
    dealer_image_2.config(image='') #clears dealer image 2
    dealer_image_3.config(image='') #clears dealer image 3
    dealer_image_4.config(image='') #clears dealer image 4
    dealer_image_5.config(image='') #clears dealer image 5

    player_image_1.config(image='') #clears player image 1
    player_image_2.config(image='') #clears player image 2
    player_image_3.config(image='') #clears player image 3
    player_image_4.config(image='') #clears player image 4
    player_image_5.config(image='') #clears player image 5

    # suits and values of card_deck
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)

    for suit in suits:
        for value in values:
            card_deck.append(f'{value}_of_{suit}')

    dealer_hit() #deals dealer one card
    dealer_hit() #deals dealer second card
    player_hit() #deals dealer one card
    player_hit() #deals dealer second card

def dealer_hit():
    global dealer_index
    if dealer_index < 5:
        dealer_card = random.choice(card_deck) #random choice of card for dealer
        card_deck.remove(dealer_card) #removes card from dealer card_deck
        dealer.append(dealer_card) #appends card to dealer
        current_dealer_card = int(dealer_card.split("_", 1)[0])
        if current_dealer_card == 14: #if card value is 14
            dealer_card_index.append(11) #appends 11 for ace
        elif current_dealer_card == 11 or current_dealer_card == 12 or current_dealer_card == 13: #if value is 11, 12, 13
            dealer_card_index.append(10) #appends value 10 for face cards
        else:
            dealer_card_index.append(current_dealer_card) #appends number value from number cards

        global dimage1, dimage2, dimage3, dimage4, dimage5

        if dealer_index == 0: #for index 0, sets image to 1st image index
            dimage1 = resize_cards(f'Assets/cards/{dealer_card}.png')
            dealer_image_1.config(image=dimage1)
            dealer_index += 1 #adds 1 to index
        elif dealer_index == 1: #for index 1, sets image to 2nd image index
            dimage2 = resize_cards(f'Assets/cards/{dealer_card}.png')
            dealer_image_2.config(image=dimage2)
            dealer_index += 1 #adds 2 to index
        elif dealer_index == 2: #for index 2, sets image to 3rd image index
            dimage3 = resize_cards(f'Assets/cards/{dealer_card}.png')
            dealer_image_3.config(image=dimage3)
            dealer_index += 1 #adds 3 to index
        elif dealer_index == 3: #for index 3, sets image to 4th image index
            dimage4 = resize_cards(f'Assets/cards/{dealer_card}.png')
            dealer_image_4.config(image=dimage4)
            dealer_index += 1 #adds 4 to index
        elif dealer_index == 4: #for index 4, sets image to 5th image index
            dimage5 = resize_cards(f'Assets/cards/{dealer_card}.png')
            dealer_image_5.config(image=dimage5)
            dealer_index += 1 #adds 5 to index
        blackjack_on_shuffle("dealer")

def player_hit():
    global player_index
    if player_index < 5:
        player_card = random.choice(card_deck) #random choice of card for player
        card_deck.remove(player_card) #removes card from player card_deck
        player.append(player_card) #appends card to player
        current_player_card = int(player_card.split("_", 1)[0])
        if current_player_card == 14: #if card value is 14
            player_card_index.append(11) #appends 11 for ace
        elif current_player_card == 11 or current_player_card == 12 or current_player_card == 13: #if value is 11, 12, 13
            player_card_index.append(10) #appends value 10 for face cards
        else:
            player_card_index.append(current_player_card) #appends number value from number cards

        global pimage1, pimage2, pimage3, pimage4, pimage5

        if player_index == 0: #for index 0, sets image to 1st image index
            pimage1 = resize_cards(f'Assets/cards/{player_card}.png')
            player_image_1.config(image=pimage1)
            player_index += 1 #adds 1 to index
        elif player_index == 1: #for index 0, sets image to 2nd image index
            pimage2 = resize_cards(f'Assets/cards/{player_card}.png')
            player_image_2.config(image=pimage2)
            player_index += 1 #adds 2 to index
        elif player_index == 2: #for index 0, sets image to 3rd image index
            pimage3 = resize_cards(f'Assets/cards/{player_card}.png')
            player_image_3.config(image=pimage3)
            player_index += 1 #adds 3 to index
        elif player_index == 3: #for index 0, sets image to 4th image index
            pimage4 = resize_cards(f'Assets/cards/{player_card}.png')
            player_image_4.config(image=pimage4)
            player_index += 1 #adds 4 to index
        elif player_index == 4:#for index 0, sets image to 5th image index
            pimage5 = resize_cards(f'Assets/cards/{player_card}.png')
            player_image_5.config(image=pimage5)
            player_index += 1 #adds 5 to index
        blackjack_on_shuffle("player")

#Dealer Text 
dealer_text = Label(frame1, text="Dealer's Cards", font=("Helvetica", 25, "bold"), bd=0, bg="white")
dealer_text.pack(padx=20, ipadx=20, pady=10)

#Player Text
player_text = Label(frame2, text="Player's Cards", font=("Helvetica", 25, "bold"), bd=0, bg="white")
player_text.pack(padx=20, ipadx=20, pady=10)

#Dealer LabelFrame for images
dealer_frame = LabelFrame(frame1, bd=0, bg="green")
dealer_frame.pack()

#Player Labelframe for images
player_frame = LabelFrame(frame2, bd=0, bg="green")
player_frame.pack()

#Dealer Image Labels
dealer_image_1 = Label(dealer_frame, bg="green")
dealer_image_1.grid(row=0, column=0, pady=20, padx=20)

dealer_image_2 = Label(dealer_frame, bg="green")
dealer_image_2.grid(row=0, column=1, pady=20, padx=20)

dealer_image_3 = Label(dealer_frame, bg="green")
dealer_image_3.grid(row=0, column=2, pady=20, padx=20)

dealer_image_4 = Label(dealer_frame, bg="green")
dealer_image_4.grid(row=0, column=3, pady=20, padx=20)

dealer_image_5 = Label(dealer_frame, bg="green")
dealer_image_5.grid(row=0, column=4, pady=20, padx=20)

#Player Image Labels
player_image_1 = Label(player_frame, bg="green")
player_image_1.grid(row=1, column=0, pady=20, padx=20)

player_image_2 = Label(player_frame, bg="green")
player_image_2.grid(row=1, column=1, pady=20, padx=20)

player_image_3 = Label(player_frame, bg="green")
player_image_3.grid(row=1, column=2, pady=20, padx=20)

player_image_4 = Label(player_frame, bg="green")
player_image_4.grid(row=1, column=3, pady=20, padx=20)

player_image_5 = Label(player_frame, bg="green")
player_image_5.grid(row=1, column=4, pady=20, padx=20)

#Buttons
btn_rules = Button(button_frame, width = 10, text="Rules", font=("Helvetica", 25, "bold"), bd=0, command=rules)
btn_rules.grid(row=0, column=0, padx=10)

btn_shuffle = Button(button_frame, width = 10, text="Deal Cards", font=("Helvetica", 25, "bold"), bd=0, command=deal_cards)
btn_shuffle.grid(row=0, column=1, padx=10)

btn_hit = Button(button_frame, width = 10, text="Hit", font=("Helvetica", 25, "bold"), bd=0, command=player_hit)
btn_hit.grid(row=0, column=2, padx=10)

btn_stand = Button(button_frame, width = 10, text="Stand", font=("Helvetica", 25, "bold"), bd=0, command=stand)
btn_stand.grid(row=0, column=3, padx=10)

btn_exit = Button(button_frame, width = 10, text="Exit", font=("Helvetica", 25, "bold"), bd=0, command=root.destroy)
btn_exit.grid(row=0, column=4, padx=10)

deal_cards()

root.mainloop()
