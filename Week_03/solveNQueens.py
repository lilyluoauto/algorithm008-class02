# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-05-01 17:22
# IDE: PyCharm
# =========================================================
class Solution:
    def solveNQueens(self, n):
        '''回溯法'''
        def could_place(row, col):
            '''判断是否能够防止queen'''
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])

        def place_queen(row, col):
            '''放置quen'''
            queens.add((row, col))
            cols[col] = 1 #标记列不能放置
            hill_diagonals[row - col] = 1 #标记主对角线不能放置
            dale_diagonals[row + col] = 1 #标记次对角线不能放置

        def remove_queen(row, col):
            '''组合不成功，进行回退'''
            queens.remove((row, col)) # 移除 row 行上的皇后
            cols[col] = 0 # 当前位置的列方向没有皇后了
            hill_diagonals[row - col] = 0 #// 当前位置的主对角线方向没有皇后了
            dale_diagonals[row + col] = 0 #当前位置的次对角线方向没有皇后了

        def add_solution():
            '设置最好的solution，赋给output'
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row=0):
            '''回溯'''
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n: #退出条件
                        add_solution()
                    else:
                        backtrack(row + 1) #回溯
                    remove_queen(row, col) #回退

        cols = [0] * n #放置queen的列
        hill_diagonals = [0] * (2 * n - 1) #主对角线
        dale_diagonals = [0] * (2 * n - 1) #次对角线
        queens = set()
        output = []
        backtrack()
        return output

so = Solution()
so.solveNQueens(4)