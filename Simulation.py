from random import*

print("Soccer Simulation\n------------------------")

stteam=input("First team")
ndteam=input("Second team")

stlevel=input("Level of First team(1~5)")
ndlevel=input("Level of Second team(1~5)")

if stlevel==1:
    stscore=randint(1,3)
    print("First team score\n"+str(stscore))
elif stlevel==2:
    stscore=randint(1,5)
    print("First team score\n"+str(stscore))
else:
    stscore=randint(1,7)
    print("First team score\n"+str(stscore))

if ndlevel==1:
    ndscore=randint(1,3)
    print("Second team score\n"+str(ndscore))
elif ndlevel==2:
    ndscore=randint(1,3)
    print("Second team score\n"+str(ndscore))
else:
    ndscore=randint(1,7)
    print("Second team score\n"+str(ndscore))

