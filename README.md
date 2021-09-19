# MCBF

## About
MCBF stands for Minimum Complexity Boolean Functions. The read once functions (RoFs) are a type of Boolean function which possess minimum Boolean complexity.
The RoF (read-once function) catalog contains a list of the *representative* RoFs and their various properties. 

## Folder Structure
There are 2 files in this repository:
  1. RoF_catalog: This folder contains 10 files called RoF_cat_XX.tsv, where XX takes values from 01 to 10. 
       It contains properties of every representative RoF such as:
       * decimal_rep: integer encoding of the RoF.
       * bias: Hamming weight of the RoF
       * avg_sensitivity: average sensitivity.
       * CF: whether is it canalyzing.
       * NCF: whether is it nested canalyzing.
       * cana_depth: Canalyzing depth
       * expressions: the Boolean expression of the representative MBCF.
       * isomorphisms: the number of isomorphisms of the function.
  2. RoF_codes.py: Program to generate and check if a Boolean function is a RoF.

## Attention
The RoF_codes.py makes use of RoF_catalog as a look-up table.  

## References
<a id="1">[1]</a>

#### In case you use the codes or database herein, please cite the reference given above. 

