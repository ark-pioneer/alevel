class Transaction():
    def __init__(self, data):
        self.type = data["type"]
        self.amount = data["amount"]
        self.date = "date object"
    
    def value(self):
        if self.type == "debit":
            return -self.amount
        else:
            return self.amount
