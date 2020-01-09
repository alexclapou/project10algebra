from texttable import Texttable
from codewords import *

def binary_list(number, k):
    '''
    convert a decimal number to a binary as a list of k elements
    parameters:
        number - a number
        k - given k
    output:
        binary_string - binary list with k elements
    '''
    number_list = []
    while number:
        number_list.append(number % 2)
        number //= 2
    while len(number_list) < k:
        number_list.append(0)
    last_list = []
    i = len(number_list) - 1
    while i >= 0:
        last_list.append(number_list[i])
        i -= 1
    return last_list

def dec_to_bin(number):
    if number < 2:
        return number
    else:
        if number % 2 == 0:
            return 10 * dec_to_bin(number // 2)
        else:
            return 1 + 10 * dec_to_bin(number // 2)

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

def everything(index, n, k):
    base_2 = binary_list(index, k)
    code = dec_to_bin(index)
    mx = calculate_mX(p, code, n, k)
    r = calculate_r(mx, p)
    r = Z2X(r)
    v = calculate_v(mx, r)
    return v
p = ""
n = int(input("n = "))
k = int(input("k = "))
p = write_polynomial(p)
table = []
code_words = 2**k
index = 0
nmk = power_nmk(n, k)
while index < code_words:
    v = everything(index, n, k)
    print(v)
    index += 1
