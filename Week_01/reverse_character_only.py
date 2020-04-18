# coding:utf8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-18 08:59
# IDE: PyCharm
# =========================================================
from collections import deque


def reverseOnlyLetters(S):
    """
    :type S: str
    :rtype: str
    """
    # strlist=list(S)
    # i=0
    # j=len(S)-1
    # while i!=j:
    #     if (65 <= ord(strlist[i]) <= 122) and (65 <= ord(strlist[j]) <= 122):
    #         a = strlist[i]
    #         # S.replace(S[i], S[j], 1)
    #         # S.replace(S[j], a, 1)
    #         strlist[i] = strlist[j]
    #         strlist[j] = a
    #         i = i + 1
    #         j = j - 1
    #         continue
    #     if ord(strlist[i])< 65 or ord(strlist[i])>122:
    #         i = i +1
    #     if ord(strlist[j])<65 or ord(strlist[j])>122:
    #         j=j-1
    # str1 = "".join(strlist)
    # S = str1
    # print(S)
    #1. 记录非字符的位置和值。变成list进行操作，删除非字符，反序，插入记录的非字符，
    #用时40MS 比较慢。可能是插入的时候比较慢引起的。判读非字符很笨，可进一步优化
    # l = {}
    # s = u"abcdefghijklmnopqrstuvwxyz"
    # s = s+s.upper()
    # print(s)
    # strlist = list(S)
    # for idx,val in enumerate(S):
    #     if val not in s:
    #         l[idx]= val
    # n=len(strlist)
    # i=0
    # while i < n:
    #     if strlist[i] not in s:
    #         del strlist[i]
    #         i = i -1
    #         n = n -1
    #     i = i +1
    # strlist = strlist[::-1]
    # for i in l.keys():
    #     strlist.insert(i,l[i])
    # str1 = "".join(strlist)
    # return str1

    # 2. 记录非字符的位置和值。变成list进行操作，删除非字符，反序，插入记录的非字符，
    # 用时40MS 比较慢。可能是插入的时候比较慢引起的。判读非字符很笨，进一步优化如下
    # 优化之后36MS
    # l={}
    # strlist = list(S)
    # for idx,val in enumerate(S):
    #     if not val.isalpha():
    #         l[idx]= val
    # n=len(strlist)
    # i=0
    # while i < n:
    #     if not strlist[i].isalpha():
    #         del strlist[i]
    #         i = i -1
    #         n = n -1
    #     i = i +1
    # strlist = strlist[::-1]
    # for i in l.keys():
    #     strlist.insert(i,l[i])
    # str1 = "".join(strlist)
    # print(str1)
    # return str1


    #3. 用deque 来做,是deque空数组,pop 弹出，先进后出，代码漂亮了很多,少了插入的操作，代码
    #快了很多，32ms
    # str1= deque(c for c in S if c.isalpha())
    # ans = []
    # for val in S:
    #     if val.isalpha():
    #         ans.append(str1.pop())
    #     else:
    #         ans.append(val)
    # print("".join(ans))


s = "Test1ng-Leet=code-Q!"
reverseOnlyLetters(s)

