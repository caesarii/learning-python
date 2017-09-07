# length
print(len([1, 2, 3]))

# 合并
print([1, 2, 3] + [3, 4, 5])

# 重复
print([1, 2, 3] * 3)

# 成员关系
print(3 in [1, 3])

# 迭代
for x in [1, 2, 3]:
    print(x)

# 解析
print([x * 3 for x in [1, 3, 4]])

# 索引赋值
lst = [0, 1, 2, 3]
lst[0] = ['a', "b"]
print(lst)

lst[0:1] = [0, 0]
print(lst)

lst.extend(['a', 'b'])
print(lst)
