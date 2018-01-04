from mongoengine import *

class sign_up(Document):
	username = StringField(max_length=200, required=True)
	password = StringField(max_length=200, required=True)
	email = EmailField(max_length=200, required=True)