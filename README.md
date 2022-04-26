# MCBF

## About
MCBF repository contains the codes and dataset associated with the following manuscript:<br/>
Ajay Subbaroyan, Olivier C Martin, Areejit Samal, <br/> *Minimum complexity drives regulatory logic in Boolean models of living systems*<br/> PNAS Nexus, Volume 1, Issue 1, March 2022, pgac017, https://doi.org/10.1093/pnasnexus/pgac017 <br/>

This repository contains 4 folders which are described below.

### 1. BF_codes 
The folder contains codes to check (BF_checkers.py) and generate (BF_generators.py) different types of biologically meaningful BFs. The code (BF_properties.py) enables computations of some properties of BFs and perform various operations on them. 

### 2. Boolean_complexity
The procedure to compute the Boolean Complexity of a given BF is provided in this folder. 

### 3. RoF
The code to check if a BF is a read-once function (RoF), and to generate the representative RoFs are given in this folder. The RoF_catalog lists all representative RoFs and their various properties up to k=10 inputs. 

### 4. biological_dataset
This folder gives the reference_biological_dataset.tsv file containing details of the 2687 Boolean functions compiled from 88 discrete models in published literature. It also contains the statistical_tests.R code which is used to compute the *p*-values to show enrichment of different types of BFs.


### CITATION
In case you use the codes or data herein, please cite the manuscript:
Ajay Subbaroyan, Olivier C Martin, Areejit Samal, <br/> *Minimum complexity drives regulatory logic in Boolean models of living systems* <br/> PNAS Nexus, Volume 1, Issue 1, March 2022, pgac017, https://doi.org/10.1093/pnasnexus/pgac017
