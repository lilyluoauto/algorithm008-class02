# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-29 19:46
# IDE: PyCharm
# =========================================================
from collections import Counter
from itertools import combinations_with_replacement

com = combinations_with_replacement('ABC', 2)
print(com)
for item in com:
    print(''.join(item))
s = map(Counter, combinations_with_replacement('ABC', 2))

c = Counter([1,1,2,3,4,4,5,2,2,2,2,2])
print(c)
print(max(c.keys(),key=c.get))
print(c.get)

d = {2: 6, 1: 2, 4: 2, 3: 1, 5: 1}
print(max(d.keys(),key=d.get))
