# About

BF_checkers.py checks if a BF(Boolean function) is an EF (Effective function), UF (Unate function), CF (Canalyzing function) or NCF (Nested canalyzing function).

Examples:
Enter the number of inputs and BF truth table as *string* of bits.

>>> check_if(3,'10001010').is_EF()
True

>>> check_if(3,'00001011').is_CF()
True

>>> check_if(3,'00001011').is_UF()
'aai'

>>> check_if(3,'00001011').conforms_to_edge_signs('aai')
True

>>> check_if(3,'11001011').is_NCF()
False

BF_generator.py generates all BFs belogning to a particular type of BF: EF, UF, CF and NCF.

Examples:

BF_properties.py is used to get various aspects of BFs such as average sensitivity, neighbors of each vertex of the hypercube, it's isomorphisms, dnf or cnf expressions (both 'full' and 'Quine-McCluskey minimized' expressions) and canalyzing depth.

<img src="repr_BFs.png">

In case you use the codes or data or catalog herein, please cite the reference given below:

## CITATION
A. Subbaroyan, O.C. Martin, A. Samal. Minimum complexity drives regulatory logic in Boolean models of living systems.
