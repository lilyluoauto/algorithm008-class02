# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-16 14:05
# IDE: PyCharm
# =========================================================

import heapq
class heapq_op():

    def create_q(self,L):
        l=[]
        for item in L:
            heapq.heappush(l,item)
        return l

    def get_values(self,l,n=None):

        if n == None or n > len(l):
            n = len(l)
        out = [heapq.heappop(l) for i in range(n)]
        return out


if __name__=="__main__":
    l=[1,3,5,7,6,5,3]

    h_op = heapq_op()
    iterable = h_op.create_q(l)
    print(iterable)
    out = h_op.get_values(iterable,5)
    print(iterable)
    heapq.heappushpop(iterable,9)
    out = heapq.heappushpop(iterable, 4)

    print(out)
    l_1 = [ 5,9,7]
    l_2 = list(heapq.merge(l,l_1))
    print(l_2)
    out = heapq.nlargest(3,l_2)
    print(out)
    print(l_2)
    out = heapq.nsmallest(2,l_2)
    print(out)
    print(l_2)


