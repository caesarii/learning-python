def inc(x):
    return x + 10

counters = [1, 2, 3, 4]

lst = list(map(inc, counters))
print(lst)