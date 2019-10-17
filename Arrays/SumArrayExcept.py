def sum_array(arr):

    dict = {}
    sum=0
    res = []

    for i in range (len(arr)):
        dict[i] = arr[i]
        sum+= arr[i]


    for i in range (len(arr)):
       res.append(sum-dict[i])

    return res

arr = [3,6,4,8,9]
print(sum_array(arr))
