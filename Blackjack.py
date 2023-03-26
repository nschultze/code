import random

def aceValue(userHand, userAceValue):
    userAceValue = input("Ace Drawn. Type l for 1 or h  for 11? ")
    if(userAceValue == "l"):
        userHand = userHand + 1
    elif(userAceValue == "h"):
        userHand = userHand + 11
    else:
        userAceValue = input("Ace Drawn. Type l for 1 or h  for 11? ")
    return userHand

def userDraw(userHand, cardList):
    cardDrawn = random.randint(0, len(cardList) - 1)
    if(cardList[cardDrawn] == 1):
        userAceValue = input("Ace Drawn. Type l for 1 or h  for 11? ")
        userHand = aceValue(userHand, userAceValue)
    elif((cardList[cardDrawn] > 1) and (cardList[cardDrawn] <= 10)):
        userHand = userHand + cardList[cardDrawn]
    elif(cardList[cardDrawn] == 11):
        userHand = userHand + 10
    elif(cardList[cardDrawn] == 12):
        userHand = userHand + 10
    elif(cardList[cardDrawn] == 13):
        userHand = userHand + 10
    cardList.remove(cardList[cardDrawn])
    return userHand, cardList

def userCheckHand(userHand, cardList):
    if(userHand == 21):
        pass
    elif(userHand > 21):
        pass
    elif(userHand < 21):
        userHand, cardList = userHitAgain(userHand, cardList)
    return userHand, cardList

def userHitAgain(userHand, cardList):
    hitAgain = input("Type h if you want to hit, type s if you want to stay: ")
    if(hitAgain == "h"):
        userHand, cardList = userDraw(userHand, cardList)
        print("User Hand: ", userHand)
        userHand, cardList = userCheckHand(userHand, cardList)
    elif(hitAgain == "s"):
        pass
    else:
        userHand, cardList = userHitAgain(userHand, cardList)
    return userHand, cardList

def dealerDraw(dealerHand, cardList):
    cardDrawn = random.randint(1, len(cardList) - 1)
    if((cardList[cardDrawn] > 1) and (cardList[cardDrawn] <= 10)):
        dealerHand = dealerHand + cardList[cardDrawn]
    elif(cardList[cardDrawn] == 11):
        dealerHand = dealerHand + 10
    elif(cardList[cardDrawn] == 12):
        dealerHand = dealerHand + 10
    elif(cardList[cardDrawn] == 13):
        dealerHand = dealerHand + 10
    elif(cardList[cardDrawn] == 1):
        if((dealerHand + 11) < 21):
            dealerHand = dealerHand + 11
        elif((dealerHand + 11) > 21):
            dealerHand = dealerHand + 1
    cardList.remove(cardList[cardDrawn])
    return dealerHand, cardList

def dealerCheckHand(dealerHand, cardList):
    if(dealerHand == 21):
        pass
    elif(dealerHand > 17):
        pass
    elif(dealerHand < 17):
        dealerHand, cardList = dealerDraw(dealerHand, cardList)
        dealerHand, cardList = dealerCheckHand(dealerHand, cardList)
    return dealerHand, cardList

def whoWon(userHand, dealerHand, bet):
    if(userHand > 21):
        bet = 0
        print("User Busted")
    elif((userHand == dealerHand) and (userHand == 21)):
        bet = bet
        print("Draw. User and Dealer has Blackjack")
    elif((userHand > dealerHand) and (userHand == 21)):
        bet = 2.5 * bet
        print("User has Blackjack. User won", bet)
    elif((userHand < dealerHand) and (userHand == 21)):
        bet = 2.5 * bet
        print("User has Blackjack. User won", bet)
    elif((userHand < 21) and (dealerHand == 21)):
        bet = 0
        print("Dealer has Blackjack")
    elif((userHand > dealerHand) and (userHand < 21)):
        bet = 2 * bet
        print("User Won", bet)
    elif((userHand < dealerHand) and (userHand < 21) and (dealerHand < 21)):
        bet = 0
        print("User Lost")
    elif((userHand < dealerHand) and (dealerHand > 21)):
        bet = 2 * bet
        print("Dealer Busted. User Won", bet)
    elif((userHand > 21) and (dealerHand > 21)):
        bet = 0
        print("User Lost. User and Dealer Busted")
        return userHand, dealerHand, bet
    elif((userHand == dealerHand) and (userHand < 21)):
        bet = bet
        print("Draw")
    return userHand, dealerHand, bet

def resetUserHand(userhand):
    userHand = 0
    return userHand

def resetDealerHand(dealerHand):
    dealerHand = 0
    return dealerHand

def resetDeck(cardList):
    cardList = list((list(range(1, 14)) + list(range(1, 14)) + list(range(1, 14)) + list(range(1, 14))))
    return  cardList

def play(userHand, dealerHand, cardList, bet):
    userHand, cardList = userDraw(userHand, cardList)
    dealerHand, cardList = dealerDraw(dealerHand, cardList)

    userHand, cardList = userDraw(userHand, cardList)
    dealerHand, cardList = dealerDraw(dealerHand, cardList)

    print("User Hand: ", userHand)
    userHand, cardList = userCheckHand(userHand, cardList)
    dealerHand, cardList = dealerCheckHand(dealerHand, cardList)
    print("Dealer Hand: ", dealerHand)

    userHand, dealerHand, bet = whoWon(userHand, dealerHand, bet)
    print(bet)

    userHand = resetUserHand(userHand)
    dealerHand = resetDealerHand(dealerHand)
    cardList = resetDeck(cardList)

    if(bet > 0):
        anotherGame = input("Do you want to play again? Type y for Yes.")
        if(anotherGame == "y"):
            userHand, dealerHand, cardList, bet = playAgain(userHand, dealerHand, cardList, bet)
        else:
            exit()
    else:
        exit()

def playAgain(userHand, dealerHand, cardList, bet):
    userHand, dealerHand, cardList, bet = play(userHand, dealerHand, cardList, bet)
    return userHand, dealerHand, cardList, bet

def bettingAmount():
    bet = int(input("How much do you want to bet? "))
    if(bet > 0):
        return bet
    else:
        bettingAmount()

userHand = 0
dealerHand = 0
cardList = list((list(range(1, 14)) + list(range(1, 14)) + list(range(1, 14)) + list(range(1, 14))))

try:
    gameReady = input("Type y if you are ready to play: ")
    bet = bettingAmount()
    if(gameReady == "y"):
        userHand, dealerHand, cardList, bet = play(userHand, dealerHand, cardList, bet)
    else:
        exit()
except ValueError:
    print("Please input a number only")