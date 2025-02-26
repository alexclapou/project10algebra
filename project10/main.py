from texttable import Texttable
from bkt import *
import copy
from codewords import *
from matrices import create_H, create_G, generate_Ik, create_P
import numpy as np

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

def get_vector(index, k):
    '''
    get the vector m(1, 0....0)
    parameters:
        index - which position is 1
        k - length of the message
    output:
        vector m
    '''
    vector = [0] * (k)
    if isinstance(index, list):
        for i in range(len(index)):
            vector[index[i]-1] = 1
        return vector
    else:
        vector[index-1] = 1
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
    mx = calculate_mX(p, code, n, k)
    r = calculate_r(mx, p)
    v = calculate_v(mx, r)
    v = Z2X(v)
    return v

def base_2(number):
    '''
    convert to base 2
    parameters:
        number - a number in base 10
    output:
        number in base 2
    '''
    if number < 2:
        return number
    else:
        if number % 2 != 0:
            return  1 + 10 * base_2(number//2)
        else:
            return 10 * base_2(number//2)

def get_syndrome(number, k):
    '''
    get the syndrome list, take number in base 10 and convet into a list(Base 2 digits)
    parameters:
        number - number 1, 2**k
        k - given k
    output:
        the list which contains digits for number in base 2
    '''
    this_list = []
    number = str(base_2(number))
    zeros = k-len(number)
    while zeros > 0:
        this_list.append(0)
        zeros -= 1
    for i in str(number):
        this_list.append(i)
    this_list = list(map(int, this_list))
    return this_list

def get_distance(data):
    x = 1
    distance = (n*(n+1))//2
    for i in data:
        if i == 1:
            distance -= x
        x = x + 1
    distance = distance / len(data)
    return distance


def search_coset(syndrome, H, n):
    '''
    search coset for each syndrome
    parameters:
        n
        syndrome
        H matrix
    output:
        [syndrome, coset]
    '''
    found = False
    index = 1
    while index < 6:
        b = Backtracking(n, index)
        b.backtracking(0)
        coset_list = b.last_list
        mini = 1000
        keep = []
        for i in coset_list:
            c = i*np.transpose(H)
            c = c % 2 #Z2
            if np.array_equal(c, syndrome):
                if get_distance(i) < mini and index != 1:
                    mini = get_distance(i)
                    keep = i
                else:
                    return i
        if mini != 1000:
            return keep
        index += 1
    return [0] * (n-k)

#input
p = ""
n = int(input("n = "))
k = int(input("k = "))
p = write_polynomial(p)
#input


nmk = power_nmk(n, k)
index = 1
coefs = []

#creating v and vector m=(1,,...)
while index <=  k:
    vector = get_vector(index, k)
    v = everything(vector, n, k)
    coefs.append(v.coef[:n-k])
    index += 1
#creating v and vector m(1,,....)

#create coefs for matrix P
coef = []
for i in coefs:
    while len(i) < n-k:
        i = np.append(i, 0)
    coef.append(i)
#create coefs for matrix P

#create matrices
P = create_P(coef)
print(P)
P = np.transpose(P)
print(P)
Ik = generate_Ik(k, 0)
Ink = generate_Ik(n, k)
G = create_G(Ik, P)
print("matrix G is : \n" + str(G))
H = create_H(Ink, P)
print("\nmatrix H is : \n" + str(H) + "\n")
'''
#create matrices

#create coset leader
syndrome = []
for i in range(2**(n-k)):
    syndrome.append(get_syndrome(i, (n-k)))

coset = []
for i in syndrome:
    ceva = []
    i = np.matrix(i)
    ceva.append(i)
    ceva.append(search_coset(i, H, n))
    coset.append(deepcopy(ceva))
    ceva.clear()
#create coset leader

#zero syndrome
things = []
m = n
abc = ""
while m > 0:
    abc += "0"
    m -= 1
zerro = ["0", abc]
#zero syndrome

t = []
number = 0
data = []

#generate coset for each syndrome
for i in coset:
    half = []
    s = get_syndrome(number, k)
    S = ""
    for CC in s:
        S += str(CC)
    half.append(S) 
    for j in i:
        string = ""
        i = 0
        for x in j:
            string += str(x)
        half.append(string)
        i = i + 1
    data.append(deepcopy(half))
    number += 1
#generate coset for each syndrome

index = 0
tabel = []

#get the final table
for i in data:
    if index == 0:
        tabel.append(zerro)
    else:
        i[1] = i[2]
        i = i[:-1]
        tabel.append(deepcopy(i))
    index += 1
print("syndrome |", "coset leader")
for i in tabel:
    print(i)
#get the final table
'''
