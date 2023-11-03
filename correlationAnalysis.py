import numpy as np
import scipy.stats

from pulsarCatalogProcessing import get_cat, get_pInitial_arr

#Retrieve catalog database (dict)
catalog_db = get_cat()

"""print(catalog_db)"""

#get p initial array
#----------------------------------------------------------------------------------
pInitial_arr = get_pInitial_arr(catalog_db)
#----------------------------------------------------------------------------------


#Get x & y and remove inf values
#----------------------------------------------------------------------------------
x = catalog_db["median_mass"].astype("f")
y = pInitial_arr

i = 0
while i < len(x):
    if y[i] == np.inf:
        x = np.delete(x, i)
        y = np.delete(y, i)
    else:
        i += 1
#----------------------------------------------------------------------------------


#Correlations
#----------------------------------------------------------------------------------
#Pearson
print("")
print("[ Pearson ]")
print(">>> r:", scipy.stats.pearsonr(x, y).correlation)
print(">>> pvalue:", scipy.stats.pearsonr(x, y).pvalue)

#Spearman
print("")
print("[ Spearman ]")
print(">>> rho:", scipy.stats.spearmanr(x, y).correlation)
print(">>> pvalue:", scipy.stats.spearmanr(x, y).pvalue)

#Kendall
print("")
print("[ Spearman ]")
print(">>> tau:", scipy.stats.kendalltau(x, y).correlation)
print(">>> pvalue:", scipy.stats.kendalltau(x, y).pvalue)

print("")
#----------------------------------------------------------------------------------