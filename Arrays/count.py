def jobOffers(scores, lowerLimits, upperLimits):

    res = [0 for _ in range(len(lowerLimits))]
    count = 0
    for i in range (len(scores)):

        for j in range(len(lowerLimits)):

            if scores[i] >= lowerLimits[j]:

                if scores[i] <= upperLimits[j]:

                    res[j] = res[j] + 1
                    if res[j] == upperLimits[j]:
                       j = lowerLimits
    return res







scores = [1,3,5,6,8]
lowerLimits = [2]
upperLimits = [6]
#scores = [4,8,7]
#lowerLimits = [2,4]
#upperLimits = [8,4]
print(jobOffers(scores, lowerLimits, upperLimits))
