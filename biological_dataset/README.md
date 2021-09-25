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
