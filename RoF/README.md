# RoF: Read-once functions

Read-once are a type of Boolean function in whose expression is constructed in such that the literal (corresponding to one input) appears exactly once in it's Boolean expresison. These literals maybe positive or negated and are joined by either AND or OR operators.

## Folder Structure
There are 3 files in this folder:
  1. RoF_catalog: This folder contains 10 files called RoF_cat_XX.tsv, where X takes values 0 to 9. 'XX' refers to the number of input variables (k) of the RoF. Each file contains the representative RoFs (upto <bias img src="https://render.githubusercontent.com/render/math?math=2^{k-1}">) and their properties such as:
       * decimal_rep: integer encoding of the RoF.
       * bias: Hamming weight of the RoF.
       * avg_sensitivity: average sensitivity.
       * CF: whether is it canalyzing.
       * NCF: whether is it nested canalyzing.
       * cana_depth: Canalyzing depth
       * expressions: the Boolean expression of the representative RoF.
       * isomorphisms: the number of isomorphisms of the function.
  2. RoF_checker.py : Program to check if a Boolean function is a RoF.
  3. RoF_generator.py : and also to generate all the representative RoFs with a given number of inputs.

## Attention
The RoF_checker.py makes use of RoF_catalog as a look-up table to check for RoFs. 

## Algorithm Flowchart for the RoF_checker
<img src="RoF_checker_flowchart.png">
  
#### In case you use the codes or catalog herein, please cite the reference given above.
## CITATION

