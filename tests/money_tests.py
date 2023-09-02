
import unittest

from ..money import PoolInterface

class TestPoolInterface(unittest.TestCase):

	def test_interface_initialization (self):
		VALUES = OrderedDict([('a' : 0.1), ('b', 0.5)])

		interface = PoolInterface(VALUES)

		self.assertEqual(interface.VALUES['a'], 0.1)
		self.assertEqual(interface.VALUES['b'], 0.5)

		self.assertEqual(interface.amounts['a'], 0)
		self.assertEqual(interface.amounts['b'], 0)


if __name__ == '__main__':
	unittest.main()
