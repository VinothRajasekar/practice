def permute(a, l, r): 
    if l==r:
        print (toString(a))
    else: 
        for i in range(l,r+1):
            #a[l], a[i] = a[i], a[l]
            # dont store o/p in  an array. creating extra space. not a good idea
            c = swap(a,l,i)
            #swap(a,l,i)
            permute(c, l+1, r)
            #swap(a,l,i)
            #a[l], a[i] = a[i], a[l]

def swap(a,i, j):

    b = list(a)
    b[i],b[j] = b[j], b[i]
    return ''.join(b)

def toString(List):
    return ''.join(List)

if __name__ == '__main__':
    string = "ABC4"
    n = len(string)
    a = list(string)
    permute(a, 0, n-1)
