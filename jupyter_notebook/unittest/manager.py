from employee import Employee

class Manager(Employee):

	def __init__(self, first, last, pay, employee=None):
		super().__init__(first, last, pay)
		
		if employee is None:
			self.employee = []
		else:
			self.emplyee = employee

	def add_emp(self, emp):
		if emp not in self.employee:
			self.employee.append(emp)

	def remove_emp(self, emp):
		if emp in self.employee:
			self.employee.remove(emp)

	def print_emps(self):
		for emp in self.employee:
			print('--> {}'.format(emp.fullname()))
