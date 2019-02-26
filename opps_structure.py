'''
# class and instance of class
class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

print(emp1) # having different - different location
print(emp2)

# instance variable : Instance variable is the data that is unique for the instance

emp1.name='amar'
emp1.pay=32334
emp1.email='amar@gmail.com'

emp2.name='anthony'
emp2.pay=4243
emp2.email='anthony@gmail.com'

print(emp1.email)
print(emp2.email)

# we want automatically make instance
class Employee:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
        self.email=name + '@gmail.com'

emp1=Employee('amar', 34233)
emp2=Employee('anthony',4354 )

print(emp1.email)
print(emp2.email)

# using method
class Employee:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay

    def email(self):
        return self.name + '@gmail.com'


emp1=Employee('amir',100)
print(emp1.email())
print(Employee.email(emp1  ))
'''
# class variable and instance variable
class Employee:
    raise_amount=10
    def __init__(self,name,pay):
        self.pay=pay
        self.name=name

    def raisepay(self):
        self.pay=int(self.pay*self.raise_amount)

# instance
emp1 = Employee('Ravi',323)
emp2 = Employee('Mandeep',433)



emp1.raisepay()
print(emp1.pay)

Employee.raise_amount=43

print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

