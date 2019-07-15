
class decorator_class:
    def __init__(self,function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # print('wrapper before the main method {}'. format(self.function.__name__))
        print('wrapper before the main method {}'.format(self.function))
        return self.function()



# print(decorator_class('hello')())

#
@decorator_class
def add():
    print('this is addition ')

# f = decorator_class(add)
# f()

add()

'''

def outer_functions(main_fun):
    def inner_function():
        print('wrapper run before main function name {}'.format(main_fun.__name__))
        return main_fun()
    return inner_function


@outer_functions
def display():
    print('this is display in main function ')

# f = outer_functions(display)
# f()
display()



'''

