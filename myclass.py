class Myclass(object):
	"""docstring for Myclass"""
	def __init__(self, arg):
		super(Myclass, self).__init__()
		self.arg = arg
		id = 0
		name = "noname"
		colour = ''
	def Main():
		me = Myclass()
		me.name = 'Max'
		me.id = 4
		me.colour = 'Brown'

		friend = Myclass()
		friend.name = "Steve"
		friend.id = 6
		friend.colour = 'Grey'


if __name__=='__main__':
	Main()