def countPalindromes(s):
    # Write your code here
    n = len(s)
    count = 0
    dp = [[0 for _ in range(n)] for _ in range (n)]

    for i in range(n):
        dp[i][i] = True
        count += 1

    for i in range (n-1,-1,-1):
        for j in range (i+1, n):
            if s[i] == s[j]:
                print(s[i])
                if (j-i == 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count +=1
    return count


s = 'aaa'
print(countPalindromes(s))
