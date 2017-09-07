log = print
x = 99
def func():
    x = 88
    return x
log(x)
log(func())
