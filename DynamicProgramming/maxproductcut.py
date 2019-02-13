def max_product_from_cut_pieces(n):
    #
    # Write your code here.
    #
    dp = [0 for _ in range(n+1)]

    dp[1] = 1

    for i in range(n+1):
        mp = 0
        for j in range (n):
            mp = max(mp,max(j*dp[i-j], j*(i-j)))
        dp[i] = mp

    return dp[-1]



n = 5
print(max_product_from_cut_pieces(n))
