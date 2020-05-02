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
            ans["".join(tuple(sorted(s)))].append(s)
        return list(ans.values())



if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    so = Solution()
    value = so.groupAnagrams(strs)
    print(value)
