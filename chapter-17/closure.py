
def maker(N):
    def action(x):
        return x ** N
    return action

print(maker(2)(3))

