# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-19 08:59
# IDE: PyCharm
# =========================================================
class Solution:
    def firstUniqChar(self, s: str) -> str:
        ##1. dict 的使用
        # dic = {}
        # for c in s:
        #     dic[c] = not c in dic
        # for c in s:
        #     if dic[c]: return c
        # return ' '
        ##2. 统计 字符出现的次数，可以考虑利用spark进行mapreduce？
        dict = {}
        for c in s:
            if c in dict:
                dict[c] = dict[c]+1
            else:
                dict[c] = 1
        for k,v in dict.items():
            if v == 1: return k
        return " "


so = Solution()
s = "abaccdeff"
flag = so.firstUniqChar(s)
print(flag)