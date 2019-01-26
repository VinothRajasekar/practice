def generate_all_expressions(num, target):

    if not num:
        return []
    output=[]

    def _dfs(so_far,evaluated,idx,prev):

        if idx==len(num):
            if evaluated == target:
               output.append(so_far)

        for i in range(idx,len(num)):
            curr = num[idx:i+1]
            curr_elem = int(curr)

            if idx == 0:
               #print((so_far + curr, curr_elem, i+1, curr_elem))
               _dfs(so_far + curr, curr_elem, i+1, curr_elem)
            else:
            print(curr_elem)
               _dfs(so_far + '+' + curr, evaluated+curr_elem, i+1, curr_elem)
               _dfs(so_far+'*'+curr, (evaluated-prev)+(prev*curr_elem), i+1, prev*curr_elem)


    _dfs('', 0, 0, 0)
    return output

















num = '1234'
target=24
print(generate_all_expressions(num,target))
