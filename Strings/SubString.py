def subString(text,prefixString,suffixString):

    left = 0
    right = 0
    preLeft=0
    preRight = 0

    ## O(n) and space O(1)
    while left < len(text) and right < len(suffixString):

          if text[left] != suffixString[right]:
              left = left + 1
          else:
              text[left] == suffixString[right]
              left = left + 1
              right = right + 1

    while preLeft < len(text) and preRight < len(prefixString):

          if text[preLeft] != prefixString[preRight]:
              preRight = preRight + 1
          else:
              text[preLeft] == prefixString[preRight]
              preLeft = preLeft + 1
              preRight = preRight + 1

    prefixScore = preLeft
    suffixScore = right

    score = preLeft + right

    ### didn't remember the other condition for return.
    return text[:score]

#Test case1
a = subString('engine','raven','gingko')
#Test case2
b = subString('ab','a','b')


print(a)
print(b)
