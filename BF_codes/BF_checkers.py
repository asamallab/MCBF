"""
====================================================================
Program to generate the different the different types of BFs, namely
EFs, UFs, CFs and NCFs
Written by: Ajay Subbaroyan
Reference: "Minimum complexity drives regulatory logic in Boolean models of living systems".
Ajay Subbaroyan, Olivier C. Martin, Areejit Samal, bioRxiv 2021.09.20.461164; 
doi: https://doi.org/10.1101/2021.09.20.461164
====================================================================
"""

from BF_properties import *

class check_if(bf):
    '''
    returns True or False, depending on the nature of the BF
    '''
    
    def __init__(self, k, f):
        '''
        k: number of inputs to a BF
        f: BF as a binary string : the string from left to right
        is the output of the truth table from top to bottom
        '''
        super().__init__(k,f)
        self.z = bf.indices(self)[0]   #indices of zeros 
        self.o = bf.indices(self)[1]   #indices of ones

    def is_EF(self):
        '''
        returns True if BF is an EF, else returns False

        #instance
        >>> check_if(3,'10001010').is_EF()
        >>> True
        '''
        Q = []
        for i in self.z:
            z_ele = list(itemgetter(*self.z[i])(self.f))
            o_ele = list(itemgetter(*self.o[i])(self.f))

            if z_ele == o_ele:
                 Q += [True]
            else:
                 Q += [False]
            
        if True in Q:
            return False
        else:
            return True

    def is_CF(self):
        '''
        returns True if BF is an EF, else returns False

        #instance
        >>> check_if(3,'00001011').is_CF()
        >>> True
        '''
        
        L = []
        for i in self.z:
            if bf.is_cana_in_input(self,i) != None:
                return True
        return False

    def is_UF(self):
        '''
        returns 'signs' of the inputs if BF is a UF, else returns False

        #instance
        >>> check_if(3,'00001011').is_UF()
        >>> 'aai'

        Note: 'signs' is a string having 'a','i' or 'x'.
        'a': activator, 'i': inhibitor, 'x': activator or inhibitor
        e.g in 'aai', the 1st 'a' is the input 3, the 2nd 'a' the input
        2 and the 3rd a the input 1.
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

    def conforms_to_edge_signs(self, inedges):
        '''
        returns True if BF conforms to the signs of the inputs, else returns
        False

        #arguments
        inedges: string of 'a' and 'i'.
        
        #instance
        >>> check_if(3,'00001011').conforms_to_edge_signs('aai')
        >>> True

        Note: The order of characters in the string 'inedges' are should be
        in the order in the truth table
        e.g in 'aai', the 1st 'a' is the input 3, the 2nd 'a' the input
        2 and the 3rd a the input 1.
        '''
        if self.k != len(inedges):
            return 'Incorrect number of input-edges'
        
        Q = []
        for i in self.z:
            z_ele = list(itemgetter(*self.z[i])(self.f))
            o_ele = list(itemgetter(*self.o[i])(self.f))
            if inedges[-i] == 'a':
                L = [o_ele[j] >= z_ele[j] for j in range(2**(self.k-1))]
                if False not in L:
                    Q += [True]
                else:
                    return False
            elif inedges[-i] == 'i':
                L = [o_ele[j] <= z_ele[j] for j in range(2**(self.k-1))]
                if False not in L:
                     Q += [True]
                else:
                    return False
        return True

    def is_NCF(self):
        '''
        returns True if BF is an NCF, otherwise returns False
        
        #instance
        >>> check_if(3,'11001011').is_NCF()
        >>> False
        '''
        
        if bf(self.k,self.f).cana_depth() == self.k:
            return True
        else:
            return False

    def is_any_types(self):
        return {'EF': check_if(self.k,self.f).is_EF(), 'UF': check_if(self.k,self.f).is_UF(),
                'CF': check_if(self.k,self.f).is_CF(),'NCF': check_if(self.k,self.f).is_NCF()}
