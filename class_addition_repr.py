class Abc:
    def __init__(self,u):
        self.u = u
    def __str__(self):
        return str(['class string method ',self.u])

    def __repr__(self):
        return 'class representation '
    def __add__(self, other):
        print(other)
        print('addition method ',self)
        return other + self.u
obj1 = Abc('amir')
obj2 = Abc('mandeep')
obj3 = Abc('Neeraj')
# print('ui ' + obj)
print(obj1+obj2)
