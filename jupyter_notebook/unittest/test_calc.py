import unittest
import radek

class TestCalc(unittest.TestCase):

	def test_add(self):
		self.assertEqual(radek.add(10, 5), 15)
		self.assertEqual(radek.add(-1, 1), 0)
		self.assertEqual(radek.add(-2, -2), -4)

	def test_sub(self):
		self.assertEqual(radek.sub(10, 5), 5)
		self.assertEqual(radek.sub(-1, 1), -2)
		self.assertEqual(radek.sub(-2, -2), 0)

	def test_mult(self): 
		self.assertEqual(radek.mult(10, 5), 50)
		self.assertEqual(radek.mult(-1, 1), -1)
		self.assertEqual(radek.mult(-2, -2), 4)

	def test_div(self):
		self.assertEqual(radek.div(10, 5), 2)
		self.assertEqual(radek.div(-1, 1), -1)
		self.assertEqual(radek.div(3, 3), 1)
		self.assertEqual(radek.div(5, 2), 2.5)

		self.assertRaises(ValueError, radek.div, 10, 0)


if __name__ == '__main__':
	unittest.main()