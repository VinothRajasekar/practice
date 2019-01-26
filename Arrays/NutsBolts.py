from itertools import starmap

def solve(nuts,bolts):

    nmap = {}
    bmap = {}
    results = []

    for i in range(0, len(nuts)):
        nmap[nuts[i]] = i

    for i in range (0,len(bolts)):
         if bolts[i] in nmap:
            nuts[i] = bolts[i]
           #nuts[i] = bolts[i]
    for i, nutval in enumerate(nuts):
        results.append('%s %s' % (nutval, bolts[i]))
    return results  
    #return list(starmap(lambda i, nut: '%s %s' % (nut, bolts[i]), enumerate(nuts)))

nuts = [6, 32, 5, 7]
bolts = [32, 7, 5,6]
res = solve(nuts,bolts)
print(res)
