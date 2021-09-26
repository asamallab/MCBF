### Reference_biological_dataset.tsv
This file contains the database of 2687 Boolean functions (BFs) compiled from 88 discrete models of biological systems. The models were compiled from various sources including the <a href="https://cellcollective.org/">Cell Collective</a>, <a href="http://ginsim.org/">GINSIM</a>, <a href="https://www.ebi.ac.uk/biomodels/">BioModels</a> and also by manual curation of published literature. The columns in this file are as follows:</br>
- Node_name: name of the node as given in the model
- *k*: number of inputs to the node
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
- PMID: The PMID of the model to which the node under consideration belongs. 
- BF_as_integer: The integer encoding of the BF

The EF, UF, CF, EUF, ECF, UCF, EUCF, NCF and RoF columns take the value TRUE if the BF from the dataset belongs to that category, else it is FALSE. 

### Statistical_tests.R
The code used to check for the enrichment of different types of BFs in the space of all BFs, and also for the enrichment of certain BFs within subtypes (for instance NCFs within CFs) by computing *p*-values.
