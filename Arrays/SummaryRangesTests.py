def summaryRangesTest(nums):

    i = 0
    left = 0
    res = []

    while i < len(nums):

         while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
               i = i + 1
         if left < i:
            res.append(str(nums[left]) + "->" + str(nums[i]))
         else:
            res.append(str(nums[left]))
         left = i + 1
         i = i + 1
    return res

#result = summaryRangesTest([0,1,2,4,5,7])
result = summaryRangesTest([0,1,2,4,5,7])
print(result)
