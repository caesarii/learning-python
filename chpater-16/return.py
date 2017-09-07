log = print


def foo():
    a = 1

print(foo())

otherFoo = foo
log(otherFoo())

foo.name = "lala"
log(foo.name)