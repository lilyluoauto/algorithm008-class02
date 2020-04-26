# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-20 23:17
# IDE: PyCharm
# =========================================================
import collections


class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
