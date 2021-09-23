"""
====================================================================
Program to compute check if a Boolean function is a read-once function
Written by: Ajay Subbaroyan
Reference:
====================================================================
"""
import sys
sys.path.append('..\\BF_codes')

from BF_properties import *

def create_RoF (k, prev_RoFs):
    '''
    returns RoFs for 'k' inputs 
    
    #arguments
    k: number of inputs
    prev_RoFs: the functions in the different RoFs upto k-1 as a list of lists

    Note: this is used as a sub-routine of generate_RoFs
    '''
    # Generate the RoFs (including redundancies)
    tot = {b:[] for b in range(1, 2**(k),2)}
    if k%2 == 0:
        decomp = [(i,k-i) for i in range(1,int(k/2)+1)]
    else:
        decomp = [(i,k-i) for i in range(1,int((k+1)/2))]
    for pair in decomp:
        k1,k2 = pair[0], pair[1]
        m1,m2 = prev_RoFs[k1-1], prev_RoFs[k2-1]
        for term1 in m1:
            for term2 in m2:
                bias1, bias2 = term1.count('1'), term2.count('1')
                bias_and = bias1*bias2
                bias_or = bias1*(2**k2) + bias2*(2**k1) - bias1*bias2
                q1,q2 = bf.logic_operation (term1, term2, 0), bf.logic_operation (term1,term2,1)
                tot[bias_and] += [q1]
                tot[bias_or] += [q2]
                
    #Remove redundancies using the permutations generator
    new_funcs = []
    for bias in range(1,2**k,2):
        funcs = list(set(tot[bias]))
        while (funcs != []):
            f = funcs[0]
            f_perms = bf(k,f).all_perms()
            new_funcs += [f]
            funcs = [ele for ele in funcs if ele not in f_perms]
    return new_funcs

def generate_RoFs(k):
    '''
    returns all the representative RoFs for a given number of inputs

    #arguments
    k: Number of inputs
    
    #instance
    >>> generate_RoFs(3)
    >>> ['00000001', '00000111', '00011111', '01111111']
    '''
    prev_RoFs = [['01']]
    if k == 1 :
        return prev_RoFs[0]
    else:
        for p in range(2,k+1):     
            x = create_RoF(p,prev_RoFs)
            prev_RoFs += [x]
    return x
