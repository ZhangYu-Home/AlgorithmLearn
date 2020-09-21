#求解0-1背包问题的函数：二维表的实现方式
#形参:
# n为整型，表示物品种类数；
# c为整型，表示背包容量；
# w为列表，表示每个物品的重量；
# V为列表，表示每个物品的价值；
# def backpack_0_1(n, c, w, v):
#     dp = [[0 for j in range(n+1)] for i in range(c+1)]

#     for i in range(1,c+1):
#         for j in range(1,n+1):
#             if i < w[j-1]:
#                 dp[i][j] = dp[i][j-1]
#             else:
#                 dp[i][j] = max(dp[i][j-1], dp[i-w[j-1]][j-1]+v[j-1])
#     return dp[c][n]

#求解0-1背包问题的函数：一维表的实现方式
#形参:
# n为整型，表示物品种类数；
# c为整型，表示背包容量；
# w为列表，表示每个物品的重量；
# V为列表，表示每个物品的价值；
def backpack_0_1(n, c, w, v):
    dp = [0 for i in range(c+1)]
    for i in range(1,c+1):
        for j in range(n):
            # if i < w[j]:
            #     dp[i] = max(dp[i-1], dp[i])
            # else:
            #     dp[i] = max(dp[i-1],dp[i-w[j]]+v[j])
            if i > w[j]:
                dp[i] = max(dp[i-1],dp[i-w[j]]+v[j])
    print(w)
    print(v)

    print(dp)
    return dp[-1]



if __name__ == "__main__":
    n = 4
    c = 10
    w = [2,3,4,7]
    v = [1,3,5,9]
    print(backpack_0_1(n,c,w,v))

    