def rotatearray(arr, n):
    print(arr[n+1::])
    return arr[n+1::] + arr[0:n+1]



arr = [1,10,20,0,59,86,32,11,9,40]
n=2
res = rotatearray(arr,n)
print(res)
