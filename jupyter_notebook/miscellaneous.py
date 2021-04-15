#!/usr/bin/env python
# coding: utf-8

# In[258]:


class Employee:
    
    num_of_emp = 0
    raise_amount = 1.04
    
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emp += 1
        
    def full_name(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        


# In[380]:


class Vehicle:
    
    veh_no = 0
    
    veh_tax = 1.05
    veh_disc = 0.95
    
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
        
        Vehicle.veh_no += 1
        
    def info(self):
        return "\nModel: {}\nYear: {}\nPrice: {}".format(self.model, self.year, self.price)
    
    def with_tax(self):
        return "\nModel: {}\nYear: {}\nPrice: + tax {}".format(self.model, self.year, (self.price * self.veh_tax))
    
    def apply_discount(self):
        disc_price = (self.price * self.veh_tax) * self.veh_disc
        return self.with_tax() + '\nDISCOUNTED TO: {}'.format(int(disc_price))
    
    @classmethod
    def set_tax(cls, amount):
        cls.veh_tax = amount
        
    @classmethod
    def from_string(cls, car_str):
        model, year, price = car_str.split('-')
        return cls(model, year, int(price))
    
    @staticmethod
    def is_thursday(day):
        if day.weekday() == 3:
            return True
        return False
        
        


# In[388]:


import datetime
my_date = datetime.datetime.now()


# In[389]:


car1_str = "Alfa Romeo 155-1992 to 1997-191949"
car2_str = "Alfa Romeo 156-1997 to 2005-680000"
car3_str = "Alfa Romeo Alfasud-1972 to 1989-1017387"


# In[390]:


car1 = Vehicle.from_string(car1_str)
car2 = Vehicle.from_string(car2_str)
car3 = Vehicle.from_string(car3_str)


# In[391]:


print(car1.info())


# In[392]:


print(car1.with_tax())


# In[393]:


print(car1.apply_discount())


# In[394]:


Vehicle.is_thursday(my_date)


# In[467]:


class Employee:
    
    emp_no = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
        Employee.emp_no += 1
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_amt
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount 
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
    


# In[468]:


emp1 = Employee("Radek", "Warowny", 50000)
emp2 = Employee("Tina", "Reid", 60000)


# In[469]:


print(emp1.fullname())
print(emp2.fullname())


# In[448]:


emp1.first = "Connor"


# In[449]:


print(emp1.fullname())


# In[450]:


emp2.apply_raise()


# In[451]:


emp2.pay


# In[452]:


Employee.set_raise_amt(0.5)


# In[453]:


emp2.pay


# In[454]:


emp2.apply_raise()


# In[455]:


emp2.pay


# In[456]:


emp1.pay


# In[457]:


emp1_str = "Radek-Warowny-50000"


# In[458]:


emp1 = Employee.from_string(emp1_str)


# In[459]:


emp1.first


# In[470]:


import datetime
my_date = datetime.datetime(2020,12,12)


# In[471]:


Employee.is_weekday(my_date)


# In[ ]:

#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
emp_1 = Employee('Radek', 'Warowny', 50000)
emp_2 = Employee('Tina', 'Reid', 60000)

print(emp_1.email)
print(emp_2.email)


# In[29]:


class Developer(Employee): # Developer class inherits from Employee class
    raise_amount = 1.10 # changing attribute only for Developer class
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None: 
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees: 
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('--> ' + emp.fullname())

dev_1 = Developer('Connor', 'Heckley', 30000, 'Python')
dev_2 = Developer('Darren', 'Brown', 39000, 'Java')

print(dev_1.email) # attributes inherited from Employee class
print(dev_2.email)
print()
print(dev_1.pay)
print(dev_2.pay)
dev_1.apply_raise()
dev_2.apply_raise()
print()
print("Pay after raise: {}".format(dev_1.pay))
print("Pay after raise: {}".format(dev_2.pay))
print()
print(dev_1.email)
print(dev_1.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
print(mgr_1.print_emps())
mgr_1.add_emp(dev_2)
print(mgr_1.print_emps())
mgr_1.remove_emp(dev_1)
print(mgr_1.print_emps())

print(isinstance(mgr_1, Manager)) # true
print(isinstance(mgr_1, Employee)) # true
print(isinstance(mgr_1, Developer)) # false
print(issubclass(Developer, Employee)) # true
print(issubclass(Manager, Developer)) # false


# In[6]:


# print(help(Developer)) # help method shows how attributes and methods are inherited


#!/usr/bin/env python
# coding: utf-8

# In[118]:


class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)


# In[119]:


emp_1 = Employee('Radek', 'Warowny', 50000) 


# In[120]:


emp_1.__repr__()


# In[121]:


emp_1.__str__()


# In[122]:


class Developer(Employee):
    
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        
    def __repr__(self):
        return "Developer({}, {}, {}, {})".format(self.first, self.last, self.pay, self.prog_lang)


# In[123]:


dev_1 = Developer('Tina', 'Reid', 50000, 'Python')


# In[124]:


dev_1.email


# In[125]:


dev_1.__repr__()


# In[126]:


dev_1.__str__()


# In[133]:


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        
        if employees is None:
            self.employees = []
        else: 
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('--> {}'.format(emp.fullname()))
            
    def __repr__(self):
        return 'Manager({}, {}, {}, {})'.format(self.first, self.last, self.pay, self.employees)
    
    def __str__(self):
        return '{} - {} - {}'.format(self.fullname(), self.email, self.employees)
            


# In[134]:


mgr_1 = Manager('Sue', 'Smith', 80000, [dev_1])


# In[135]:


mgr_1.email


# In[136]:


print(mgr_1.__repr__())


# In[137]:


print(mgr_1.__str__())


# In[ ]:











