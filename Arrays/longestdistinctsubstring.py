def longestsubstring(s):

    map = set()
    n = len(s)
    i, j, ans = 0,0,0

    while (i<n and j<n):

        if s[j] not in map:
            map.add(s[j])
            j+=1
            ans = max(ans,j-i)
        else:
            map.remove(s[i])
            i+=1
    return ans








s = "abcabcbb"
print(longestsubstring(s))
