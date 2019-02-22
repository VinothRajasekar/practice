def knapsack(profits,weights,capacity):

    if len(profits) == 0 or len(weights)!= len(profits) or capacity<=0:
        return 0

    n = len(profits)

    dp = [[0 for _ in range(capacity+1)] for _ in range(n)]
    print(dp)

    for i in range(capacity+1):
        if weights[0] <= capacity:
            dp[0][i] = profits[0]
    print(dp)

    for i in range(1,n):
        for c in range(1,capacity+1):
            profit1=0
            profit2=0

            if (weights[i]<=c):
                profit1 = profits[i] +dp[i-1][c-weights[i]]
            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1,profit2)
    return dp[n-1][capacity]












profits = [1,6,10,6]
weights = [1,2,3,5]
capacity = 7
print(knapsack(profits,weights,capacity))
