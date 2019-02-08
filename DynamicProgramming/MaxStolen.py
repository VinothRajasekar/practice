def maxStolenValue(values):

    dp = [None] * (len(values) + 2)
    print(dp)
    dp[-1] = 0
    dp[-2] = 0

    for i in range(len(values)-1,-1,-1):
        steal = dp[i+2] + values[i]
        skip = dp[i+1]
        dp[i] = max(steal,skip)
    return dp[0]

values = [1, 2, 4, 5, 1]
print(maxStolenValue(values))
