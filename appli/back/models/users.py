import re, bcrypt, motor

client = motor.motor_tornado.MotorClient()
db = client['renzen']

def sign_up(data):
	size = len(data)

	###check the size of the post method###
	if size < 3 or size > 3 :
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
			print(user_regx.match(u))

			if user_regx.match(u) is None:
				return {"message" : "invalid username"}

		#check username lenght
		if len(username) < 4:
			return {"mesage" : "username is too short"}

		if len(username) > 25:
			return {"mesage" : "username is too long"}

	else :
		return {"message" : "missing username in the post method" }

	###check if password is valid###

	if 'password' in data:
		password = data['password']

		if not password:
			return {"message" : "missing password"}

		for u in password:
			user_regx = re.compile('^[a-zA-Z0-9]+$')
			print(user_regx.match(u))

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

	else:
		return {"message" : "missing email in the post method" }

	password_tmp = data['password'].encode('utf-8')
	data['password'] = bcrypt.hashpw(password_tmp, bcrypt.gensalt())

	print(data['password'])
	return {"message" : "user is create"}
