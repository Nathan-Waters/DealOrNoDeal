#Nathan Waters
#final project
#Deal or no deal

#function that will take the averages of whats left and offer a deal
def banker(caseAvg):
  caseAvg = sum(caseValues)/len(caseValues)

  AvgRound = round(caseAvg, 2)

  print("The banker is willing to pay you", AvgRound,"dollars\n Deal?... or No Deal!")

  return AvgRound

#time commented out for troubleshooting speed
import time
import random

#creat list and randomized 
originalCase = []
caseValues = [0.01, 1, 5, 10, 25, 50, 100, 250, 500, 1000]
caseValuesUsed = []
#reserch for this was from https://pynative.com/python-random-shuffle/
random.shuffle(caseValues)

#rules of the game
print("Hello and welcome to Deal or No deal.")
print("The rules are as follows:\n")
time.sleep(1)
print("First you will choose your original case\nfrom a list list of 10 options.\n(choosing 0 thru 9)\n")
time.sleep(1)
print("Then if you want to pull another case type -1 or 0.\n")
time.sleep(1)
print("After you choose another case the banker will\noffer you a deal to sell your original case\nbased on what you have revealed so far.\n")
time.sleep(1)
print("Should you choose to turn down all of banks offers\nyou will recieve the value of your original choice.\n")
time.sleep(3)
print("Now lets play deal or no deal!\n")

casesLeft = 9

#users choice of cases
while casesLeft != 0:
  if casesLeft == 9:

    UserInput = int(input("which case would you like ot start with!\nChoose between 0 and 9\n:"))
    originalCase.insert(UserInput, caseValues.pop(UserInput))
    casesLeft = casesLeft - 1
    print("Now that you have chosen the game can start!")

#after user picks the first case
  if casesLeft <= 8:
    UserInput2 = int(input("please enter 0 to choose another case\n:"))
    caseValuesUsed.insert(UserInput, caseValues.pop(UserInput))
    casesLeft = casesLeft - 1

    banker(caseValues)

  UserInput3 = int((input("1 = Deal, 2 = No Deal\n:")))

  dealAmmount = sum(caseValues)/len(caseValues)
  finalTake = round(dealAmmount, 2)

  if UserInput3 == 1:
    print("we have a deal!\nCongratulations you have won", finalTake, "dollars")
    break
  if UserInput3 == 2:
    print("We are on to another round!\n")

  # print(caseValuesUsed)

finalAmmount = sum(originalCase)
if casesLeft == 0:
  print("Well that only leaves us with one case left")
  print("You will be leaving here with", finalAmmount, "dollars")
