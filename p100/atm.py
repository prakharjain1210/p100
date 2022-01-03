class Atm(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber

    def checkBalance(self):
        print("your balance is ₹50000")

    def withdrawl(self, amount):
        remaining=50000-amount
        print("you have withdrawn: "+ str(amount)+ "your balacne is: " + str(remaining))

def main():
    cn=input("enter your card number : ")
    pn=input("enter your pin number : ")
    prakhar= Atm(cn,pn)
    print("choose one option:1. balance enquiry  2. withdrawl")
    act=int(input("enter your choice"))
    if(act==1):
        prakhar.checkBalance()
    elif(act==2):
        amount=int(input("enter your amount : "))
        prakhar.withdrawl(amount)

main()