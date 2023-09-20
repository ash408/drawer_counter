
from collections import OrderedDict


class PoolAbstract():

	'''
	Abstract used for creation of money pools


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

		#iterate through denominations and values
		for denomination, value in self.VALUES.items():
			#divide amount by denom and add to amounts
			add_to_denom = amount / value
			number_of_denom = self.amounts[denomination]

			self.amounts[denomination] = number_of_denom + add_to_denom
			
			amount = amount % value
			
			if amount == 0:
				break;

		return amount

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


class ChangePool(PoolAbstract):

	def __init__(self):
		VALUES = OrderedDict([ 	('penny',	  	0.01),
			  		  		('nickel',  	0.05),
			  		  		('dime',	 	0.10),
			  		  		('quarter',  	0.25),
							('half',		0.50),
							('dollar',	1.00) ])
		super(VALUES)


class BillPool(PoolAbstract):

	def __init__(self):
		VALUES = OrderedDict([	('one',		1),
							('two',		2),
			  		  		('five',   	5),
			  		  		('ten',  		10),
			  		  		('twenty',  	20),
							('fifty',  	50),
							('hundred', 	100) ])
		super(VALUES)

