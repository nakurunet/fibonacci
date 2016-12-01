import unittest
from fib import fibonaci

class PrimeTests(unittest.TestCase):
	
	def test_input_must_not_be_float(self):
		self.assertEqual(fibonaci(10.5),"The number must be a whole number")
	
	def test_no_string(self):
		self.assertEqual(fibonaci("a"), "Cannot allow letters")

	def test_no_list(self):
		self.assertEqual(fibonaci([24]), "Cannot allow lists")
	
	def test_input_must_not_be_a_tuple(self):
		self.assertEqual(fibonaci((100)),"The number must be a whole number")
	
	def test_not_big_integer(self):
		self.assertTrue(fibonaci(isPrime>1000),'large numbers not allowed!!!')
	
	def test_input_must_not_be_a_boolean(self):
		self.assertEqual(fibonaci(True),"The number must not be a boolean")

if __name__ == 'main':
	unittest.main()
