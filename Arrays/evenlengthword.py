import heapq
def even(sentence):

    #print(sentence)
    a =[]
    max=0
    count =0
    currWord = []
    s = sentence.split(' ')

    for word in s:
        if len(word) %2 == 0:
            #print(word)
            count = len(word)
            if count >= max:
                #print('here')
                if len(currWord) == len(word):
                    continue
                else:
                    currWord = word
                    max = len(currWord)
                #print(currWord)
            #heapq.heappush(a, word)
    #print(heapq.heappop(a)[-1])
    #print(heapq.nlargest(1,a))
    if not currWord:
        return 00
    else:
        return currWord
    print(currWord)

    #print(s)
    #print(heapq)







sentence = 'It is a pleasant word today'
#sentence = 'Time to write great code'
print(even(sentence))
