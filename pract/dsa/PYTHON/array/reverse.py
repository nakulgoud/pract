arr = [1,2,3,4, 5, 6, 7]
start = 0
end = len(arr) - 1
while start < end:
    tmp = arr[start]
    arr[start] = arr[end]
    arr[end] = tmp
    start = start + 1
    end = end - 1

print arr
