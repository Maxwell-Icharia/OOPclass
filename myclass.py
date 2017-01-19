class Myclass(object):
	"""docstring for Myclass"""
	def __init__(self, id, name, age):
		self.id = id
		self.name = name
		self.age = age
	def nname(self):
		if name != str:
			return 'Invalid name, try again!'
	def age(self):
		if (age != int) & (age < 18):
			return 'Invalid age, try again!'
	def idd(self):
		if id in Myclass.idd:
			return 'Already exists'

class Display(Myclass):
	def get_name(self):
		return 'Name: ', name
	def get_age(self):
		return 'Age: ', age
	def get_id():
		return 'ID number: ', id
