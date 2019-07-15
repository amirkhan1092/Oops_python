def decorator_function(main_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(main_func.__name__),level=logging.INFO)
    def wrapper_function(*argv,**kwargs):
        logging.info(
            'run with argv : {} and kwargv :  {}'. format(argv,kwargs)
        )
        return main_func(*argv,**kwargs)

    return wrapper_function


@decorator_function
def add(a,b):
    print('addition of two number ')
    return a+b

f = add(3,5)
print(f)
