
def bstsearch(root, val):


    #time complexity O(log n). since one side of tree is pruned on searching

    #space complexity O(1). no extra space is used

    ## if root is None return 0 else iterarte and value found return 1 else 0

    if root is None:
        return 0

    iter = root

    while iter:
        if iter.value == val:
            return 1
        elif val < iter.value:
            iter = iter.left
        else:
            iter = iter.right
    return 0
