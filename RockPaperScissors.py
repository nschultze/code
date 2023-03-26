import random

gameReady = input("Type Y if you are ready to play: ")
userInput = input("Type Rock, Paper, or Scissors: ")

randomNumber = random.randint(0, 2)
if(randomNumber == 0):
    computerInput = "Rock"
elif(randomNumber == 1):
    computerInput = "Paper"
elif(randomNumber == 2):
    computerInput = "Scissors"
print("The computer choose: ", computerInput)

if((userInput == 'Rock') and (computerInput == 'Rock')):
    print("Draw")
elif((userInput == 'Paper') and (computerInput == 'Paper')):
    print("Draw")
elif((userInput == 'Scissors') and (computerInput == 'Scissors')):
    print("Draw")
elif((userInput == 'Rock') and (computerInput == 'Paper')):
    print("You Lose")
elif((userInput == 'Rock') and (computerInput == 'Scissors')):
    print("You Win")
elif((userInput == 'Paper') and (computerInput == 'Rock')):
    print("You Win")
elif((userInput == 'Paper') and (computerInput == 'Scissors')):
    print("You Lose")
elif((userInput == 'Scissors') and (computerInput == 'Rock')):
    print("You Lose")
elif((userInput == 'Scissors') and (computerInput == 'Paper')):
    print("You Win")
