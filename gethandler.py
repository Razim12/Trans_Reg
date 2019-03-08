import tornado.web
from transreg import transactionregister
import json


class GetHandler(tornado.web.RequestHandler):
    def initialize(self, transactions):
        self.transactions = transactions
        
    def get(self):
        self.write(self.transactions.json_list())
