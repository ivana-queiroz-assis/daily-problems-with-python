#Given an array of n elements which contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and using only constant memory space.
def printRepeating(arr, size):
    print("The repeating elements are: ")

    for i in range(0, size):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")
arr = [1, 2, 3, 1, 3, 6, 6]
arr_size = len(arr)

printRepeating(arr, arr_size)
