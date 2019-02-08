def max_win(coins):

    n = len(coins)
    #print(n)
    dp = [[0]*n for _ in range(n)]
    #print(dp)

    for i in range(n):
        dp[i][i] = coins[i]
    #print(dp)

    for i in range(n-1, -1,-1):
        for j in range(i,n):
            if i==j:
                #print(i,j, coins[i])
                dp[i][j] = coins[i]
                continue
            print("stat",i,j)

            o1 = dp[i+2][j] if i < n-2 else float('inf')
            print("o1",o1, i+2, j)
            o2 = dp[i+1][j-1] if i < n - 1 and j > 0 else float('inf')
            print("o2",o2,i+1,j-1)
            o3 = dp[i][j-2] if j > 1 else float('inf')
            print("o3",o3, i, j-2)
            print(coins[i])
            print(min(o1,o2))
            print(coins[j])
            print(min(o2,o3))


            dp[i][j] = max(coins[i] + min(o1, o2), coins[j] + min(o2, o3))

    return dp[0][n-1]







c = [8, 15, 3, 7]
print (max_win(c))
