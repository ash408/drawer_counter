
from collections import OrderedDict


#Defines functions for counting denominations
class PoolInterface():
	'''
	Interfaced used for creation of money pools

	...

	Attributes
	==========
	AMOUNTS : dict (str : double), constant
		key : name of denomination
		value : monitary value

	Methods
	=======
	addToPool(amount)
		add denomiations to pool based on amount (highest to lowest)
		returns remainder
	'''
	def __init__(self):
		this.AMOUNTS = OrderedDict()

	def addToPool(self, amount):
		'''
		Adds denominationes to pool based on amount (highest to lowest)
		then subtracts that amount from total, and returns the remainder.
			
			Parameters:
				amount (double): A total money amount

			Returns:
				remainder (double) : left over amount after denominations
								 are removed
		'''
		pass

	def sortDescending():
		'''
		
		'''


class ChangePool(PoolInterface):

	def __init__(self):
		this.AMOUNTS = OrderedDict({ 	('penny'   :  0.01),
			  		  			('nickel'  :  0.05),
			  		  			('dime'    :  0.1),
			  		  			('quarter' :  0.25)	})


class BillPool(PoolInterface):

	def __init__(self):
		this.AMOUNTS = OrderedDict({	('one'    :  1),
			  		  			('five'   :  5),
			  		  			('ten'    :  10),
			  		  			('twenty' :  20) }

