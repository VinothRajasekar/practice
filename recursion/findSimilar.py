output = []
x = set()
y = set()

def findSimilar(a, b):
    # Write your code here
    firsta =a[0]
    firstb =b[0]
    n = len(a)
    n1= len(b)

    def __permutate(a,l,r):

        if l == r :
            if x!=y:
              compare = toString(a)
              if(compare[0] == firsta[0] and compare not in output):
                output.append(compare)
              else:
                if compare not in output:
                    output.append(compare)
            else:
              compare = toString(a)
              if(compare[0]!='0' and compare not in output):
                 output.append(compare)
            return
        else:
            for i in range (l, r + 1):
                c = swap(a,l,i)
                __permutate(c,l+1,r)

    for num in a:
        x.add(num)
    for num in b:
        y.add(num)

    if len(x) == len(y):
        __permutate(a,0,n-1)
    else:

        __permutate(b,0,n1-1)
    return len(output)


def swap(a,i,j):
    b = list(a)
    b[i],b[j] = b[j],b[i]
    return ''.join(b)

def toString(List):
    return ''.join(List)

#TestCase 1
#-----------
#a = '1234'
#b = '1324'
#output = 24
#TestCase 2
#-----------
#a = '1234'
#b = '1213'
#output = 12
#TestCase 3
#-----------
#a = '1100'
#b = '1001'
#output = 3
#TestCase 4
#-----------
a = '11'
b = '223'
#output = 3
print(findSimilar(a,b))
