import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('setupClass\n')

	@classmethod
	def tearDownClass(cls):
		print('teardownClass')

	def setUp(self):
		print('setUp')
		self.emp_1 = Employee('Radek', 'Warowny', 50000)
		self.emp_2 = Employee('Tina', 'Reid', 30000)
		
	def tearDown(self):
		print('tearDown\n')

	def test_email(self):
		print('test_email')
		self.assertEqual(self.emp_1.email, 'Radek.Warowny@company.com')
		self.assertEqual(self.emp_2.email, 'Tina.Reid@company.com')

		self.emp_1.first = 'Connor'
		self.emp_2.last = 'Heckley'

		self.assertEqual(self.emp_1.email, 'Connor.Warowny@company.com')
		self.assertEqual(self.emp_2.email, 'Tina.Heckley@company.com')

	def test_fullname(self):
		print('test_fullname\n')
		self.emp_1.first = 'Mike'
		self.emp_2.last = 'Spencer'

		self.assertEqual(self.emp_1.fullname(), 'Mike Warowny')
		self.assertEqual(self.emp_2.fullname(), 'Tina Spencer')

	def test_apply_raise(self):
		print('test_apply_raise')
		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 52000)
		self.assertEqual(self.emp_2.pay, 31200)

	def test_monthly_schedule(self):
		with patch('employee.requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'

			schedule = self.emp_1.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/Warowny/May')
			self.assertEqual(schedule, 'Success')

			mocked_get.return_value.ok = False

			schedule = self.emp_2.monthly_schedule('June')
			mocked_get.assert_called_with('http://company.com/Reid/June')
			self.assertEqual(schedule, 'Bad Response!')







if __name__ == '__main__':
	unittest.main()