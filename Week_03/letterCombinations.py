# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-05-01 16:49
# IDE: PyCharm
# =========================================================
class Solution:
    def letterCombinations(self, digits):
        '''回溯，时间和空间复杂度都是：O(3^n*4^M)'''
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        output=[]

        def backtrack(combination,next_digits):

            if len(next_digits)==0:
                output.append(combination)

            else:
                for letter in phone.get(next_digits[0]):
                    combination = combination+letter #选择
                    backtrack(combination,next_digits[1:]) #回溯，组合
                    combination = combination[0:len(combination)-1] # 回退
        if digits is not None:
            backtrack("",digits)
            return output
        else:
            return []

so = Solution()
combination = so.letterCombinations('23')
print(combination)

