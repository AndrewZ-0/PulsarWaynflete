import numpy as np
import matplotlib.pyplot as plt

from pulsarCatalogProcessing import get_cat, get_pInitial_arr

#Retrieve catalog database (dict)
catalog_db = get_cat()

"""print(catalog_db)"""

#get p initial array
#----------------------------------------------------------------------------------
pInitial_arr = get_pInitial_arr(catalog_db)
#----------------------------------------------------------------------------------


#Plot period against median_mass
#----------------------------------------------------------------------------------
plt.title("Median mass against barycentric period of ATNF Catalog sample")

plt.xlabel("Log median_mass (Solar Mass Units)")
x_axis = np.log10(catalog_db["median_mass"].astype("f"))

plt.ylabel("Log barycentric initial period (seconds)")
y_axis = np.log10(pInitial_arr)

plt.scatter(x = x_axis, y = y_axis, marker = ".")
plt.show()
#----------------------------------------------------------------------------------