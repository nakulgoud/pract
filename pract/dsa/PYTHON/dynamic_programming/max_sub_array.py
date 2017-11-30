'''
Maximum sum sub array is a sum of subset of given array with consecutive elements such that their sum is max
Consider array: [1, -3, 2, 1, -1], its max sub array is [2, 1] and their sum is 3
'''


def max_sub_array_naive(array):
    '''
    Complexity O(n^2)
    '''
    pass

def max_sub_array_dynamic(array):
    '''
    complexity O(n)
    '''
    max_global = max_current = array[0]
    for i in array[1:]:
        max_current = max(i, max_current + i)
        if max_current > max_global:
            max_global = max_current

    return max_global

if __name__=='__main__':
    array = [1, -3, 2, 1, -1]
    print 'by naive approach:{}'.format(max_sub_array_naive(array))
    print 'by dynamic approach:{}'.format(max_sub_array_dynamic(array))
