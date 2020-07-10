# _*_coding:utf-8_*_
# author: lily luo
# date: 2020/5/15
# project: project

class Solution:
    def maxProfit_1(self, prices):

        profit = 0
        for i in range(len(prices)-1):
            tmp = prices[i+1]-prices[i]
            if tmp>0:
                profit += tmp
        print(profit)
        return profit

    def maxProfit_2(self,prices):
        '''动态规划'''


so = Solution()
prices = [1,3,5,2,6,9,1]
so.maxProfit_1(prices)

