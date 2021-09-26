"""
====================================================================
Written by: Ajay Subbaroyan
Program to compute obtain the minimal expression of Boolean functions
Reference: "Minimum complexity drives regulatory logic in Boolean models of living systems".
Ajay Subbaroyan, Olivier C. Martin, Areejit Samal, bioRxiv 2021.09.20.461164; 
doi: https://doi.org/10.1101/2021.09.20.461164
====================================================================
"""

./abc read_eqn input_BF/repBF_full_cnf032.eqn; sop; write output_BF/fact_repBF_full_cnf032.eqn
./abc read_eqn input_BF/repBF_full_dnf032.eqn; sop; write output_BF/fact_repBF_full_dnf032.eqn
./abc read_eqn input_BF/repBF_qm_cnf032.eqn; sop; write output_BF/fact_repBF_qm_cnf032.eqn
./abc read_eqn input_BF/repBF_qm_dnf032.eqn; sop; write output_BF/fact_repBF_qm_dnf032.eqn
