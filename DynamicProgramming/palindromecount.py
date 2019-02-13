def CountPS(str, n):

    # creat empty 2-D matrix that counts
    # all palindrome substring. dp[i][j]
    # stores counts of palindromic
    # substrings in st[i..j]
    dp = [[0 for x in range(n)]
             for y in range(n)]

    # P[i][j] = true if substring str[i..j]
    # is palindrome, else false
    P = [[False for x in range(n)]
                for y in range(n)]

    # palindrome of single lenght
    for i in range(n):
        P[i][i] = True

    # palindrome of length 2
    for i in range(n - 1):
        if (str[i] == str[i + 1]):
            P[i][i + 1] = True
            dp[i][i + 1] = 1

    # Palindromes of length more then 2. This
    # loop is similar to Matrix Chain Multiplication.
    # We start with a gap of length 2 and fill DP
    # table in a way that gap between starting and
    # ending indexes increases one by one by
    # outer loop.
    for gap in range(2, n):

        # Pick starting point for current gap
        for i in range(n - gap):

            # Set ending point
            j = gap + i;

            # If current string is palindrome
            if (str[i] == str[j] and P[i + 1][j - 1]):
                P[i][j] = True

            # Add current palindrome substring ( + 1)
            # and rest palinrome substring (dp[i][j-1] +
            # dp[i+1][j]) remove common palinrome
            # substrings (- dp[i+1][j-1])
            if (P[i][j] == True):
                dp[i][j] = (dp[i][j - 1] + 
                            dp[i + 1][j] + 1 - dp[i + 1][j - 1])
            else:
                dp[i][j] = (dp[i][j - 1] +
                            dp[i + 1][j] - dp[i + 1][j - 1])

    # return total palindromic substrings
    return dp[0][n - 1]
