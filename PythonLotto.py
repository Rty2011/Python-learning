from random import*

print("-Python Lotto-\n----------------------------------")

mode=input("Select 'Auto' or 'Self'")

if mode=="Auto":
    num=randint(1,45)
    print("Your number is {0}.".format(num))
elif mode=="Self":
    num=input("Your number(1~45)")
else:
    print("Error")
    wrwerwerwedsfc

Ainum=randint(1,45)
print("Ai's number: {0}\nYour number: {1}".format(Ainum,num))
if Ainum==num:
    print("You Win!")
elif Ainum!=num:
    print("You Lose!")   