def recursion_braces(n):

    output = []

    def validteBraces(s):
        stack = []
        dict = {'[' :']'}
        for char in s:
            if char in dict:
                stack.append(char)
            elif not stack or char!= dict[stack.pop()]:
                 return False
        return not stack

    def _recurse_braces(s,open, close):

        if(len(s)==2*n):

          if (validteBraces(s)):
             output.append(''.join(s))
          return

        _recurse_braces(s+['['], open+1, close)
        _recurse_braces(s+[']'], open, close+1)

    _recurse_braces([],0,0)
    return output



n=2
print(recursion_braces(n))
