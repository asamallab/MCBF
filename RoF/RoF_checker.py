'''
====================================================================
Program to check if a Boolean function is a RoF for some given number
of inputs
Written by: Ajay Subbaroyan
Reference: "Minimum complexity drives regulatory logic in Boolean models of living systems".
Ajay Subbaroyan, Olivier C. Martin, Areejit Samal, bioRxiv 2021.09.20.461164; 
doi: https://doi.org/10.1101/2021.09.20.461164
====================================================================
'''

import sys
sys.path.append('..\\BF_codes')

from BF_properties import *
from BF_checkers import *

from pandas import read_csv

def is_RoF(k,f):
    '''
    returns whether a BF is an RoF or a particular sub-type of RoF which
    are:the NCFs or non-NCF RoFs
    It uses the properties and the catalog of RoFs to check if a BF is a
    RoF

    #arguments
    k: Number of Inputs
    f: BF as a binary string : the string from left to right
    is the output of the truth table from top to bottom
    
    #instance
    >>> is_RoF (3, '11001101')
    >>> 'The BF is not a RoF'
    '''

    bias = bf(k,f).bias()

    #Set the catalog number
    if k < 10:
        num =  '0' + str(k)
    else:
        num = k
    
    #Check if the bias is even: if so, the BF is not an RoF
    if bias%2 == 0:
        return ('The BF is not a RoF')
    
    else:
        # Checks if the BF is an NCF
        if bf(k,f).cana_depth() == k: 
            return ('The BF is a NCF')

        # Complement the BF if the bias is greater than 2^(k-1)
        else:
            if bias > 2**(k-1):
                f = ''.join([f.replace('0','X').replace('1','0').replace('X', '1')])
                bias = 2**k - bias
            else:
                f = f
            
            signs = check_if(k,f).is_UF()
            
            #Check if the BF is a unate function
            if signs == False:
                return ('The BF is not a RoF')

            else:
                #Select all RoFs with the same bias and average sensitivity
                db = read_csv('RoF_catalog/RoF_cat_'+num+'.tsv', sep = '\t')
                db_bias = db[db['bias'] == bias]
                avg_sen = bf(k,f).avg_sensitivity()
                if avg_sen not in list(db_bias['avg_sensitivity']):
                    return ('The BF is not a RoF')
          
                else:
                    #Generate the list of isomorphisms of the RoF and check if the input BF is present in this list
                    F = [bin(int(ele))[2:].zfill(2**k) for ele in list(db_bias[db_bias['avg_sensitivity'] == avg_sen].decimal_rep)]
                    cols = [k-ind for ind,val in enumerate(signs) if val == 'i']
                    positive_f = bf(k,f).swap_rows(cols)
                    for f_db in F:
                        n = k
                        L = bf(k,f_db).some_perms(n)
                        if positive_f in L:
                            return ('The BF is a non-NCF RoF')
                        for n in range(k-1,1,-1):
                            L = list(set(chain(*[bf(k,func).some_perms(n) for func in L])))
                            if positive_f in L:
                                return ('The BF is a non-NCF RoF')
                    return ('The BF is not a RoF')
