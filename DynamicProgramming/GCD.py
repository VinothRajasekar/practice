def splitTheArray(val):
    # Write your code here
    first = val[0]
    n = len(val)

    def __splitarray(a,b):
        if (a==0 or b==0):
            return 0

        if (a == b):
            return a

        if a<b:
            return  __splitarray(a,b-a)
        return __splitarray(a-b,b)


    for i in range (1,n):
        first = __splitarray(first,val[i])
    return first

arr = [2,3,2,3,3]
print(splitTheArray(arr))
