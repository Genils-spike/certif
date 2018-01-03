import tornado.web, tornado.ioloop

class hello_world(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello, world")

class hello_world_ki(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello, world 2 the coumback")

def make_app():
	return tornado.web.Application([
		(r"/", hello_world),
	])

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()