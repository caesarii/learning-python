

def func():
    x = 'xxx'
    def nested():
        nonlocal x
        x = 'spam'
    nested()
    print(x)
func()
