def levenshteinDistance(strWord1, strWord2):


    srcLen = len(strWord1)
    destLen = len(strWord2)

    dp = [[0 for _ in range(destLen+1)] for _ in range(srcLen+1)]

    for i in range(srcLen):
        dp[i][destLen] = srcLen - i

    print(dp)

    for j in range(destLen):
        dp[srcLen][j] = destLen - j

    print(dp)

    ##delete -> (i+1, j), add(i,j+1), update/replace(i+1,j+1)

    for i in range (srcLen-1, -1, -1):
        for j in range(destLen-1, -1, -1):
            if strWord1[i]==strWord2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
    return dp[0][0]









strWord1='cat'
strWord2='bat'
print(levenshteinDistance(strWord1,strWord2))
