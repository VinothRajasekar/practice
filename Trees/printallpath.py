def  printAllPaths(root):

    if root is None:
        return

    def _printpath(root,so_far):

        so_far.append(root.val)

        if root.left == None and root.right==None:
           print(''.join(str(i) for i in so_far))

        _printpath(root.left, so_far)
        _printpath(root.right, so_far)
        so_far.pop()

    _printpath(root,[])
