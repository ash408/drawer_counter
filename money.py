
#Defines functions for counting denominations
class DenominationInterface():

	def __init__(self):
		pass


class Change(DenominationInterface):

	def __init__(self):
		this.AMOUNTS = { 'penny'   :  0.01,
			  		  'nickel'  :  0.05,
			  		  'dime'    :  0.1,
			  		  'quarter' :  0.25 }


class Bills(DenominationInterface):

	def __init__(self):
		this.AMOUNTS = { 'one'    :  1,
			  		  'five'   :  5,
			  		  'ten'    :  10,
			  		  'twenty' :  20 }

