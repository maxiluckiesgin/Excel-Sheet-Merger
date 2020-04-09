import pandas as pd
import numpy as np
import os, collections, csv
from os.path import basename

# This script concatenates the sheets (named 'Table 1', 'Table 2', ... so on) of an Excel file into a single sheet. 
df = []
f = "../file_with_extra_sheet.xlsx" #Modify this. This is the path to the Excel file

#Add your desired sheet name to the list  
sheet_name_list = ['Table 1','Table 23','Table 45'] #Modify this. 

#Take the rest of the sheet without header
for sheet_name in sheet_name_list:
    data = pd.read_excel(f, sheet_name = sheet_name)
    df.append(data)

final = "../mergedfile.csv" #Path to the file in which new sheet will be saved.
df = pd.concat(df)
df.to_csv(final,index=False)
