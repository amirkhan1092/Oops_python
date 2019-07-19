class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def print_data(self):
        print('Name ', self.name, 'Pay ', self.pay)
        return None
    @staticmethod
    def independent(value):
        print('value receiving from user ', value)
        return value+34
        Employee.pay = 0


emp1 = Employee('vinay',3433)
print(emp1.independent(89))
emp1.print_data()

