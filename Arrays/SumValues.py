def sum_two_values(arr,val):

    found_values = set()

    for a in arr:
        print(found_values)
        print(val-a)
        if val-a in found_values:
           return True
        found_values.add(a)

checkSum = sum_two_values([2,3,5], 8)
print(checkSum)


def sum_two_values_with_pointers(arr, val):

    arr = sorted(arr)
    print(arr)

    i = 0
    j = len(arr)-1

    while i < j:
        found = arr[i] + arr[j]
        if(found == val):
           return True

        if found < val:
            i += 1
        else:
            j -=1
    return False

checkSum = sum_two_values_with_pointers([2,1,8,4,7,3], 3)
print(checkSum)
