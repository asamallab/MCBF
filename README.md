# MCBF

## About
MCBF stands for Minimum Complexity Boolean Functions. Read once functions (RoFs) are a type of Boolean function which possess minimum Boolean complexity. We provide here a catalog of RoFs and a code to both generate RoFs and check if a Boolean function is an RoF.


## Folder Structure
There are 2 files in this repository:
  1. RoF_catalog: This folder contains 10 files called RoF_cat_XX.tsv, where XX takes values from 01 to 10 and is the number of input variables (k) of the RoF. Each file contains the representative RoFs (upto 2^(k-1))for a given number of inputs. 
       This catalog contains properties of each representative RoF such as:
       * decimal_rep: integer encoding of the RoF.
       * bias: Hamming weight of the RoF
       * avg_sensitivity: average sensitivity.
       * CF: whether is it canalyzing.
       * NCF: whether is it nested canalyzing.
       * cana_depth: Canalyzing depth
       * expressions: the Boolean expression of the representative MBCF.
       * isomorphisms: the number of isomorphisms of the function.
  2. RoF_codes.py: Program to check if a Boolean function is a RoF, and also to generate all the representative RoFs with a given number of inputs.

## Attention
The RoF_codes.py makes use of RoF_catalog as a look-up table to check for RoFs. 

## References
<a id="1">[1]</a>

#### In case you use the codes or catalog herein, please cite the reference given above. 

