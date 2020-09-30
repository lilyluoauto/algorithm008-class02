学习笔记
## chainMap:
1. dict-like class for creating a single view of multiple mappings

## Dynamic programming

1. bootom to up: like the shortest path between two points
2. top to bottom:

- triangle:
    - top to bottom:
> 状态定义：dp[i][j]表示包含第i行第j列元素的最小路径和
状态分析
初始化：
dp[0][0]=triangle[0][0]
常规：
triangle[i][j]一定会经过triangle[i-1][j]或者triangle[i-1][j-1],
所以状态dp[i][j]一定等于dp[i-1][j]或者dp[i-1][j-1]的最小值+triangle[i][j]
特殊：
triangle[i][0]没有左上角 只能从triangle[i-1][j]经过
triangle[i][row[0].length]没有上面 只能从triangle[i-1][j-1]经过
转换方程：dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
-----




