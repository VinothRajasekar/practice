
def removeduplicates(nums):

        if len(nums)<=0:
            return 0

        j=0

        for i in range(1, len(nums)):

            if(nums[i] != nums[j]):
               j= j + 1
               nums[j] = nums[i]

        return j+1


a = [1,1,2]
res = removeduplicates(a)
print(res)
ans =[]
for i in range(0,res):
    ans.append(a[i])
print(ans)

