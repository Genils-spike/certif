import re, bcrypt, json
from pymongo import MongoClient

client = MongoClient()
db = client['renzen']
collection = db['users']

def sign_up(data):

	###check the size of the post method###
	if len(data) < 3 and len(data) > 3 :
		return { "error" : "missing arguments"}

	###check if username is valid###
	if 'username' in data:
		username = data['username']
		#check if username is not empty
		if not username:
			return {"message" : "missing username"}

		#check username normalization
		for u in username:
			user_regx = re.compile('^[a-zA-ZÀ-ÿ0-9_.-]+$')

			if user_regx.match(u) is None:
				return {"message" : "invalid username"}

		#check username lenght
		if len(username) < 4:
			return {"mesage" : "username is too short"}

		if len(username) > 25:
			return {"mesage" : "username is too long"}

		if collection.find_one({'username' : username}) is not None:
			return {"message" : "username is already exist"}
		

	else :
		return {"message" : "missing username in the post method" }

	###check if password is valid###

	if 'password' in data:
		password = data['password']

		if not password:
			return {"message" : "missing password"}

		for u in password:
			user_regx = re.compile('^[a-zA-Z0-9]+$')

			if user_regx.match(u) is None:
				return {"message" : "invalid password"}

		if len(password) < 8:
			return {"mesage" : "password is too short"}

		if len(password) > 50:
			return {"mesage" : "password is too long"}

	else:
		return {"message" : "missing password in the post method" }

	###check if email is valid###

	if 'email' in data:
		email = data['email']

		if not email:
			return {"message" : "missing email"}

		if re.search(r'\w+@\w+\.+[a-zA-Z]', email) == None:
			return {"message" : "invalid email"}

		if collection.find_one({'email' : email}) is not None:
			return {"message" : "email is already exist"}
		
	else:
		return {"message" : "missing email in the post method" }

	password_tmp = data['password'].encode('utf-8')
	data['password'] = bcrypt.hashpw(password_tmp, bcrypt.gensalt())

	collection.insert_one(data)
	return {"message" : "user is create"}

def login(data):

	if len(data) < 2 and len(data) > 2 :
		return { "error" : "missing arguments"}

	login = data['login']
	pwd = data['password'].encode('utf-8')

	if collection.find_one({'username' : login}) is None and collection.find_one({'email' : login}) is None:
		return {'mesage' : 'invalid login'}

	else:
		user_check = collection.find_one({'username' : login})
		email_check = collection.find_one({'email' : login})
		user_pwd = ""

		if user_check is not None:
			user_pwd = user_check['password']

		if email_check is not None:
			user_pwd = user_check['password']

		user_pwd

		pwd_compare = bcrypt.checkpw(pwd, user_pwd)

		if bcrypt.checkpw(pwd, user_pwd):
			user_id = str(user_check["_id"])
			return {"user_id" : user_id}

		return {"message" : "invalid password"}
