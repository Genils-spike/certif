import tornado.web, tornado.ioloop, json, motor
from routes.users import urls

client = motor.motor_tornado.MotorClient()
db = client.test_database

def make_app():
	return tornado.web.Application(urls, db=db)

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()