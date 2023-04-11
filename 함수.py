def goal():
    print("골!!!")

goal()    

def deposit(balance,money):
    print("{0}골이 추가 되었습니다! 총 {1}골입니다".format(money,balance+money))
    return balance+money

balance=0
balance=deposit(balance,2)

def withdraw(balance,money):
    print("{0}골이 취소되었습니다. 총{1}골입니다".format(money,balance-money))
    return balance-money


balance=2
balance=withdraw(balance,1)