from random import*
Joiner=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(Joiner)
Chiken=(sample(Joiner,1))
Coffee=(sample(Joiner,3))
print("------당첨자 발표------")
print("치킨 당첨자: "+str(Chiken))
print("커피 당첨자: "+str(Coffee))
print("------축하합니다!------")