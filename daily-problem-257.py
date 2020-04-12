#Given an array of integers out of order,
# determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted.
# For example, given [3, 7, 5, 6, 9], you should return (1, 3).

def window(array):
    left, right = None, None
    s = sorted(array)
    print('Array: ', str(arr))
    print('Array ordernado: ', str(s))
    for i in range(len(array)):
        print( str(i)+ 'ª Interação')
        print('Se ' + str(arr[i]) + " é diferente " + str(s[i]))
        if array[i] != s[i] and left is None:
            print('Left recebeu: '+ str(i))
            left = i
        elif array[i] != s[i]:
            print('Right recebeu: ' + str(i))
            right = i
    print('Retornando, left: ' + str(left) + ', right: ' + str(right))
    return left, right

def window_better_perfomance(array):
    left, right = None, None
    n = len(array)
    max_seen, min_seen = -float("inf"), float("inf")

    for i in range(n):
        max_seen = max(max_seen, array[i])
        print('Máximo visto : ' + str(max_seen))
        if array[i] < max_seen:
            right = i
            print('Novo right : ' + str(right))

    for i in range(n - 1, -1, -1):
        min_seen = min(min_seen, array[i])
        print('Minimo visto : ' + str(min_seen) + ', com I igual á: '+ str(i))
        if array[i] > min_seen:
            left = i
            print('Novo left : ' + str(left))

    return left, right


arr = [4,7,3,1,10]

print(window_better_perfomance(arr))