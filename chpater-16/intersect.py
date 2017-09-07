log = print

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

log(intersect('abcd', 'bcdef'))


s1 = 'abx'
s2 = 'ab'
list = [x for x in s1 if x in s2]
log(list)

# 多态
log(intersect([1, 2, 3], (1, 3)))