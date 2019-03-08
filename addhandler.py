import tornado.web
from transreg import transactionregister
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self, transactions):
        self.transactions = transactions
        
    def get(self):
        name = self.get_argument('name')
        id = self.get_argument('id')
        result = self.transactions.add_transaction(name, id)
        self.write(result)
