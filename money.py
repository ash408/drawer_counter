
from collections import OrderedDict


class PoolInterface():
	'''
	Interfaced used for creation of money pools


	Attributes
	==========
	VALUES : OrderedDict (str : double), constant
		key : name of denomination
		value : monitary value

	amounts : dict (str : int)
		key : name of denomination
		value : number of denomination in pool

	Methods
	=======
	addToPool(amount)
		add denomiations to pool based on amount (highest to lowest)
		returns remainder

	removeFromPool(amount)
		remove denominations from pool based on amount (highest to lowest)
		returns remainder

	addDenominations(denominations)
		add denominations to pool based on dictionary of denominations
		returns dictionary with remainder

	removeDenominations(denominations)
		remove denominations from pool based on dictionary of denominations
		returns dictionary with remainder
	'''
	def __init__(self, values):
		self.VALUES = values
		
		amounts = {}
		for denomination in list(values.keys()):
			amounts[denomination] = 0

		self.amounts = amounts

	def addToPool(self, amount):
		'''
		Adds denominations to pool based on amount (highest to lowest)
		then subtracts that amount from total, and returns the remainder.
			
			Parameters:
				amount (double): A total money amount

			Returns:
				remainder (double): left over amount after denominations
								 are removed
		'''
		pass

	def removeFromPool(self, amount):
		'''
		Removes denominations from pool based on amount (highest to lowest)
		then subtracts that amount from total, and returns the remainder.

			Parameters:
				amount (double): A total money amount

			Returns:
				remainder (double): left over amount after denominations
								are removed
		'''
		pass

	def addDenominations(denominations):
		'''
		Adds denominations to pool based on dictionary, removing
		denominations from said dictionary and returning the remainder.

			Parameters:
				denominations : dict (str : int)
					key : name on denomination
					value : number to add

			Returns:
				denominations : dict (str : int)
					key : name of denomination
					value : number to add
		'''
		pass

	def removeDenominations(denominations):
		'''
		Removes denominations from pool based on dictionary, removing
		denominations from said dictionary and returning the remainder.

			Parameters:
				denominations : dict (str : int)
					key : name on denomination
					value : number to remove

			Returns:
				denominations : dict (str : int)
					key : name of denomination
					value : number to remove
		'''
		pass


class ChangePool(PoolInterface):

	def __init__(self):
		this.VALUES = OrderedDict([ 	('penny',	  	0.01),
			  		  			('nickel',  	0.05),
			  		  			('dime',	 	0.10),
			  		  			('quarter',  	0.25),
								('half',		0.50),
								('dollar',	1.00) ])


class BillPool(PoolInterface):

	def __init__(self):
		this.VALUES = OrderedDict([	('one',		1),
								('two',		2),
			  		  			('five',   	5),
			  		  			('ten',  		10),
			  		  			('twenty',  	20),
								('fifty',  	50),
								('hundred', 	100) ])

