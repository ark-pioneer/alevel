from transaction import Transaction

class TransactionList():
    def __init__(self, transaction_class = Transaction):
        self.transaction_class = transaction_class
        self.transactions = []
    
    def create_transaction(self, data):
        self.transactions.append(self.transaction_class(data))
    