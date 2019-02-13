def numberOfPaths(a):

    print(a)
    r = len(a)
    c = len(a[0])
    print(r,c)
    dp = [[0 for _ in range(r+1)]for _ in range (c+1)]
    print(dp)

    dp [0][0] = 1

    for i in range(r):
        dp[i][0] = 1

    for j in range(r):
        dp[0][j] = 1

    for i in range(1, r):
        for j in range(c):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[r-1][c-1]














a = [[1,1,0],[1,1,1]]
print(numberOfPaths(a))
