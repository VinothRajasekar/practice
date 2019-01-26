def dutch_flag_sort(balls):
    #
    # Write your code here.
    #
    low = 0
    mid = 0
    high = len(balls)-1
    print(len(balls))

    while mid <=high:
        if balls[mid] == 'R':
            balls[low], balls[mid] = balls[mid],balls[low]
            mid = mid + 1
            low = low + 1
        elif balls[mid] == 'G':
            mid = mid + 1
        else:
            balls[mid],balls[high] = balls[high], balls[mid]
            high = high -1
    return "".join(balls)

d ='GBGGRBRG'
arr = list(d)
print(arr)
#d = ['G','B','G','G','R','B','R','G']
a = dutch_flag_sort(arr)
print(a)
