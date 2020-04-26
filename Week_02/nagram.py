# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-20 23:04
# IDE: PyCharm
# =========================================================
class Solution:
    #1. 暴力解法：直接排序，比对字符是否相等,56ms
    def isAnagram_1(self, s, t) -> bool:
        return True if sorted(s) == sorted(t) else False


if __name__ == "__main__":
    so = Solution()
    s = 'a'
    t = 'b'
    flag = so.isAnagram_1(s,t)
    print(flag)

