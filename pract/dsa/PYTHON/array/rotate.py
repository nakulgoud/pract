'''
Juggling algorithm: 

Link for problem: http://www.geeksforgeeks.org/array-rotation/
'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def left_rotate(arr, rotate_by):
    for i in range(0, gcd(len(arr), rotate_by)):
        temp = arr[i]
        j = i
        while True:
            k = j + rotate_by
            if k >= len(arr):
                k = k - len(arr)
            if k == i:
                break
            arr[j] = arr[k]
            j = k

        arr[j] = temp

arr = [1,2,3,4,5,6,7,8,9,10,11,12]
rotate_by = 7
left_rotate(arr, rotate_by)
print arr

