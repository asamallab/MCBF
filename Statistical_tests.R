# PROPOSED STATISTICAL TESTS AT GIVEN k (number of inputs)

# EF: Effective functions
# UF: Unate functions
# CF: Canalyzing functions
# NCF: Nested canalyzing functions
# RoF: Read-once functions
# non-NCF RoF: RoFs which are not NCFs

# Test 1: 
# To check for an enrichment in odd biases in the empirical dataset.
# For a given k (number of inputs), consider the 2 ensembles H0 and H1.
# H0 is the set of all BF (no constraints) with the uniform measure. 
# prob_odd is the probability that an element drawn randomly under 
# H0 has odd bias.
# For the proposed choice of H0, prob_odd=0.5.
# The ensemble H1 is all the BF in the empirical dataset. 
# of M_total_k BF of which M_odd_k have odd bias. The (one sided) test 
# for enrichment in odd bias is done by determining the probability 
# that M_odd_k takes its observed value or higher under H0.

#For instance:
prob_odd=0.5
M_odd_k = 378
M_total_k = 412
pval_odd_bias <- pbinom(M_odd_k,M_total_k,prob=prob_odd,lower.tail=FALSE)

# Test 2
# T2.1: To check for an enrichment in EFs, UFs, CFs, NCFs or RoFs in the
#  empirical  dataset (Enrichment in the space of all BFs)
# T2.2: To check for an enrichment in the ratios NCF/CF or NCF/RoF  
# (Enrichment in sub types)

# For a given k (number of inputs), consider the 2 ensembles H0 and H1.
# Under H0, prob_EF, prob_UF prob_CF, prob_RoF and prob_NCF are the   
# probabilities to be EF, UF, CF, RoF or NCF within H0.
# These quantities are determined either by mathematics or by enumeration.
# Since all NCFs are in CF and in RoF, the ratios NCF/CF and NCF/RoF in H0 
# are just prob_NCF/prob_CF and prob_NCF/prob_RoF.
# The ensemble H1 is all the BF in the empirical dataset. It has a total
# of M_total_k BF of which M_CF_k are CFs, M_RoF_k are RoF and M_NCF_k are NCFs.

# Test T2.1:
# The (one sided) test for enrichment of the 5 types of BF is done by 
# determining the probability that M_EF_k, M_UF_k, M_CF_k, M_RoF_k or M_NCF_k
# take their observed values or higher under H0.

# Instance: To check for enrichment of RoFs for k = 4:
tot_RoF_k <- 832
tot_k <- 65536
M_RoF_k <- 244
M_tot_k <- 258
prob_RoF_k <- tot_RoF_k/tot_k 
pval_RoF_k <- pbinom(M_RoF_k,M_total_k,prob=prob_RoF_k,lower.tail=FALSE)

# Test T2.2:
# The (one sided) test for enrichment of the NCF type within one of the two 
# other types

# Instance: To check for specific enrichment of NCF within RoFs at k=4:
tot_NCF_k <- 736
tot_k <- 65536
M_NCF_k <- 230

prob_NCF_k <- tot_NCF_k/tot_k
prob_RoF_k <- tot_RoF_k/tot_k
pval_NCF_RoF_k <- pbinom(M_NCF_k,M_RoF_k,prob=prob_NCF_k/prob_RoF_k,lower.tail=FALSE)
