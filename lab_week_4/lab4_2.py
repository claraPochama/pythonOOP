from lab4_2_module import card, deck

def main():
    print("Card Dealer\n")

    deck_here = deck()
    deck_here.shuffle()
    print("I have shuffled a deck of 52 cards.\n")
    draw_cards = int(input("How many cards would you like?: "))
    print("Here are your cards: ")
    for i in range(draw_cards): 
        print(deck_here.deal())
    print("There are ", deck_here.count(), "cards left in the deck. ")
   
    
if __name__ == "__main__":
    main()