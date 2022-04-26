"""
====================================================================
Written by: Ajay Subbaroyan
Program to compute obtain the minimal expression of Boolean functions
Ajay Subbaroyan, Olivier C Martin, Areejit Samal,
Minimum complexity drives regulatory logic in Boolean models of living systems,
PNAS Nexus, Volume 1, Issue 1, March 2022, pgac017, 
https://doi.org/10.1093/pnasnexus/pgac017
====================================================================
"""

./abc read_eqn input_BF/repBF_full_cnf032.eqn; sop; write output_BF/fact_repBF_full_cnf032.eqn
./abc read_eqn input_BF/repBF_full_dnf032.eqn; sop; write output_BF/fact_repBF_full_dnf032.eqn
./abc read_eqn input_BF/repBF_qm_cnf032.eqn; sop; write output_BF/fact_repBF_qm_cnf032.eqn
./abc read_eqn input_BF/repBF_qm_dnf032.eqn; sop; write output_BF/fact_repBF_qm_dnf032.eqn
