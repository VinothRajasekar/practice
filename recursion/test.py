
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
              if(compare[0] == firsta and compare not in output):
                output.append(compare)
              else:
                  if compare not in output:
                      output.append(compare)
            else:
              comparef = toString(a)
              if(comparef[0]!='0' and comparef not in output):
                 output.append(comparef)
                 #print(output)
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

#a = '1100'
#b = '1001'
#a = '11'
#b = '223'
#a = '1234'
#b = '1324'
a = '1234'
b = '1213'
print(findSimilar(a,b))
