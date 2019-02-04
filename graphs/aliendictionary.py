from collections import defaultdict

def find_order(words):

    all_chars = set()
    for word in words:
        for c in word:
            all_chars.add(c)

    deps = defaultdict(set)
    visited = {}
    order = []
    seen = set()

    for w1, w2 in zip(words,words[1:]):
        print(w1,w2)
        for c1, c2 in zip(w1,w2):
            if c1!=c2:
                deps[c1].add(c2)
                break

    def _dfs1(start):

        seen.add(start)

        for next in deps[start] - seen:
            _dfs1(next)
        return True


    def _dfs(start):

        status = visited.get(start)
        if status == 1:
            return True

        if status == -1:
            return False

        visited[start] = -1

        for n in deps[start]:
            if not _dfs(n):
               return False


        visited[start] = 1
        order.append(start)

        return True


    for c in all_chars:
        if not _dfs(c):
            return ''
    return ''.join(reversed(order))


words = ['baa', 'abcd', 'abca', 'cab','cad']

#words = ['c', 'aaaa', 'aaaa', 'aabc']
#words = ['wrt','wrf','er','ett','rftt']
print(find_order(words))
