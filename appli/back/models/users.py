import re

def sign_up(data):
	size = len(data)

	#check the size of the post method
	if size < 3 or size > 3 :
		return { "error" : "missing arguments"}

	#check if username exist
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

	#check if password exist
	if 'password' in data:
		password = data['password']


	else:
		return {"message" : "missing password in the post method" }
	return {"message" : "sucess"}
