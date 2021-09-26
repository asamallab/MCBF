# PROPOSED STATISTICAL TESTS AT GIVEN k (number of inputs)

# EF: Effective functions
# UF: Unate functions
# CF: Canalyzing functions
# NCF: Nested canalyzing functions
# RoF: Read-once functions
# non-NCF RoF: RoFs which are not NCFs

# For a given k (number of inputs), consider the 2 ensembles H0 and H1.
# H0 is the set of all BF (no constraints) with the uniform measure. 
# The ensemble H1 corresponds to the BFs in the reference biological dataset and is 
# equal to M_total_k for k input BFs.
# The (one sided) test for the enrichment in a particular BF is done by determining
# the probability that the BF takes its observed value (in H1) or higher under H0.

# Test1
# To check for an enrichment in EFs, UFs, CFs, NCFs or RoFs in the
# reference biological dataset (Enrichment in the space of all BFs)

# For a given k (number of inputs), consider the 2 ensembles H0 and H1.
# Under H0, prob_odd, prob_EF, prob_UF prob_CF, prob_RoF and prob_NCF are the   
# probabilities to be odd-biased, EF, UF, CF, RoF or NCF within H0.
# These quantities are determined either by mathematics or by enumeration.
# The ensemble H1 are the BF in the reference biological dataset. It has a total
# of M_total_k BF of which M_odd_k are odd biased, M_EF_k are the EFs, M_UF_k are the
# UFs, M_CF_k are CFs, M_RoF_k are RoF and M_NCF_k are NCFs.

# The (one sided) test for enrichment of these types of BF is done by 
# determining the probability that M_odd_k, M_EF_k, M_UF_k, M_CF_k, M_RoF_k or M_NCF_k
# take their observed values or higher under H0.

# Instance: To check for enrichment of RoFs for k = 4:
tot_RoF_k <- 832
tot_k <- 65536
M_RoF_k <- 244
M_tot_k <- 258
prob_RoF_k <- tot_RoF_k/tot_k 
pval_RoF_k <- pbinom(M_RoF_k,M_total_k,prob=prob_RoF_k,lower.tail=FALSE)


# Test 2: Enrichment within sub-types
# Since all NCFs are in CF and in RoF, the ratios NCF/CF and NCF/RoF in H0 
# are just prob_NCF/prob_CF and prob_NCF/prob_RoF.
# The (one sided) test for enrichment of the NCF type within one of the two 
# other types is done as follows:

# Instance: To check for specific enrichment of NCF within RoFs at k=4:
tot_NCF_k <- 736
tot_k <- 65536
M_NCF_k <- 230

prob_NCF_k <- tot_NCF_k/tot_k
prob_RoF_k <- tot_RoF_k/tot_k
pval_NCF_RoF_k <- pbinom(M_NCF_k,M_RoF_k,prob=prob_NCF_k/prob_RoF_k,lower.tail=FALSE)
