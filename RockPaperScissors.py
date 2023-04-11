#RockPaperScissors
from random import*

print("RockPaperScissors Game!\n--------------------------")
your=input("Rock or Scissors or Paper")

if your=="Rock":
    yournum=1
elif your=="Scissors":
    yournum=2
elif your=="Paper":
    yournum=3        

Ai=randint(1,3)
#1=Rock
#2=Scissors
#3=Paper
if Ai==1:
    print("Ai's: Rock")
elif Ai==2:
    print("Ai's: Scissors")
else:
    print("Ai's: Paper")        

score=int(Ai)-int(yournum)

if score==0:
    print("Draw!")
elif score==1:
    print("You Win!")
elif score==2:
    print("You Lose!")
elif score==-1:
    print("You Lose!")
elif score==-2:
    print("You Win!")