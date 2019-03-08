import json


class transactionregister:

    def __init__(self):
        self.transactions = []

    def add_transaction(self, name, id):
        new_transaction = {}
        new_transaction["name"] = name
        new_transaction["id"] = id
        self.transactions.append(new_transaction)
        print("transaction: {0}".format(new_transaction))
        return json.dumps(new_transaction)

    def del_transaction(self, name):
        found = False
        for idx, transaction in enumerate(self.transactions):
            if transaction["name"] == name:
                index = idx
                found = True
                del self.transactions[idx]
        print("transactions: {0}".format(json.dumps(self.transactions)))
        return found

    def get_all_transactions(self):
        return self.transactions

    def json_list(self):
        return json.dumps(self.transactions)
