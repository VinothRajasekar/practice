def productexceptself(s):


    res = []
    temp = 1

    for num in s:
        res.append(temp)
        temp*=num
    #print(res)

    temp = 1

    for i in range(len(s)-1,-1,-1):
        res[i]  *= temp
        print(temp,res[i])
        temp *= s[i]
        print(temp)
        print(res)


s = [3,2,1]
print(productexceptself(s))
