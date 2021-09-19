import os
import math
import string
import numpy as np
import pandas as pd
from itertools import chain, combinations, permutations
from operator import itemgetter

##Abbreviations
##UF: Unate Function, NCF: Nested Canalyzing Functions,

##RoF: Read-once function

class bf:
    '''
    returns properties of the BF
    '''
    def __init__(self, k, f):
        '''
        k: Number of inputs to a node
        f: BF as a decimal/binary string
        '''
        self.k = k
        if type(f) == int:
            self.f = bin(f)[2:].zfill(2**self.k)
        else:
            self.f = f

    def indices(self):
        '''
        returns two dictionaries of the indices of the zeros and ones respectively
        for every input
        Note:'1' is the column closest to the output column and k the farthest
        '''
        z = {}
        o = {}
        L = [i for i in range(2**self.k)]
        temp = []
        for num in range(self.k):
            for i in range(0,(2**self.k),2**(num+1)):
                temp += L[i:i+2**num]
            z[num+1] = temp
            o[num+1] = list(set(L)-set(temp))
            temp = []
        return z,o

    def inps_neibs(self):
        '''
        returns a list all neighbours 1 HD away, for each vertex of the hypercube
        '''
        n = 2**self.k
        Dct = {}
        for line in range(n):
            b = bin(line)[2:].zfill(self.k)
            x = []
            for i in range(len(b)):
                if i == 0 :
                    x += [int(bin(not int(b[i]))[-1] + b[1:], 2)]
                elif i == len(b)-1:
                    x += [int (b[:-1] + bin(not int(b[i]))[-1], 2)]
                else:
                    x += [int (b[:i] + bin(not int(b[i]))[-1] + b[i+1:], 2)]
            Dct[int(b,2)] = x
        return Dct

    def avg_sensitivity(self):
        '''
        returns the average sensitivity of the BF (between 1 and k)
        '''
        I = bf.inps_neibs(self)
        tot = 0
        for pos in I:
            for neib in I[pos]:
                if self.f[neib] != self.f[pos]:
                    tot += 1
        return tot/(2**self.k)

    
    def bias(self,norm=False):
        '''
        returns the normalized/un-normalized bias
        '''
        if norm == False:
            return self.f.count('1')
        else:
            return self.f.count('1')/(2**self.k)

    def is_C_in_input(self,i):
        '''
        i: input (takes values from 1 to k)
        returns False if BF is not canalyzing in input 'i'
        '''
        self.z = bf.indices(self)[0]   #indices of zeros 
        self.o = bf.indices(self)[1]   #indices of ones

        z_ele = list(itemgetter(*self.z[i])(self.f))
        o_ele = list(itemgetter(*self.o[i])(self.f))
        
        is_c_z = all(bit == z_ele[0] for bit in z_ele) 
        is_c_o = all(bit == o_ele[0] for bit in o_ele)
        
        if is_c_z and is_c_o:
            return '01'
        elif is_c_z:
            return '0'
        elif is_c_o:
            return '1'

    def C_depth (self):
        '''
        returns the canalyzing depth of the BF
        '''

        if self.k == 1:
            if self.f =='01' or self.f == '10':
                return 1
            else:
                return 0

        if self.f.count('0') == 2**self.k or self.f.count('1') == 2**self.k:
            return 0
        
        else:
            for i in range(1,self.k+1):
                if bf.is_C_in_input(self, i) == '0': # canalyzing input is '0'
                    self.f = ''.join(itemgetter(*self.o[i])(self.f))
                    self.k -= 1
                    return bf.C_depth(self) + 1
                
                elif bf.is_C_in_input(self, i) == '1': #canalyzing input is '1'
                    self.f = ''.join(itemgetter(*self.z[i])(self.f))
                    self.k -= 1
                    return bf.C_depth(self) + 1
                
                elif bf.is_C_in_input(self, i) == '01': #canalyzing inputs are '0' and '1'
                    return 1                    #This implies that the remaining
                                                #inputs are non-canalyzing
                
        return 0        

    def right_shift (self):
        '''
        returns a single 'right' cyclic permutation of the truth table
        '''
        m = int(len(self.f)/2)
        upper_half, lower_half = self.f[:m], self.f[m:]
        perm = ''
        for i in range(m):
            perm += upper_half[i] + lower_half[i]
        return perm

    def swap_rows (self,cols):
        '''
        cols: the inputs to be negated
        returns a BF with the inputs 'cols' negated 
        '''
        I = bf.indices(self)
        str_lst = list(self.f)    
        for col in cols:
            I0, I1 = I[0][col], I[1][col]  
            for i in range(len(I0)):
                str_lst[I0[i]], str_lst[I1[i]] =  str_lst[I1[i]], str_lst[I0[i]] 
        return ''.join(str_lst)

    def pos_BF_perms(self,n):
        '''
        n: Number of inputs to be permuted.
        returns the isomorphisms of BF with positive literals, for a given 'n'
        '''
        if n == 1:
            return ''
        
        else:
            parts = [self.f[i:i+2**n] for i in range(0,2**self.k,2**n)]
            perms_k = [self.f]
            for times in range(1,n):
                perms_k += [''.join([bf(self.k,part).right_shift() for part in parts])]
                self.f = perms_k[-1]
                parts = [self.f[i:i+2**n] for i in range(0,2**self.k,2**n)]
            Q = list(set(perms_k))
            return Q
    
    def all_BF_isomorphisms (self):
        '''
        returns all the permutations of the BF
        '''
        n = self.k
        L_tot = bf(self.k,self.f).pos_BF_perms(n)
        L_new = L_tot
        for n in range(self.k-1,1,-1):
            L_new = list(set(chain(*[bf(self.k,f).pos_BF_perms(n) for f in L_new])))
            L_tot = list(set(L_tot + L_new))
        return L_tot
    
    def logic_operation (a,b,operation):
        '''
        i/p: a and b are 2 string of '0's and '1s' operation : AND(0) or OR(1)
        o/p: a string of 0's and 1's of size len(a)*len(b)
        '''
        a1 = np.array([int(ele) for ele in a])
        b1 =  np.array([int(ele) for ele in b])
        
        if operation == 0:
            q = np.tensordot(a1, b1, axes= 0)
            q.shape = len(a1)*len(b1)
            return ''.join(list(map(str,q)))
        
        else:
            q = [np.logical_or(ele_a1, ele_b1) for ele_a1 in a1 for ele_b1 in b1]
            return ''.join([str(int(ele)) for ele in q])
        
class check_if(bf):
    '''
    returns True or False, depending on the nature of the BF
    '''
    def __init__(self, k, f):
        super().__init__(k,f)
        self.z = bf.indices(self)[0]   #indices of zeros 
        self.o = bf.indices(self)[1]   #indices of ones

    def is_UF(self):
        '''
        returns 'signs' of the inputs, else returns False if BF is not UF
        (if 'x' is present in the output, it signifies that that input is
        ineffective)
        '''
        Q = ''
        for i in self.z:
            z_ele = list(itemgetter(*self.z[i])(self.f))
            o_ele = list(itemgetter(*self.o[i])(self.f))

            La = [o_ele[j] >= z_ele[j] for j in range(2**(self.k-1))]
            Li = [o_ele[j] <= z_ele[j] for j in range(2**(self.k-1))]
            
            if False in La and False in Li:
                return False
            elif False in La and False not in Li:
                Q = 'i' + Q
            elif False not in La and False in Li:
                Q = 'a' + Q
            else:
                Q = 'x' + Q
        return Q

    def is_NCF(self):
        '''
        returns True/False if BF is an NCF or not respectively
        '''
        if bf(self.k,self.f).C_depth() == self.k:
            return True
        else:
            return False

    def is_RoF(self):
        '''
        This program uses the database of RoFs to check if a BF is an RoF.
        f: BF
        returns True/False if BF is RoF or not respectively.
        '''
        bias = bf(self.k,self.f).bias()

        #Set the catalog number
        if self.k < 10:
            num =  '0' + str(self.k)
        else:
            num = self.k
        
        #Check if the bias is even: if so, the BF is not an RoF
        if bias%2 == 0:
            return ('The BF is not a RoF')
        
        else:
            # Checks if the BF is an NCF
            if bf(self.k,self.f).C_depth() == self.k: 
                return ('The BF is a NCF')

            # Complement the BF if the bias is greater than 2^(k-1)
            else:
                if bias > 2**(self.k-1):
                    f = ''.join([self.f.replace('0','X').replace('1','0').replace('X', '1')])
                    bias = 2**self.k - bias
                else:
                    f = self.f
                
                signs = check_if(self.k,f).is_UF()
                
                #Check if the BF is a unate function
                if signs == False:
                    return ('The BF is not a RoF')

                else:
                    #Select all RoFs with the same bias and average sensitivity
                    db = pd.read_csv('RoF_catalog/RoF_cat_'+num+'.tsv', sep = '\t')
                    db_bias = db[db['bias'] == bias]
                    avg_sen = bf.avg_sensitivity(self)
                    if avg_sen not in list(db_bias['avg_sensitivity']):
                        return ('The BF is not a RoF')
              
                    else:
                        #Generate the list of isomorphisms of the RoF and check if the input BF is present in this list
                        F = [bin(int(ele))[2:].zfill(2**self.k) for ele in list(db_bias[db_bias['avg_sensitivity'] == avg_sen].decimal_rep)]
                        cols = [self.k-ind for ind,val in enumerate(signs) if val == 'i']
                        positive_f = bf(self.k,f).swap_rows(cols)
                        for f_db in F:
                            n = self.k
                            L = bf(self.k,f_db).pos_BF_perms(n)
                            if positive_f in L:
                                return ('The BF is a non-NCF RoF')
                            for n in range(self.k-1,1,-1):
                                L = list(set(chain(*[bf(self.k,func).pos_BF_perms(n) for func in L])))
                                if positive_f in L:
                                    return ('The BF is a non-NCF RoF')
                        return ('The BF is not a RoF')

class generate(bf):
    def __init__(self, k):
        self.k = k

    def create_RoF (k, prev_RoFs):
        '''
        k: number of inputs
        prev_RoFs: the functions in the different RoFs upto k-1 as a list of lists
        '''
        # Generate the RoFs
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
                    
        #Removing redundancies
        new_funcs = []
        for bias in range(1,2**k,2):
            funcs = list(set(tot[bias]))
            while (funcs != []):
                f = funcs[0]
                f_perms = bf(k,f).all_BF_isomorphisms()
                new_funcs += [f]
                funcs = [ele for ele in funcs if ele not in f_perms]
        return new_funcs
    
    def rep_RoF (self):
        '''
        returns all the representative RoFs for a given number of inputs
        '''
        prev_RoFs = [['01']]
        if self.k == 1 :
            return prev_RoFs[0]
        else:
            for p in range(2,self.k+1):     
                x = generate.create_RoF(p,prev_RoFs)
                prev_RoFs += [x]
        return x
