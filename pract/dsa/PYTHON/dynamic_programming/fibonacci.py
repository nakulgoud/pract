def fibonacci_recursive(n):
    '''
    finds nth element in fibonacci series by recursive approach
    '''
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2) 

def fibonacci_dynamic(n):
    '''
    finds nth element in fibonacci series by dynamic programming approach
    '''
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    n1 = 1
    n2 = 1
    ret = 0
    for i in range(2, n+1):
        ret = n1 + n2
        n1 = n2
        n2 = ret

    return ret

if __name__=='__main__':
    '''
    fibo series: 1 1 2 3 5 8 13 21 ...
    '''
    print 'fibonacci by naive approach'
    print fibonacci_recursive(8)
    print 'fibonacci by dynamic programming approach'
    print fibonacci_dynamic(8)
