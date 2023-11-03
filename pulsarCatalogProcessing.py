import numpy as np

#A function that removes unneccessary witespaces, new lines from the pure txt, then splits the string into a list using: "|"
def parse_line(line):
    data = line.strip().replace(" ", "").split("|")

    #to remove "" at the start and the end of the split
    del data[0]
    del data[-1]

    return data


#A function that opens and parses the ATNF catalog
def get_cat():
    catalog_db = {}

    #Open txt file
    with open("ATNF_PulsarCatalog_(period&mass).txt", "r") as f:
        #First two lines of metedata
        #----------------------------------------------------------------------------------
        title = f.readline()
        system = f.readline()
        #----------------------------------------------------------------------------------

        #Parsing fieldnames
        #----------------------------------------------------------------------------------
        fieldNames = parse_line(f.readline())
        #----------------------------------------------------------------------------------

        #Creating empty np arrays for records
        #----------------------------------------------------------------------------------
        for i in range(len(fieldNames)):
            #string datatype used to store all data
            catalog_db[fieldNames[i]] = np.array([], dtype = "S")
        #----------------------------------------------------------------------------------

        #Parsing records
        #----------------------------------------------------------------------------------
        n_of_fields = len(fieldNames)

        while True:
            record = f.readline()

            if record == "":
                #stop if no more records left
                break 
            else:
                #continue by parsing record
                record = parse_line(record)

            #append individual elements to their fields
            for i in range(n_of_fields):
                updates_arr = np.append(catalog_db[fieldNames[i]], record[i])
                catalog_db[fieldNames[i]] = updates_arr
        #----------------------------------------------------------------------------------
    
    return catalog_db


#A function that calculates P initial
def calcluate_pInitial(period, approxCharAge, actualAge):
    return period / (1 - (approxCharAge / actualAge))

#A function that creates a P initial array using catalog_db
def get_pInitial_arr(catalog_db):
    pInitial_arr = np.array([])
    for i in range(len(catalog_db["period"])):
        period = catalog_db["period"][i].astype("f")
        age = catalog_db["age"][i].astype("f")
        corr_age = catalog_db["corr_age"][i].astype("f")

        pInitial = calcluate_pInitial(period, age, corr_age)
        pInitial_arr = np.append(pInitial_arr, pInitial)
    
    return pInitial_arr


if __name__ == "__main__":
    #Retrieve catalog database (dict)
    catalog_db = get_cat()

    """print(catalog_db)"""

    #get p initial array
    #----------------------------------------------------------------------------------
    pInitial_arr = get_pInitial_arr(catalog_db)
    #----------------------------------------------------------------------------------
