from collections import deque
import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        m = len(wordList[0])
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        wordList.add(beginWord)
        matrix = collections.defaultdict(list)
        for word in wordList:
            print(word)
            for i in range(m):
                s = word[:i] + '_' + word[i+1:]
                print(s)
                matrix[s].append(word)
        print(matrix)
        queue = [beginWord]
        mark = set()
        mark.add(beginWord)
        dist = 1
        while queue:
            next_queue = []
            while queue:
                word = queue.pop(0)
                for i in range(m):
                    s = word[:i] + '_' + word[i+1:]
                    for next_word in matrix[s]:
                        if next_word not in mark:
                            if next_word == endWord:
                                return dist + 1
                            mark.add(next_word)
                            next_queue.append(next_word)
            queue = next_queue
            dist += 1
        return 0

begin = "hit"
end = "cog"
dict_words = ["hot","dot","dog","lot","log","cog"]
a = Solution()
print(a.ladderLength(begin,end,dict_words))
