# _*_coding:utf-8_*_
# author: lily luo
# date: 2020/5/15
# project: project

class Solution:
    def findContentChildren(self, g, s):
        '''208ms, 很慢，需要优化,进行优化'''

        #判断g or s 是否为0：
        if len(g) == 0 or len(s) == 0:
            return 0
        # sorting g and s
        g.sort()
        s.sort()
        if s[-1]<g[0]:
            return 0
        i,j = 0,0
        count = 0
        while i <len(g) and j <len(s):
            if g[i] <= s[j]:
                i = i+1
                count +=1
                s[j] =0
            j = j+1
        return count

g = [10,9,8,7]
s = [5,6,7,8]

so = Solution()
count = so.findContentChildren(g,s)
print (count)


