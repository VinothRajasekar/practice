from collections import deque

def checkforPalindrome(dString):

    chardeque = deque()

    for i in dString:
        chardeque.appendleft(i)
    print(chardeque)

    stillEqual = True

    while (len(chardeque) > 1 and stillEqual):

        left = chardeque.popleft()
        right = chardeque.pop()

        if (left != right):
            stillEqual = False
    return stillEqual

data = checkforPalindrome('toot')
print(data)
