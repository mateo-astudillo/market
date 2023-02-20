

class User:
	def __init__(self, username:str, password:str):
		self.username = username
		self.password = password # hashed

		self.id: int = None
		
		self.name:str = None
		self.surname:str = None
		self.age:int = None
