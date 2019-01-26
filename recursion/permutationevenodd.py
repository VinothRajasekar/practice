def permutate(val, l, r):

    if(l == r):
        print(val)
    else:
        for i in range(l, r + 1):

            #if(checkoddeven(i, val[l])):
            tempResult = swap(val, l, i)
            permutate(tempResult, l+1, r)

def checkoddeven(i, data):

    if ((i%2 == 0 ) and data %2 == 1) or (i%2 ==1 and data % 2 ==0):
        return True
    return False

def swap(val, l, i):

    val[i], val[l] = val[l], val[i]
    return val

if __name__ == '__main__':

   val = [1,2,3,4]
   n = len(val)
   permutate(val, 0, n-1)
