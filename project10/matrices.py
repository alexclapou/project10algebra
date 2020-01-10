import numpy as np
'''
create G and H matrices
    G = P/I
    H = I/P
'''

def generate_Ik(k):
    '''
    create and return the identity matrix for an given k
    parameters:
        k - 
    output:
        identity matrix
    '''
    Ik = np.identity(k)
    return Ik

def create_P(code):
    '''
    create P matrix
    parameters:
        code - columns which are the message
    output:
        P matrix
    '''
    P = np.matrix(code)
    P = np.transpose(P)
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
