def combination_sum(s,target):

    output = []
    s.sort()

    def _generate_all_subsets(target,idx,so_far):

        if target < 0:
           return

        if (target == 0):
           output.append(so_far)
           return

        for i in range(idx, len(s)):
            
            _generate_all_subsets(target-s[i],i,so_far+[s[i]])
        #_generate_all_subsets(so_far,idx+1)

    _generate_all_subsets(target,0,[])

    return output

#s = ['x','y']
s = [2,3,6,7]
target = 7
res = combination_sum(s,target)
print(res)
