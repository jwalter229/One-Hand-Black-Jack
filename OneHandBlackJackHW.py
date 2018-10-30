
#!/usr/bin/python3


#Jason Walters
#HW 3


import cgi
import random

# Returns a shuffled list of 52 integers from 0 to 51
def getDeck():
    ls = []
    ls.extend(range(52))
    random.shuffle(ls)
    return ls

# Returns a string of the suit and face of a given card
def cardName(num):
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    faces = ("Ace", "Deuce", "Three", "Four", "Five", "Six",
             "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
             "King")
    suitNum = num // 13
    faceNum = num % 13
    return faces[faceNum] + " of " + suits[suitNum]


# Returns an image card
def cardImage(num):
    suits = ("hearts", "diamonds", "clubs", "spades")
    faces = ("ace", "2", "3", "4", "5", "6",
             "7", "8", "9", "10", "jack", "queen",
             "king")
    suitNum = num // 13
    faceNum = num % 13
    return suits[suitNum] + "-" + faces[faceNum] + ".png"

# Returns the face value of a given card (with aces = 1)
def cardFaceVal(num):
    faceIndex = num % 13
    if (faceIndex >= 10):
        return 10
    else:
        return faceIndex + 1

# Creates the shuffled deck by calling getDeck()
#   then deals just two cards for the player and
#   the dealer in the game of Black Jack
def main():
    try:
        print ("Content-type: text/html\n")
        print ("<html>")
        print ("<body style='background-color:lightblue'>")
        print ("<h1 style='color:black'>Welcome to One Hand BlackJack</h1>")

        deck = getDeck()
        currentCard = 0
        playerCard1 = deck[currentCard]
        currentCard += 1
        playerCard2 = deck[currentCard]
        currentCard += 1
        dealerCard1 = deck[currentCard]
        currentCard += 1
        dealerCard2 = deck[currentCard]

        playerHandValue = cardFaceVal(playerCard1) + cardFaceVal(playerCard2)

        if(cardFaceVal(playerCard1) == 1):
            playerHandValue += 10
        elif(cardFaceVal(playerCard2) == 1):
            playerHandValue += 10

        print("<h2> Player Hand:" + str(playerHandValue) + " </h2> ")
        print("<img src='/cards/" + cardImage(playerCard1)+ " '>")
        print("<img src='/cards/"  + cardImage(playerCard2) + " '>")

        #print "\tPlayer's hand value: ", playerHandValue

        dealerHandValue = (cardFaceVal(dealerCard1) + cardFaceVal(dealerCard2))
        if(cardFaceVal(dealerCard1) == 1):
            dealerHandValue += 10
        elif(cardFaceVal(dealerCard2) == 1):
            dealerHandValue += 10

        print("<h2> Dealer Hand:" + str(dealerHandValue) + " </h2> ")
        print("<img src='/cards/" + cardImage(dealerCard1)+ " '>")
        print("<img src='/cards/"  + cardImage(dealerCard2) + " '>")

        #print "\tDealer's hand value: ", dealerHandValue

        if (dealerHandValue >= playerHandValue):
            print("<h2>Dealer wins!</h2>")
        else:
            print("<h2>Player wins!</h2>")
        print ("<button onclick = 'location.reload()'> Play Again </button>")

    except:
        print ("<!-- --><hr><h1>Oops.  An error occurred.</h1>")
        cgi.print_exception()  # Prints traceback, safely


    print ("</body></html>")

main()