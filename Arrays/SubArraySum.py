#Subarray Sum Equals K

def subArray_sum(nums,k):
    dict={0:1}
    count = 0
    sum =0
    res=0
    for num in nums:

        sum += num

        if sum-k in dict:
            res +=dict[sum-k]

        if sum in dict:
            dict[sum] +=1
        else:
            dict[sum] = 1
    return res

s = [1,1,1]
k=2
print(subArray_sum(s,k))
