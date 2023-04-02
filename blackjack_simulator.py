
# Date: 3/31/23-first coded

# Goal: using to GUI create a blackjack simulation
# it involves handling several complex interactions between 
# the game logic, the user interface, and the players' actions
 
# Future update plans: add a bank type system to keep track of bets/score, maybe make code more clean somehow

from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox


root = Tk()
root.title("Noah Bird - Blackjack Simulator")
root.geometry("1000x730")
root.configure(background="green")

# stand
def stand():
    global player_total, dealer_total
    # keep track of score totals
    player_total = 0
    dealer_total = 0

    # get the dealers score total
    for score in dealer_score:
        # add score
        dealer_total += score

    # loop through player score list and add up cards
    for score in player_score:
        # add score
        player_total += score

    # freeze the buttons
    deal_button.config(state="disabled")
    stand_button.config(state="disabled")

    # logic
    if dealer_total >= 17:
        # check if bust
        if dealer_total > 21:
            messagebox.showinfo(":)", f"Player wins!! Dealer busted with {dealer_total}")
        
        # check if tie
        elif dealer_total == player_total:
            messagebox.showinfo("Push!!", f"Tie game!! You both had {dealer_total}")

        # dealer wins
        elif dealer_total > player_total:
            messagebox.showinfo(":(", f"Dealer wins!! Dealer wins with {dealer_total}")

        # player wins
        else:
            messagebox.showinfo(":)", f"Player wins!! Player wins with {player_total}")

    # dealer has less than 17 so they need to pull another card
    else:
        # add card to dealer
        dealer_hit()
        # recaculate
        stand()    

# test for blackjack on shuffle
def blackjack_shuffle(player):
    global player_total, dealer_total
    # keep track of score totals
    player_total = 0
    dealer_total = 0

    if player == "dealer": 
        if len(dealer_score) == 2:
            if dealer_score[0] + dealer_score[1] == 21:
                # update status
                blackjack_status["dealer"] = "yes"
        else:
            # loop through dealer score list and add up cards
            for score in dealer_score:
                # add score
                dealer_total += score

            if player_total == 21:
                blackjack_status["dealer"] = "yes"

            elif dealer_total > 21:
                # check for ace conversion
                for card_num, dcard in enumerate(dealer_score):
                    if dcard == 11:
                        dealer_score[card_num] = 1

                        # clear dealer total and recalculate
                        dealer_total = 0
                        for score in dealer_score:
                            # add up score with ace converted
                            dealer_total += score
                        # check for over 21
                        if dealer_total > 21:
                            blackjack_status["dealer"] = "bust"
                else:
                    # check new totals for 21 or over 21
                    if dealer_total == 21:
                        blackjack_status["dealer"] = "yes"
                    if dealer_total > 21:
                        blackjack_status["dealer"] = "bust"
               
    if player == "player":
        if len(player_score) == 2:
            if player_score[0] + player_score[1] == 21:
                # update status
                blackjack_status["player"] = "yes"
        else:
            # loop through player score list and add up cards
            for score in player_score:
                # add score
                player_total += score

            if player_total == 21:
                blackjack_status["player"] = "yes"

            elif player_total > 21:
                # check for ace conversion
                for card_num, pcard in enumerate(player_score):
                    if pcard == 11:
                        player_score[card_num] = 1

                        # clear player total and recalculate
                        player_total = 0
                        for score in player_score:
                            # add up score with ace converted
                            player_total += score
                        # check for over 21
                        if player_total > 21:
                            blackjack_status["player"] = "bust"
                else:
                    # check new totals for 21 or over 21
                    if player_total == 21:
                        blackjack_status["player"] = "yes"
                    if player_total > 21:
                        blackjack_status["player"] = "bust"                   
                     
    if len(dealer_score) == 2 and len(player_score) == 2:
        # check for push/tie
        if blackjack_status["dealer"] == "yes" and blackjack_status["player"] == "yes":
            # its a push/tie situation
            messagebox.showinfo("Push", "Tie Game! Its a push!")
            # disable buttons
            deal_button.config(state="disabled")
            stand_button.config(state="disabled")

        # check if dealer won
        elif blackjack_status["dealer"] == "yes":
            messagebox.showinfo(":(", "Sorry, Dealer Wins")
            # disable buttons
            deal_button.config(state="disabled")
            stand_button.config(state="disabled")

        # check if player won
        elif blackjack_status["player"] == "yes":
            messagebox.showinfo(":)", "Congrats you won!!!! :)")
            # disable buttons
            deal_button.config(state="disabled")
            stand_button.config(state="disabled")

    # check for 21 during the game            
    elif len(player_score) > 2:
        # check for push/tie
        if blackjack_status["dealer"] == "yes" and blackjack_status["player"] == "yes":
            # its a push/tie situation
            messagebox.showinfo("Push", "Tie Game! Its a push!")
            # disable buttons
            deal_button.config(state="disabled")
            stand_button.config(state="disabled")

        # check if dealer won
        elif blackjack_status["dealer"] == "yes":
            messagebox.showinfo(":(", "Sorry, Dealer Wins")
            # disable buttons
            deal_button.config(state="disabled")
            stand_button.config(state="disabled")

        # check if player won
        elif blackjack_status["player"] == "yes":
            messagebox.showinfo(":)", "Congrats you won!!!! :)")
            # disable buttons
            deal_button.config(state="disabled")
            stand_button.config(state="disabled")
        elif blackjack_status["player"] == "bust":
            messagebox.showinfo(f"{player_total}", "Player Busts! Dealer Wins")
            # disable buttons
            deal_button.config(state="disabled")
            stand_button.config(state="disabled")        


# resize cards
def resize_cards(card):
    # open the image
    our_card_img = Image.open(card)

    # resize the image
    our_card_resize_image = our_card_img.resize((150, 218))
    # output the card
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)
    # return that card
    return our_card_image

# shuffle the cards
def shuffle():
    # keep track of winning
    global blackjack_status, player_total, dealer_total

    # keep track of score totals
    player_total = 0
    dealer_total = 0

    blackjack_status = {"dealer":"no", "player":"no"}

    # disable buttons
    deal_button.config(state="normal")
    stand_button.config(state="normal")

    # clear all the old cards from previous game
    dealer_label_1.config(image='')
    dealer_label_2.config(image='')
    dealer_label_3.config(image='')
    dealer_label_4.config(image='')
    dealer_label_5.config(image='')

    player_label_1.config(image='')
    player_label_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')

    # define the deck
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2,15)
    # 11=Jack, 12=Queen, 13=King, 14=Ace

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f"{value}_of_{suit}")

    # create players
    global dealer, player, dealer_spot, player_spot, dealer_score, player_score
    dealer = []
    player = []
    dealer_score = []
    player_score = []
    dealer_spot = 0
    player_spot = 0

    # shuffle two cards for player and dealer
    dealer_hit()
    dealer_hit()

    player_hit()
    player_hit()

    # put number of remain cards in title bar
    root.title(f"Noah Bird - Blackjack Simulator - {len(deck)} cards left")


def dealer_hit():
    global dealer_spot,player_total, dealer_total, dealer_score
    if dealer_spot <= 5:
        try:
            # get the players card
            dealer_card = random.choice(deck)
            # remove card from deck
            deck.remove(dealer_card)
            # append card to dealer list
            dealer.append(dealer_card)
            # append to dealer score list and convert facecards to 10 or 11
            dcard = int(dealer_card.split("_", 1)[0])
            if dcard == 14:
                dealer_score.append(11)
            elif dcard == 11 or dcard == 12 or dcard == 13:
                dealer_score.append(10)
            else:
                dealer_score.append(dcard)    


            # output card to screen
            global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5
            
            if dealer_spot == 0:
                # resize card
                dealer_image1 = resize_cards(f"Desktop/PPprojects/playing_cards_images/{dealer_card}.png")
                # output card to screen
                dealer_label_1.config(image=dealer_image1)
                # increment dealer spot counter
                dealer_spot += 1
            elif dealer_spot == 1:
                # resize card
                dealer_image2 = resize_cards(f"Desktop/PPprojects/playing_cards_images/{dealer_card}.png")
                # output card to screen
                dealer_label_2.config(image=dealer_image2)
                # increment dealer spot counter
                dealer_spot += 1
            elif dealer_spot == 2:
                # resize card
                dealer_image3 = resize_cards(f"Desktop/PPprojects/playing_cards_images/{dealer_card}.png")
                # output card to screen
                dealer_label_3.config(image=dealer_image3)
                # increment dealer spot counter
                dealer_spot += 1
            elif dealer_spot == 3:
                # resize card
                dealer_image4 = resize_cards(f"Desktop/PPprojects/playing_cards_images/{dealer_card}.png")
                # output card to screen
                dealer_label_4.config(image=dealer_image4)
                # increment dealer spot counter
                dealer_spot += 1
            elif dealer_spot == 4:
                # resize card
                dealer_image5 = resize_cards(f"Desktop/PPprojects/playing_cards_images/{dealer_card}.png")
                # output card to screen
                dealer_label_5.config(image=dealer_image5)
                # increment dealer spot counter
                dealer_spot += 1

            # put number of remaining cards in title bar
            root.title(f"Noah Bird - Blackjack Simulator - {len(deck)} cards left")

        except:
            root.title(f"Noah Bird - Blackjack Simulator - No more cards in deck")

        # check for blackjack
        blackjack_shuffle("dealer")

def player_hit():
    global player_spot, player_total, dealer_total, player_score
    if player_spot <= 5:
        try:
            # get the players card
            player_card = random.choice(deck)
            # remove card from deck
            deck.remove(player_card)
            # append card to player list
            player.append(player_card)
            # append to dealer score list and convert facecards to 10 or 11
            pcard = int(player_card.split("_", 1)[0])
            if pcard == 14:
                player_score.append(11)
            elif pcard == 11 or pcard == 12 or pcard == 13:
                player_score.append(10)
            else:
                player_score.append(pcard) 

            # output card to screen
            global player_image1, player_image2, player_image3, player_image4, player_image5
            
            if player_spot == 0:
                # resize card
                player_image1 = resize_cards(f"Desktop/PPprojects/playing_cards_images/{player_card}.png")
                # output card to screen
                player_label_1.config(image=player_image1)
                # increment player spot counter
                player_spot += 1
            elif player_spot == 1:
                # resize card
                player_image2 = resize_cards(f"Desktop/PPprojects/playing_cards_images/{player_card}.png")
                # output card to screen
                player_label_2.config(image=player_image2)
                # increment player spot counter
                player_spot += 1
            elif player_spot == 2:
                # resize card
                player_image3 = resize_cards(f"Desktop/PPprojects/playing_cards_images/{player_card}.png")
                # output card to screen
                player_label_3.config(image=player_image3)
                # increment player spot counter
                player_spot += 1
            elif player_spot == 3:
                # resize card
                player_image4 = resize_cards(f"Desktop/PPprojects/playing_cards_images/{player_card}.png")
                # output card to screen
                player_label_4.config(image=player_image4)
                # increment player spot counter
                player_spot += 1
            elif player_spot == 4:
                # resize card
                player_image5 = resize_cards(f"Desktop/PPprojects/playing_cards_images/{player_card}.png")
                # output card to screen
                player_label_5.config(image=player_image5)
                # increment player spot counter
                player_spot += 1

            # put number of remaining cards in title bar
            root.title(f"Noah Bird - Blackjack Simulator - {len(deck)} cards left")
            
        except:
            root.title(f"Noah Bird - Blackjack Simulator - No more cards in deck")

        # check for blackjack
        blackjack_shuffle("player")

# deal out cards
def deal_cards():
    try:
        # get the dealers card
        card = random.choice(deck)
        # remove card from deck
        deck.remove(card)
        # append card to dealer list
        dealer.append(card)
        # output card to screen
        global dealer_image
        dealer_image = resize_cards(f"Desktop/PPprojects/playing_cards_images/{card}.png")
        dealer_label_1.config(image=dealer_image)

        # get the players card
        card = random.choice(deck)
        # remove card from deck
        deck.remove(card)
        # append card to player list
        player.append(card)
        # output card to screen
        global player_image
        player_image = resize_cards(f"Desktop/PPprojects/playing_cards_images/{card}.png")
        player_label_1.config(image=player_image)
        # player_label.config(text=card)

        # put number of remaining cards in title bar
        root.title(f"Noah Bird - Blackjack Simulator - {len(deck)} cards left")
                   
    except:
        root.title(f"Noah Bird - Blackjack Simulator - No more cards in deck")



my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# create frames for cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.pack(ipadx=20, pady=10)

# put dealer cards in frames
dealer_label_1 = Label(dealer_frame, text='')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_frame, text='')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_frame, text='')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = Label(dealer_frame, text='')
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = Label(dealer_frame, text='')
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

# put player cards in frames
player_label_1 = Label(player_frame, text='')
player_label_1.grid(row=1, column=0, pady=20, padx=20)

player_label_2 = Label(player_frame, text='')
player_label_2.grid(row=1, column=1, pady=20, padx=20)

player_label_3 = Label(player_frame, text='')
player_label_3.grid(row=1, column=2, pady=20, padx=20)

player_label_4 = Label(player_frame, text='')
player_label_4.grid(row=1, column=3, pady=20, padx=20)

player_label_5 = Label(player_frame, text='')
player_label_5.grid(row=1, column=4, pady=20, padx=20)

# create button frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

# create few buttons
shuffle_button = Button(button_frame, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.grid(row=0, column=0)

deal_button = Button(button_frame, text="Hit!", font=("Helvetica", 14), command=player_hit)
deal_button.grid(row=0, column=1, padx=10)

stand_button = Button(button_frame, text="Stand!", font=("Helvetica", 14), command=stand)
stand_button.grid(row=0, column=2)



# shuffle deck on start
shuffle()
root.mainloop()




# dang almost 500 lines