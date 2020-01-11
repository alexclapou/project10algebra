import numpy as np
from copy import  deepcopy
'''
create G and H matrices
    G = [P/Ik] Ik - identity matrix k
    H = [Ink|P]  Ink identity matrix n-k
'''

def generate_Ik(n, k):
    '''
    create and return the identity matrix for an given k
    parameters:
        k - 
    output:
        identity matrix
    '''
    Ik = np.identity(n-k)
    return Ik

def create_P(code):
    '''
    create P matrix
    parameters:
        code - columns which are the message
    output:
        P matrix
    '''
    '''
    index_inlist = len(code[0])
    i = 0
    random = []
    new_code = []
    while i < index_inlist:
        for j in code:
            random.append(j[i])
        new_code.append(deepcopy(random))
        random.clear()
        i += 1
    print(new_code)
    print(code)
    '''
    P = np.matrix(code)
    return P


def create_G(Ik, P):
    '''
    create the G matrix
    parameters:
        Ik - identity matrix
        P - P matrix
    output:
        matrix G
    '''
    G = np.concatenate((P, Ik))
    return G

def create_H(Ik, P):
    '''
    create H matrix
    parameters:
        Ik - identity matrix
        P - P matrix
    output:
        H matrix
    '''
    H = np.concatenate((Ik, P), axis=1)
    return H
