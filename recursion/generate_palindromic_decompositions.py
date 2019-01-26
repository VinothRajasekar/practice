from collections import deque

def generate_palindromic_decompositions(s):

    if len(s) == 1:
        return [s]
    output=[]

    def _generate_palindromic_decompositions(so_far,idx):

        ##base case
        if idx == len(s):
           output.append("|".join(so_far))
           return

        for i in range(idx+1, len(s)+1):
            curr = s[idx:i]
            print(idx,i)
            d = deque(curr)
            if checkPalindrome(d):
                print(curr)
                so_far.append(curr)
                _generate_palindromic_decompositions(so_far,i)
                so_far.pop()
    _generate_palindromic_decompositions([],0)

    return output

def checkPalindrome(d):
    while len(d) > 1 :
        left = d.popleft()
        right = d.pop()
        if(left!=right):
            return False
    return True




#s = "abracadabra"
s = "aa"
res = generate_palindromic_decompositions(s)
print("output",  res)
