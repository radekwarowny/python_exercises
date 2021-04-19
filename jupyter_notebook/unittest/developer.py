from employee import Employee

class Developer(Employee):

	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)

		self.prog_lang = prog_lang

	def info(self):
		return '{} {} is using {} programming language.'.format(self.first, self.last, self.prog_lang)

		
