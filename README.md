# MCBF

## About
MCBF repository contains the codes and dataset associated with the following manuscript:

"Minimum complexity drives regulatory logic in Boolean models of living systems".
Ajay Subbaroyan, Olivier C. Martin, Areejit Samal,
bioRxiv 2021.09.20.461164; doi: https://doi.org/10.1101/2021.09.20.461164

### BF_codes 
The checkers (BF_checkers.py) and generators (BF_generators.py) of the different types of BFs are given in this folder. BF_properties are the codes to get some properties fo BFs and perform various operations on them. 

### Boolean_complexity
The procedure to compute the Boolean Complexity is given in this folder. 

### RoF
The code to check if a BF is an RoF, and to generate the representative RoFs are given here. The RoF_catalog list all the representative RoFs and their various properties upto 10 inputs. 

### Reference_biological_dataset.tsv
This contains the 2687 Boolean functions compiled from 88 models which have been recontructed from biological data. They include models from various sources including the CellCollective, GINSIM, BioModels and also by manual curation. The columns in this file are:

Node_name: name of the node as given in the model
- *k* : number of inputs to the node
- Bias: number of 1s in the output column of the truth table of the BF
- EF: Effective functions
- UF: Unate functions
- CF: Canalyzing functions
- EUF: Effective and unate functions
- ECF: Effective and canalyzing functions
- UCF: Unate and canalyzing functions
- EUCF: Effective, unate and canalyzing functions
- NCF: Nested canalyzing functions
- RoF: Read-once functions
- PMID : The PMID of the model to which the node under consideration belongs. 
- BF_as_integer: The integer encoding of the BF

The EF, UF, CF, EUF, ECF, UCF, EUCF, NCF and RoF columns take the value TRUE if the BF from the dataset belongs to that category, else it is FALSE. 


### Statistical_tests.R
The code used to check for the enrichment of different types of BFs in the space of all BFs, and also for the enrichment of certain BFs within subtypes (for instance NCFs within CFs) by computing *p*-values.


In case you use the codes or data or catalog herein, please cite the reference given below: 

## CITATION
"Minimum complexity drives regulatory logic in Boolean models of living systems". Ajay Subbaroyan, Olivier C. Martin, Areejit Samal, bioRxiv 2021.09.20.461164; doi: https://doi.org/10.1101/2021.09.20.461164
