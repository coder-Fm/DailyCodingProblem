# RigthRotate: array, number -> array
# RightRotate: consumes an array arr, and a number of rotation k,
# then returns a rotated array
def RightRotate(arr, k):
    n = len(arr)
    #gcd function calculates the greater conmmon divisor
    #of any given x and y
    def gcd(x, y):
        if y == 0:
            return x;
        else:
            return gcd(y, x % y)
    k = k % n
    arr_gcd = gcd(k, n)

    for i in range(arr_gcd,n):
        temp = arr[i]
        j = i

        while 1:
            m = j + k
            if m >= n:
                m = m - n
            if m == i:
                break
            arr[j] = arr[m]
            j = m
        arr[j] = temp
    return arr
#test
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

RightRotate(arr, 2)
