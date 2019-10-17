def tuple():

    dict = {}
    output = []
    arr = [('horror', 'scary'), ('frightful', 'ghost')]

    synonm = [('hello how are you scary', 'hello how are you horror'),
              ('hello how are you ghost', 'hello how are you frightful'),
              ('hello how are you good', 'hello how are you good')]

    for i in range (len(arr)):
        print(arr[i][1])
        dict[arr[i][0]] = arr[i][1]

    print(dict)

    for a1, a2 in synonm:
        arrq1 = a1.split(' ')
        arrq2 = a2.split(' ')
        #print(arrq1, arrq2)

        for i in range(len(arrq2)):

            if arrq1[i] != arrq2[i]:
                arrq2[i] = dict[arrq2[i]]
                output.append(True)
            else:
                output.append(False)
        print (arrq2)
        print(output)

        for i in arrq2:
            print(' '.join(arrq2))



tuple()
