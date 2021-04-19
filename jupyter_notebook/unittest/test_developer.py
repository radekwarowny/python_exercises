import unittest

from developer import Developer

class TestDeveloper(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		print('\nsetupClass')

	@classmethod
	def tearDownClass(self):
		print('\nteardownClass')

	def setUp(self):

		self.dev_1 = Developer('Radek', 'Warowny', 5000, 'Python')
		self.dev_2 = Developer('Tina', 'Reid', 8000, 'Java')

	def tearDown(self):
		pass

	def test_email(self):
		print('\nemail_test')

		self.assertEqual(self.dev_1.email, 'Radek.Warowny@company.com')

		self.dev_1.first = 'Connor'

		self.assertEqual(self.dev_1.email, 'Connor.Warowny@company.com')

	def test_info(self):
		print('\ninfo_test')

		self.assertEqual(self.dev_1.info(), 'Radek Warowny is using Python programming language.')

		self.dev_1.prog_lang = 'C#'

		self.assertEqual(self.dev_1.info(), 'Radek Warowny is using C# programming language.')

	def test_apply_raise(self):
		print('\napply_raise_test')

		self.assertEqual(self.dev_1.pay, 5000)

		self.dev_1.apply_raise()

		self.assertEqual(self.dev_1.pay, 5500)

if __name__ == '__main__':
	unittest.main()

