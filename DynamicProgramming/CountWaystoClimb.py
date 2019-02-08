def countWaystoClims(steps,n):

    print(steps,n)
    k = len(steps)
    dp = [0 for _ in range(n+1)]
    dp[0] = 1

    for j in range(n+1):
        for i in range(k):
            print(steps[i], j)
            if steps[i] <=j:
                print('here')
                dp[j] += dp[j-steps[i]]
                print(dp)
    return dp[n]

steps =[2,3]
n=7

print(countWaystoClims(steps,n))
