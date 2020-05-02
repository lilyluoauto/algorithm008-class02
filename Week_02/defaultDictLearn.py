# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-27 09:06
# IDE: PyCharm
# =========================================================
import itertools
from collections import defaultdict


def constant_factory(value):
    return itertools.repeat(value).next()

d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print('%(name)s %(action)s to %(object)s' % d)

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(d.items())