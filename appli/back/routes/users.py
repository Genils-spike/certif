import tornado.web, tornado.ioloop

def load_src(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))
 
load_src("controllers", "../controllers/users.py")
import controllers

urls = [
			(r"/", controllers.sign_up)
			#(r"user/signup", controllers.signup()),
			#(r"user/login", controllers.login())
		]