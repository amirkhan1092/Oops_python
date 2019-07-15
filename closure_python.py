# Python program to illustrate
# closures
# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
#
# It is a record that stores a function together with an environment: a mapping associating each free variable of
# the function (variables that are used locally, but defined in an enclosing scope) with the value or reference
# to which the name was bound when the closure was created.
# A closure—unlike a plain function—allows the function to access those captured variables through the closure’s
# copies of their values or references, even when the function is invoked outside their scope

def func():
    name = 'mandeep'
    def closure():
        print(name)
    return closure
# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
f = func()
f()
f()
f()








'''

import logging

logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
        # Necessary for closure to work (returning WITHOUT parenthesis)

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)
'''