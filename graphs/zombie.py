from collections import deque

def zombieClusters(zombies):

    graph ={}
    visited = set()
    count = [0]

    for i in range (len(zombies)):
        graph[i] = []
        for j in range (len(zombies)):
            if zombies[i][j] == '1'and i!=j:
                graph[i].append(j)
        print(graph)

    for z in graph:
        if z not in visited:
            visited.add(z)
            q=deque()
            q.append(z)

            while q:
                curr = q.popleft()
                for e in graph[curr]:
                    if e not in visited:
                        visited.add(e)
                        q.append(e)
            print("b", z)
            count[0]+=1
    return count[0]






input = ['1100', '1110', '0110', '0001']
#input = ['10000', '01000', '00100', '00010','00001']

print(zombieClusters(input))
