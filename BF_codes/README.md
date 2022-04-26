# About
<img src="repr_BFs.png">

<b>BF_checkers.py</b> checks if a BF (Boolean function) is an EF (Effective function), UF (Unate function), CF (Canalyzing function) or NCF (Nested canalyzing function).<br/>
<b>Instances:</b><br/>
Enter the number of inputs and BF truth table as a binary string. The string from left to right is the output of the truth table from the top to bottom.

```python
>>> check_if(3,'10001010').is_EF()
True

>>> check_if(3,'00001011').is_CF()
True

>>> check_if(3,'00001011').is_UF()
'aai' # 'a':activator and  'i': inhibitor

>>> check_if(3,'00001011').conforms_to_edge_signs('aai')
True

>>> check_if(3,'11001011').is_NCF()
False
```

<b>BF_generator.py</b> generates all BFs belogning to a particular type of BF namely, EF, UF, CF and NCF.<br/>
<b>Instances:</b><br/>

```python
>>> generate(1).all_BF()
['00', '01', '10', '11']

>>> generate(1).all_EF()
['01', '10']

>>> generate(2).UF_with_sign('ai')
['0000', '0010', '0011', '1010', '1011', '1111']

>>> generate(2).all_signs_UF()
['1000', '1110', '0010', '1011', '0100', '1101', '0001', '0111']

>>> generate(2).all_CF()
['0000', '0001', '1110', '0010', '1111', '0011', '1010','0111', '1100', '1000', '0100', '1101', '1011', '0101']

>>> generate(2).all_NCF()
['0001', '1110', '0010', '0111', '1000', '0100', '1101', '1011']
```

<b>BF_properties.py</b> is used to get various aspects of BFs such as average sensitivity, it's permutations, DNF or CNF expressions, both 'full' and 'Quine-McCluskey minimized' expressions, among others.<br/>
<b>Instances:</b><br/>
```python

>>> bf(3, '10000101').avg_sensitivity() 
1.75

>>> bf(3, '11100000').is_cana_in_input(3) # Checks if the BF is canalyzing in input '3'.
'1'                                       # Input 3 is canalyzing, with the canalyzing input value equal to '1'

>>> bf(3, '11001010').right_shift() #returns a single 'right' cyclic permutation of the truth table (if 3,2,1 is the order of
'11100100'                          #the inputs, to start with; after the operation 1,3,2 will be the order of the inputs)


>>> bf(3, '11100000').swap_rows([1,3]) #negates the inputs 1 and 3
'00001101'

>>> bf(3, '11100000').all_perms()    #returns all the permutations of the BF given that all inputs have same sign 
['10101000', '11001000', '11100000'] #i.e positive or negative

>>> bf.logic_operation('1001', '1010', 0) # Combines the BFs '1001' and '1010' with the '0' (AND) operator
'1010000000001010'

>>> bf(3,'10001010' ).get_dnf()
{'full_DNF': '(~a & ~b & ~c) | (a & ~b & ~c) | (a & b & ~c)', 'QM-DNF': (a & ~c) | (~b & ~c)}

>>> bf(3,'10001010' ).get_cnf()
{'full_CNF': '(a | b | ~c) & (a | ~b | c) & (a | ~b | ~c) & (~a | b | ~c) & (~a | ~b | ~c)', 'QM-CNF': ~c & (a | ~b)}
```

### CITATION
In case you use the codes or data herein, please cite the manuscript:<br/>
Ajay Subbaroyan, Olivier C Martin, Areejit Samal, *Minimum complexity drives regulatory logic in Boolean models of living systems*, PNAS Nexus, Volume 1, Issue 1, March 2022, pgac017, https://doi.org/10.1093/pnasnexus/pgac017
