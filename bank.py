
from money import ChangePool
from money import BillPool


class BankInterface():
	'''
	Interface used for creation of banks

	...

	Attributes
	==========
	change : ChangePool
		Holder for change denominations

	bills : BillPool
		Holder for bill denominations

	Methods
	=======
	TODO(parameters)
		Description
		returns ...
	'''
	def __init__(self):
		self.change = ChangePool()
		self.bills = BillPool()

	def TODO(self):
		'''
		Description		
	
			Parameters:
				name (type): description

			Returns:
				name (type): description
		'''
		pass


class Drawer(BankInterface):

	def __init__(self):
		pass

class Safe(BankInterface):

	def __init__(self):
		pass
