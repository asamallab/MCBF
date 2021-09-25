# MCBF

## About
MCBF repository contains the codes and dataset associated with the following manuscript:

"Minimum complexity drives regulatory logic in Boolean models of living systems".
Ajay Subbaroyan, Olivier C. Martin, Areejit Samal,
bioRxiv 2021.09.20.461164; doi: https://doi.org/10.1101/2021.09.20.461164

In this repository we provide codes to study certain types of biologically meaningful Boolean functions, namely: read-once functions (RoFs) and the nested canalyzing functions (NCFs). The other types of biologically meaningful functions are EF (Effective function), UF (Unate function) and CF (Canalyzing function).

### BF_codes 
The checkers (BF_checkers.py) and generators (BF_generators.py) of the different types of BFs are given in this folder. BF_properties are the codes to get some properties fo BFs and perform various operations on them. 

### Boolean_complexity
The procedure to compute the Boolean Complexity is given in this folder. 

### RoF
The code to check if a BF is an RoF, and to generate the representative RoFs are given here. The RoF_catalog list all the representative RoFs and their various properties upto 10 inputs. 

### Reference_biological_dataset.tsv
This contains the 2687 Boolean functions compiled from 88 models which have been recontructed from biological data. They include models from various sources including the CellCollective, GINSIM, BioModels and also by manual curation.

### Statistical_tests.R
The code used to check for the enrichment of different types of BFs in the space of all BFs, and also for the enrichment of certain BFs within subtypes (for instance NCFs within CFs) by computing *p*-values.


In case you use the codes or data or catalog herein, please cite the reference given below: 

## CITATION
"Minimum complexity drives regulatory logic in Boolean models of living systems". Ajay Subbaroyan, Olivier C. Martin, Areejit Samal, bioRxiv 2021.09.20.461164; doi: https://doi.org/10.1101/2021.09.20.461164
