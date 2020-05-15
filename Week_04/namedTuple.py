# _*_coding:utf-8_*_
# author: lily luo
# date: 2020/5/15
# project: project
from collections import namedtuple

Point = namedtuple('Point',["x","y"])
p = Point(11,y=22)
print(p[0],p[1])
x,y = p
print(x,y)

