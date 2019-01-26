def generate_all_subsets(s):

    output = []

    def _generate_all_subsets(so_far, idx):

        if (idx == len(s)):
            output.append("".join(so_far))
            return

        _generate_all_subsets(so_far+[s[idx]], idx+1)
        _generate_all_subsets(so_far,idx+1)




    _generate_all_subsets([],0)

    return output

s = ['x','y']
res = generate_all_subsets(s)
print(res)
