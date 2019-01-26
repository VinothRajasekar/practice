
def threeSum(arr):
        if len(arr) < 3:
            return []

        results = []


        arr.sort()
        n = len(arr)

        if arr[0] == arr[1] == arr[-1] == 0:
            results.append([0,0,0])
            return map(lambda x: ','.join([str(a) for a in x]), results)


        for i in range(0,n-2):

            left = i + 1
            right = n-1
            curr = arr[i]
            if arr[i] > 0:
                continue
            print(arr[i], arr[i-1])
            if arr[i] == arr[i-1]:
              continue
            while (left < right):

              if(curr + arr[left] + arr[right] == 0):

                 results.append([curr, arr[left], arr[right]])
                 print(results)

                 while left < right and arr[left] == arr[left + 1]:
                   left=left + 1

                 while left < right and arr[right] == arr[right - 1]:
                   right=right-1


                 left = left + 1
                 right = right -1

              elif (curr + arr[left] + arr[right] < 0 ):

                    left = left + 1
              else:

                    right = right - 1
        return map(lambda x: ','.join([str(a) for a in x]), results)

arr = [6,0,0,0]
a = threeSum(arr)
print(list(a))
