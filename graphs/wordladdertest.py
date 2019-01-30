from collections import deque
import string

class Solution:
    def findLadders(self, beginWord, endWord, wordList):

        words_set = set(wordList)
        words_set.add(endWord)
        def get_neighbors(string):

            res = []

            if len(words_set)>26:
                for char in string.ascii_lowercase:
                    for i in range(len(string)):
                        new_str = string[:i] + char + string[i+1:]
                        if new_str in words_set:
                            res.append[new_str]
            else:
                for word in words_set:
                    difference = 0
                    for i in range(len(string)):
                        if word[i]!=string[i]:
                            difference += 1
                        if difference > 1:
                            break
                    if difference == 1:
                       res.append(word)
            return res

        back_refs = {beginWord:None}
        q = deque()
        q.append(beginWord)
        visited = set()
        found = False

        while q:
            w = q.popleft()
            for n in get_neighbors(w):
                if n==endWord:
                    found = True
                    back_refs[n] = w
                    break
                if n not in visited:
                    visited.add(n)
                    q.append(n)
                    back_refs[n] = w
            if found:
                break

        path = []
        curr = endWord

        while curr:
            path.append(curr)
            curr=back_refs[curr]

            if curr == beginWord:
                path.append(curr)
                break

        return path[::-1]


begin = "hit"
end = "cog"
dict_words = ["hot","dot","dog","lot","log","cog"]
a = Solution()
print(a.findLadders(begin,end,dict_words))
