from transaction_list import TransactionList

class Account():
    def __init__(self, transaction_list_class = TransactionList):
        self.transaction_list = transaction_list_class()
    
    def new_transaction(self, tx_data):
        self.transaction_list.create_transaction(tx_data)