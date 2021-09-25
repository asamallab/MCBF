"""
====================================================================
Program to generate the different the different types of BFs, namely
EFs, UFs, CFs and NCFs
Written by: Ajay Subbaroyan
Reference: A. Subbaroyan, O. C. Martin, A. Samal. Minimum complexity 
drives regulatory logic in Boolean models of living systems. 
====================================================================
"""

from BF_properties import *

class generate:
    '''
    returns a list of various kinds of BFs
    '''
    def __init__(self, k):
        self.k = k

    def all_BF(self):
        '''
        returns all the 2^(2^k) BFs. Works upto k=4

        #instance
        >>> generate(1).all_BF()
        >>> ['00', '01', '10', '11']
        '''
        L = []
        func = 2**(2**self.k)
        for integer in range(func):
            b = bin(integer)[2:].zfill(2**self.k)
            L+=[b]
        return L
    
     def all_EF(self):
        '''
        returns all the EFs with k inputs. Works upto k=4

        #instance
        >>> generate(1).all_EF()
        >>> ['01', '10']
        '''
        A = generate(self.k).all_BF()
        L = [func for func in A if check_if(self.k,func).is_EF()]
        return L

    def UF_temp (inedge, uf):
        '''
        returns the UFs for k inputs
        
        #arguments
        inedge: 'i' or 'a' (kth element in the string)
        uf    : UFs for k-1 inputs
        o/p   : UFs for k inputs

        Note: this is used as a routine for UF_with_sign hence no
        instance is given
        '''
        if inedge == 'a':
            newuf = [f1+f2 for f1 in uf for f2 in uf if np.all(np.array(list(f2)) >= np.array(list(f1)))] 
        else:
            newuf = [f1+f2 for f1 in uf for f2 in uf if np.all(np.array(list(f2)) <= np.array(list(f1)))] 
        return newuf

    def UF_with_sign (self, inedges):
        '''
        returns all the UFs with a given sign combination

        #arguments
        inedges: composed only of 'a' or 'i'. The order of characters
        in the string indicates the order in the truth table

        #instance
        >>> generate(2).UF_with_sign ('ai')
        ['0000', '0010', '0011', '1010', '1011', '1111']
        '''
        if self.k != len(inedges):
            return 'Incorrect number of input-edges'

        inedge = inedges[-1]
        
        if inedge == 'a':
            uf = ['00','01','11']
        else:
            uf = ['00','10','11']

        if self.k == 1:
            return uf
        else:
            for i in range(self.k-2,-1,-1):
                inedge = inedges[i]
                uf = generate.UF_temp(inedge, uf)
            return uf

    def unique_permutations (self):
        '''
        returns the unique permutations of inedges for all k

        #instance
        >>> generate(2).unique_permutations ()
        >>> ['ii', 'ai', 'ia', 'aa']
        '''
        uniq_str = ['a'*i + 'i'*(self.k-i) for i in range(self.k+1)]
        Z = []
        for string in uniq_str:
            q = list(permutations(string))
            for perm in q:
                z = ''.join(perm)
                if z not in Z:
                    Z += [z]
        return Z

    def all_signs_UF (self):
        '''
        returns all the UFs pooling all sign combinations

        #instance
        >>> generate(2).all_signs_UF ()
        ['1000', '1110', '0010', '1011', '0100', '1101', '0001', '0111']
        '''
        uf, ueff = [], []
        Perms = generate.unique_permutations(self)
        Dk = {a:0 for a in range(0,self.k+1)}
        for inedges in Perms:
            temp = generate.UF_with_sign(self,inedges)
            uf += temp
        uf = list(set(uf))
        return uf

    def all_CF (self):
        '''
        returns all CFs with 'k' inputs for k < 5

        #instance
        >>> generate(2).all_CF
        >>> ['0000', '0001', '1110', '0010', '1111', '0011', '1010',
             '0111', '1100', '1000', '0100', '1101', '1011', '0101']
        
        '''
        v1,v2 = 2**(self.k)*['0'],2**(self.k)*['0']
        I = bf.indices(self)
        z,o = I[0], I[1]
        F,Q = generate.all_BF(self), []
        for i in range(1,self.k+1):
            for bit in ['0','1']:
                for f in F:
                    for j in range(2**(self.k-1)):
                        v1[z[i][j]] = bit
                        v2[o[i][j]] = bit
                        v1[o[i][j]] = f[j]
                        v2[z[i][j]] = f[j]
                    Q += [''.join(v1),''.join(v2)]
        return list(set(Q))

    def NCF_funcs (self, j, ncf):
        '''
        returns a list of NCFs for j inputs
        
        #arguments
        j: number of inputs
        ncf: the list of NCFs for j-1 inputs

        Note: this is used as a routine for all_NCF hence no
        instance is given
        '''
        temp = []
        new_ncf = []
        if j == 1:
            return ['01', '10']
        else:
            ones = (2**(j-1))*'1'
            zeros = (2**(j-1))*'0'
            
            for ele in ncf:
                temp+=[ones+ele,ele+ones,zeros+ele,ele+zeros]
            new_ncf+=temp
            
            for num in range(j-1):
                temp = [generate.NCF_perm(self,ele) for ele in temp]
                new_ncf+=temp
                
            new_ncf = list(set(new_ncf))
            return new_ncf

    def NCF_perm (self, ncf):
        '''
        returns the permutations of BFs in the list 'ncf'

        #argument
        ncf: list of NCFs
        
        Note: this is used as a routine for all_NCF hence no
        instance is given
        '''
        perm_ncf = ''
        k = int(len(ncf)/2)
        for i in range(k):
            perm_ncf += ncf[i]+ncf[i+k]
        return perm_ncf
    
    def all_NCF (self):
        '''
        returns all the NCFs for a given number of inputs

        #instance
        >>> generate(2).all_NCF ()
        >>> ['0001', '1110', '0010', '0111', '1000', '0100', '1101', '1011']        
        '''
        ncf = ['01', '10']
        if self.k == 1:
            return ncf
        else:
            for num in range(2,self.k+1):
               ncf = generate.NCF_funcs(self, num, ncf)
            return ncf    
