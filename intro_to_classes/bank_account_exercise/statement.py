class Statement():
    def __init__(self, transaction_list):
        self.transaction_list = transaction_list
    
    # This method is doing too much - work can be delegated to a helper class
    # make more modular: StatementLine as a class to handle creating the line item
    def create(self):
        lines = []
        lines.append(["Date", "Debit", "Credit", "Balance"])
        running_balance = 0
        for tx in self.transaction_list.transactions:
            line = [tx.date]
            if tx.type == "debit":
                line.append(tx.value())
                line.append("")
            elif tx.type == "credit":
                line.append("")
                line.append(tx.value())
            running_balance += tx.value()
            line.append(running_balance)
            lines.append(line)

        return "\n".join([ " | ".join([str(col) for col in line]) for line in lines])

            
        
