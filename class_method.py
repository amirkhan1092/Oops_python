class Employee:

    def __init__(self, pay, age):
        self.pay = pay
        self.age = age

    def update(self):
        self.pay = 2000
        self.age = 24

    @classmethod
    def from_string(cls,s):
        pay, age = s.split()
        return cls(pay,age)

    @classmethod
    def common_clear(cls):
        cls.pay = 0
        cls.age = 0
        return cls


em1 = Employee(2000, 24)
# em2 = Employee(1000, 25)
em2 = Employee.from_string('1000 25')

print(em1.age)
print(em2.age)

Employee.common_clear()

print(Employee.age)
print(em2.age)