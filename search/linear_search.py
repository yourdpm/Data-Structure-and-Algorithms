# Linear search x in arr[]
# If x is present the return it location
# else return -1

def linear_search(arr, x):
    for i range(len(arr)):
        if arr[i] == x:
            return i

    return -1