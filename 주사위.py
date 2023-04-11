#Roll the Dice!
from random import*
from time import*
go=0
while go!="q":
    go=input("Press q")
print("Start!")

for dice in range(6):
    print(int(dice))
    sleep(0.1)
for dice in range(6):
    print(int(dice))
    sleep(0.1)
for dice in range(6):
    print(int(dice))
    sleep(0.1)
for dice in range(6):
    print(int(dice))
    sleep(0.1)            

dice=randint(1,7)

dice=randint(1,7)
print("Result:'{}'!".format(dice))
sleep(2)

