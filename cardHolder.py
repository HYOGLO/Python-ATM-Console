class CardHolder:
    def __init__(self, cardNum, pin, firstname, lastname, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    # Getter methods
    def get_cardNum(self):
        return self.cardNum

    def get_pin(self):
        return self.pin

    def get_firstName(self):
        return self.firstname

    def get_lastName(self):
        return self.lastname

    def get_balance(self):
        return self.balance

    # Setter methods
    def set_cardNum(self, newValue):
        self.cardNum = newValue

    def set_pin(self, newValue):
        self.pin = newValue

    def set_firstName(self, newValue):
        self.firstname = newValue

    def set_lastName(self, newValue):
        self.lastname = newValue

    def set_balance(self, newValue):
        self.balance = newValue

    # Print method
    def printout(self):
        print("Card Number:", self.cardNum)
        print("Pin Number:", self.pin)
        print("First Name:", self.firstname)
        print("Last Name:", self.lastname)
        print("Balance:", self.balance)
