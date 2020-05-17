# _*_coding:utf-8_*_
# author: lily luo
# date: 2020/5/15
# project: project

class Solution(object): #aw
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

if __name__=="__main__":
    bills = [5,10,5,20,5,5,10]
    so = Solution()
    flag = so.lemonadeChange(bills)
    print(flag)
