def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        bucket = [[] for _ in range(len(nums)+1)]
        print(bucket)
        #print(bucket)
        for key, val in dict.items():
            bucket[val].append(key)
        print(bucket)
        print(list(reversed(bucket)))
        ret = []
        for row in reversed(bucket):
            if not row:
                continue
            else:
                for i in range(len(row)):
                    ret.append(row[i])
                    if len(ret) == k:
                        return ret
nums=[1,5,5,1]
k=2
print(topKFrequent(nums,k))
