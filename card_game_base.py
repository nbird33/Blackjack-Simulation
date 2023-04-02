

# Date: 3/31/23-first coded
# Output: simple playing cards simulator that shuffles two cards
# with images and can deal them out until there is none left in single deck
# could be used as the foundation of basicly any card game aka poker, blackjack, war


from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()
root.title(" ")
root.geometry("900x500")
root.configure(background="green")

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
    global dealer, player
    dealer = []
    player = []

    # grab a random card for dealer
    card = random.choice(deck)
    # remove card from deck
    deck.remove(card)
    # append card to dealer list
    dealer.append(card)
    # output card to screen
    global dealer_image
    dealer_image = resize_cards(f"Desktop/PPprojects/playing_cards_images/{card}.png")
    dealer_label.config(image=dealer_image)

    
    # grab a random card for player
    card = random.choice(deck)
    # remove card from deck
    deck.remove(card)
    # append card to dealer list
    player.append(card)
    # output card to screen
    global player_image
    player_image = resize_cards(f"Desktop/PPprojects/playing_cards_images/{card}.png")
    player_label.config(image=player_image)


    # put number of remain cards in title bar
    root.title(f"{len(deck)} cards left")

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
        dealer_label.config(image=dealer_image)

        # get the players card
        card = random.choice(deck)
        # remove card from deck
        deck.remove(card)
        # append card to dealer list
        player.append(card)
        # output card to screen
        global player_image
        player_image = resize_cards(f"Desktop/PPprojects/playing_cards_images/{card}.png")
        player_label.config(image=player_image)
        # player_label.config(text=card)

        root.title(f"{len(deck)} cards left")
                   
    except:
        root.title(f"No more cards in deck")


my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# create frames for cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

# put cards in frames
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

# create button frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

# create few buttons
shuffle_button = Button(button_frame, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.grid(row=0, column=0)

deal_button = Button(button_frame, text="Deal Cards", font=("Helvetica", 14), command=deal_cards)
deal_button.grid(row=0, column=1, padx=10)




shuffle()
root.mainloop()