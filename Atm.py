bal = 0


class ATM(object):
    def __init__(self, cardNum, PIN):
        self.cardNumber = cardNum
        self.pin = PIN
        self.bal = 0

    def balance(self, cardnum):
        if(cardnum == self.cardNumber):
            print(self.bal)

    def deposit(self, cardNum, amount):
        if cardNum == self.cardNumber:
            self.bal = self.bal + amount
            print('Amount successfully deposited! Current balance: ' + self.bal)
        else:
            print('Card number is not valid!')

    def withdraw(self, cardNum, PIN, amount):
        if(self.cardNumber == cardNum and self.pin == PIN and self.balance >= amount):
            self.bal = self.bal - amount
            print('Amount withdrawn: ' + amount)
        else:
            print('Invalid card number/PIN or not enough balance!')


def main():
    cardnum = input('Please enter your card number: ')
    pin = input('Enter PIN: ')

    card = ATM(cardnum, pin)
    print('Card successfully created!')
    print('Current balance: ' + card.balance())


main()
