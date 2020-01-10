from numpy.polynomial import Polynomial as P

'''
functions to calculate the solution for the table
'''

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
    for i in code:
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
def calculate_r(mX, p):                                                            
    '''                                                                            
    calculate r polynomial, mX^(n-k) mod p                                         
    parameters:                                                                    
        mX - mX^(n-k)                                                              
        p - the polynomial                                                         
    output:                                                                        
        mX^(n-k) % p                                                               
    '''                                                                            
    return mX % p                                                                  
                                                                                   
def Z2X(p):                                                                        
    '''                                                                            
    convert to Z2[X]                                                               
    parameters:                                                                    
        p - polynomial                                                             
    output:                                                                        
        p - polynomial in Z2[X]                                                    
    '''                                                                            
    p = p.coef                                                                     
    new_coef= [0] * (len(p))                                                       
    for i, j in enumerate(p):                                                      
        new_coef[i] = (2-int(j)) % 2                                             
    return P(new_coef)                                                             
                                                                                   
                                                                                   
def calculate_v(mX, r):                                                            
    '''                                                                            
    calculate v polynomial, r + mX^(n-k)                                           
    parameters:                                                                    
        mX - mX^(n-k)                                                              
        r - mX^(n-k) mod p                                                         
    output:                                                                        
        v polynomial                                                               
    '''                                                                            
    r = Z2X(r)                                                                     
    v = mX+r
    return v
