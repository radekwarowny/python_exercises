import unittest
from developer import Developer
from manager import Manager

class TestManager(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('\nsetupClass')

	@classmethod
	def tearDownClass(cls):
		print('\nteardownClass')

	def setUp(self):
		self.dev_1 = Developer('Tina', 'Reid', 400, 'Python')
		self.dev_2 = Developer('Connor', 'Heckley', 360, 'Java')

		self.mgr_1 = Manager('Radek', 'Warowny', 5000, [self.dev_1])

	def tearDown(self):
		pass

	def test_fullname(self):
		print('\ntest_fullname')
		self.assertEqual(self.mgr_1.fullname(), 'Radek Warowny')

		self.mgr_1.first = 'Connor'

		self.assertEqual(self.mgr_1.fullname(), 'Connor Warowny')

	def test_add_emp(self):
		print('\nadd_emp_test')
		self.dev_2 = Developer('Connor', 'Heckley', 360, 'Java')

		#self.assertEqual(self.mgr_1.print_emps(), '--> Tina Reid')

		self.mgr_1.add_emp(dev_2) 

		self.assertEqual(self.mgr_1.print_emps(), [dev_1, dev_2])

if __name__ == '__main__':
	unittest.main()
