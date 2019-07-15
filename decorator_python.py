def outer_functions(main_fun):
    def inner_function():
        print('wrapper run before main function name {}'.format(main_fun.__name__))
        return main_fun()
    return inner_function

@outer_functions
def display():
    print('this is display in main function ')


h = display()
