
class FirstClass:
    def setData(self, value):
        self.data = value
    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()

x.setData('caesar')
x.display()

x.data = 'new name'
x.display()

y.setData('qinhge')
y.display()


class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)


z = SecondClass()
z.setData("sdjfkl")
z.display()