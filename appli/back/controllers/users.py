import tornado.web, json, re

def load_src(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))
 
load_src("user_model", "../models/users.py")
import user_model

class sign_up(tornado.web.RequestHandler):
    def post(self):
        test = json.loads(self.request.body)

        self.write(user_model.sign_up(test))

