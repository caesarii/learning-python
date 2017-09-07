def tet(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

f = tet(0)
# f("a")
# f("b")

# def tet2(start):
#     def nested(label):
#         # 不能声明
#         nonlocal state
#         print(label, state)
#         state = 1
#     return nested
# tet2(1)

state = 1
def tet3():
    # 只用于 嵌套函数
    nonlocal state
    state = 2
    return state

tet3()

