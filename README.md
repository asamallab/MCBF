# MCBF

## About
MCBF stands for Minimum Complexity Boolean Functions. Read once functions (RoFs) are a type of Boolean function which possess minimum 'Boolean complexity'. We provide here a catalog of RoFs and a code to both generate RoFs and check if a Boolean function is an RoF.


## Folder Structure
There are 2 files in this repository:
  1. RoF_catalog: This folder contains 10 files called RoF_cat_XX.tsv, where X takes values 0 to 9. 'XX' refers to a input variables (k) of the RoF. Each file contains the representative RoFs (upto <img src="https://render.githubusercontent.com/render/math?math=2^{k-1}">) and their properties such as:
       * decimal_rep: integer encoding of the RoF.
       * bias: Hamming weight of the RoF.
       * avg_sensitivity: average sensitivity.
       * CF: whether is it canalyzing.
       * NCF: whether is it nested canalyzing.
       * cana_depth: Canalyzing depth
       * expressions: the Boolean expression of the representative RoF.
       * isomorphisms: the number of isomorphisms of the function.
  2. RoF_codes.py: Program to check if a Boolean function is a RoF, and also to generate all the representative RoFs with a given number of inputs.

## Attention
The RoF_codes.py makes use of RoF_catalog as a look-up table to check for RoFs. 

## References
<a id="1">[1]</a>

#### In case you use the codes or catalog herein, please cite the reference given above.
