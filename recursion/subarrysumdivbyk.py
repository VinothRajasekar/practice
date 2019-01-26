
def test(A,K):

        mapp={0:1}    ## mapp stores (sum % K, count)
        total,count=0,0
        for x in A:
            total+=x
            if total%K in mapp: count+=mapp[total%K]
            mapp[total%K]=mapp.get(total%K,0)+1
        return count


A = [4,5,0,-2,-3,1]
K=19
print(test(A,K))
