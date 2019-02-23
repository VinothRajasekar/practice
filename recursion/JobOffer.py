def jobOffers(scores, lowerLimits, upperLimits):

    output =[]
    query = len(lowerLimits)

    for i in range(0,query):
        res = findRange(scores,lowerLimits[i],upperLimits[i])
        output.append(res)
    return output

def findRange(scores,low,high):
    count = 0
    for num in scores:
        if num >= low and num<=high:
            count +=1
        elif num == high:
            count += 1
            break
    return count

#TestCase 1
scores = [1,3,5,6,8]
lower = [2]
upper =[6]
#output 3

#Testcase 2:
scores = [4,8,7]
lower=[2,4]
upper=[8,4]
#output [3,1]
print(jobOffers(scores,lower,upper))
