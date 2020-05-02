# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-27 19:38
# IDE: PyCharm
# =========================================================
class Solution:
    def generateParenthesis(self, n: int):
        '''recursive'''

        result = []
        left,right = 0,0

        def _generateParenthesis(left,right,n,str):
            if left < n:

                _generateParenthesis(left+1,right,n,str+"(")
            if right < left:

                _generateParenthesis(left,right+1,n,str+")")
            if left == n and right == n:
                result.append(str)
                return

        _generateParenthesis(left,right,n,"")
        return result

so = Solution()
result = so.generateParenthesis(2)
print(result)







