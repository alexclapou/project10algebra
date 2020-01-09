from texttable import Texttable
from numpy.polynomial import Polynomial as P

def power_nmk(n, k):
    '''
    get the X^(n-k) polynomial
    parameters:
        n - given number of digits 
        k - given k information digits
        (n-k)
    output:
        X^(n-k)
    '''
    coefs = [0] * (n-k+1)
    coefs[n-k] = 1
    p = P(coefs)
    return p

def get_code(code):
    '''
    create a list which contains every digit of the code
    parameters:
        code - a code word
        n - given number of digits
        k - given k information digits
    output:
        code list
    '''
    code_list = []
    for i in str(code):
        code_list.append(int(i))
    return code_list

def calculate_mX(p, code, n, k):
    '''
    calculate mX^(n-k)
    parameters:
        p - the polynomial X^(n-k)
        code - a code word
        n - given number of digits 
        k - given k information digits
    output:
        mX^(n-k)
    '''
    m = P(get_code(code))
    X = power_nmk(n, k)
    mX = m*X
    return mX

n = int(input("n = "))
k = int(input("k = "))
p = P([1, 1, 0, 1])
print(calculate_mX(p, 110, n, k))
