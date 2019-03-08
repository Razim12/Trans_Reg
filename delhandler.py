import tornado.web
from transreg import transactionregister
import json


class DelHandler(tornado.web.RequestHandler):
    def initialize(self, transactions):
        self.transactions = transactions
        
    def get(self):
        name = self.get_argument('name')
        result = self.transactions.del_transaction(name)
        if result:
            self.write("Deleted transaction name: {0} successfully".format(name))
            self.set_status(200)
        else:
            self.write("transactionregister '{0}' not found".format(name))
            self.set_status(404)
