import functools

h = [1,2,3,4,5,6]

s = functools.reduce(lambda a, b:a*b,h)
print(s)