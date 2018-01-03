import tornado.web, tornado.ioloop
import json

class hello_world(tornado.web.RequestHandler):
	def post(self):
		reponse_obj = {
			"status" : "success",
			"message" : "hello world"
		}
		self.write(json.dumps(reponse_obj))
	get = post

def make_app():
	return tornado.web.Application([
		(r"/", hello_world),
	])

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()