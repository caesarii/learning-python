class Foo():
    name = 'qinhge'
    def getName(self):
        return self.name

f = Foo()
print(Foo.name)
print(f.getName())
print(f.name)
f.name = 'caesar'
print(Foo.name)
print(f.getName())
print(f.name)

