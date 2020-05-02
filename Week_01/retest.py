# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-18 21:54
# IDE: PyCharm
# =========================================================
# !/usr/bin/python
import re

def grouptest():
    line = "Cats are smarter than dogs"

    matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

    if matchObj:
        print(
        "matchObj.group() : ", matchObj.group())
        print(
        "matchObj.group(1) : ", matchObj.group(1))
        print(
        "matchObj.group(2) : ", matchObj.group(2))
        print(
            "matchObj.group(2) : ", matchObj.groups())
    else:
        print("No match!!")




# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
str = re.match('(?P<value>\d+)',s)
print(str)
re.sub('(?P<value>\d+)',str,s)
print(re.sub('(?P<value>\d+)', double, s))