# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-20 20:36
# IDE: PyCharm
# =========================================================


class Solution:
    def trap_1(self, height): # 单调栈实现，这种方法要理解并且记住
        length = len(height)
        if length < 3: return 0
        res, idx = 0, 0
        stack = []
        while idx < length:
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()  # index of the last element in the stack
                if len(stack) == 0:
                    break
                h = min(height[stack[-1]], height[idx]) - height[top]
                dist = idx - stack[-1] - 1
                res += (dist * h)
            stack.append(idx)
            idx += 1
        return res

    def trap_2(self,height):
        maxHeight = max(height)
        n = 0
        m = 0
        for i in range(len(height)):
            if height[i] == 0:
                n = n+1
            else:
                break
        for j in range(len(height)):
            if height[len(height)-1-j] == 0:
                m = m+1
            else:
                break

        v1 = 1*(len(height)-n-m)
        res = 0
        for j in range(1,maxHeight):
            w = 0
            for i in range(n,(len(height)-m)):
                if height[i]>j:
                    w=w+1
            res = res+1*w
        res1 = 0
        for i in range(len(height)):
            res1=res1+height[i]
        return res+v1-res1




if __name__=="__main__":
    so =Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,3]
    area = so.trap_1(height)
    print(area)