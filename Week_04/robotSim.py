# _*_coding:utf-8_*_
# author: lily luo
# date: 2020/5/15
# project: project

class Solution:
    def robotSim(self, commands, obstacles) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  # left
                di = (di - 1) % 4
            elif cmd == -1:  # right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x * x + y * y)

        return ans
so = Solution()
commands = [4,-1,3]
obstacles = []
ans = so.robotSim(commands,obstacles)
print(ans)