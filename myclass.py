class Myclass(object):
	"""docstring for Myclass"""
	def __init__(self, arg):
		super(Myclass, self).__init__()
		self.arg = arg
		number = 0
		name = "noname"
def Main():
	me = Myclass()
	me.name = "Draps"
	me.number = 4


	friend = Myclass()
	friend.name = "Steve"
	friend.number = 6


	print "Name: " + me.name ", Favorite Number: " + str(me.number)
	print "Name: " + friend.name ", Favorite Number: " + str(friend.number)


if __name__=='__main__':
	Main()