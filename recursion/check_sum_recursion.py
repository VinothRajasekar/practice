
def check_if_sum_possible(arr, k):

    flag = []

    if not arr:
        return False

    def _recurse_sum(so_far,idx):

        if len(arr) == idx:
           if so_far and sum(so_far) == k:
              flag.append(True)
              return True
           return False

        #return _recurse_sum(so_far+[arr[idx]], idx+1)

        #_recurse_sum(so_far,idx+1)
        _recurse_sum(so_far+[arr[idx]], idx+1)
        _recurse_sum(so_far,idx+1)


    def checkSum(data):
        val = sum(data)
        if val==k:
           flag=1
           return True
        return False

    _recurse_sum([], 0)
    return flag[0]

arr = [2,4,6,0,0,2,3]
k=12
print(check_if_sum_possible(arr,k))
