def dtrcompare(s1,s2):

    count = 0
    same = False
    x = set()
    y = set()
    for num in s1:
        x.add(num)

    for num in s2:
        y.add(num)

    print(x)
    print(y)

    if len(s1) == len(s2):
        print('trueaa')

    for s1 in s2:
        count = count + 1

    if len(s1) == count:
        print('hey')
    print(count)







s1 = '112'
s2 = '121'
dtrcompare(s1,s2)
