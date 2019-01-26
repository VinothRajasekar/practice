a = [2,1,3,4]
b={}

for i in a:
    b[i] = True
print(b)

for a in b:
    if (a-1) not in b:
        print(a)
