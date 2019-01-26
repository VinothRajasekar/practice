
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def merger_first_into_second(A1,A2):
     n = len(A1)
     j = 0
     for i in range(n, 2*n):
        swap(A2, i, j)
        j += 1
     print(arr2)


     j,k = 0,n
     print(j,k,n)
     for i in range(2*n):
        if j == n:
            print("barro",i,A2[k])
            A2[i] = A2[k]
            k += 1
        elif k == 2*n:
            A2[i] = A1[j]
            j += 1
        elif A1[j] < A2[k]:
            A2[i] = A1[j]
            j += 1
            print(A2)
        else:
            A2[i] = A2[k]
            k += 1
            print(k)
            print("h",A2, j)
     return A2








arr1 = [1, 3, 5]
arr2 = [2, 4, 6, 0, 0, 0]
print (merger_first_into_second(arr1, arr2))
