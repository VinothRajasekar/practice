def summaryRanges(nums):

    left = 0
    right = 0
    res = []

    for i in range(0,len(nums)-1):
        if nums[i]+1 == nums[right + 1]:
           right=right+1
        elif left < right:
            res.append(str(nums[left]) + "->" + str(nums[i]))
            left = i + 1
            right = right + 1
            print(res, left, right, i,len(nums))
        elif left == right:
            res.append(str(nums[left]))
            left = i + 1
            right = i + 1
    else:
        if left == right:
            res.append(str(nums[left]))
        else:
            res.append(str(nums[left]) + "->" + str(nums[i+1]))

    return res

result = summaryRanges([0,1,2,4,5,7])
print(result)
