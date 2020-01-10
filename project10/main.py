from texttable import Texttable
from codewords import *
from matrices import create_H, create_G, generate_Ik, create_P

def write_polynomial(p):
    '''
    write the polynomial
    parameters:
        polynomial variable
    output:
    '''
    list_p = []
    p = input("p = ")
    if p[:1] == "1":
        list_p.append(1)
        p = p[1:]
    p = p.replace(" ", "")
    p = p.replace("+", "")
    p = p.replace("x", "")
    p = list(map(int, p))
    index = 1
    while index <= p[-1]:
        if index in p:
            list_p.append(1)
        else:
            list_p.append(0)
        index += 1
    return list_p

def get_vector(index, n, k):
    '''
    get the vector m(1, 0....0)
    parameters:
        index - which position is 1
        n - length of the code
        k - length of the message
    output:
        vector m
    '''
    vector = [0] * (n-k)
    vector[index - 1] = 1
    return vector

def everything(code, n, k):
    '''
    calculates the code word polynomial
    parameters:
        index - message in binary
        n - given number n
        k - given number k
    output:
        v polynomial
    '''
    #base_2 = binary_list(index, k)
    #code = get_code(base_2)
    mx = calculate_mX(p, code, n, k)
    r = calculate_r(mx, p)
    r = Z2X(r)
    v = calculate_v(mx, r)
    return v

p = ""
n = int(input("n = "))
k = int(input("k = "))
p = write_polynomial(p)
index = 1
nmk = power_nmk(n, k)
coefs = []
while index <= n-k:
    vector = get_vector(index, n, k)
    v = everything(vector, n, k)
    coefs.append(v.coef[:k])
    index += 1

P = create_P(coefs)
Ik = generate_Ik(k)
G = create_G(Ik, P)
H = create_H(Ik, P)
print("matrix G is : \n" + str(G))
print("matrix H is : \n" + str(H))

