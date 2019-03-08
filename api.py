import tornado.ioloop
import tornado.web
from transreg import transactionregister
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler

transactions = transactionregister()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("transaction Microservice v1")

def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addtransreg", AddHandler, dict(transactions = transactions)),
        (r"/v1/deltransreg", DelHandler, dict(transactions = transactions)),
        (r"/v1/gettransactions", GetHandler, dict(transactions = transactions)),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
