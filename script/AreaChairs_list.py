# -*- coding: utf-8 -*-
"""
This script is used to make the list of all Area Chairs at IJCNN 2025
(e.g., for recognition in the the program).
It is used with the submission file downloaded from Microsoft CMT system.

Created on Mon Apr 28 12:11:48 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import pandas as pd
import IJCNN_utils as ut


# Set file names
path = './data/'
dest = './report/'
file = path + 'AreaChair_AllTracks_OnlyContributing.xlsx'
output_file_txt = dest + 'List_AC.txt'


# Read the Area Chairs
df = pd.read_excel(file)

# Extract the Area Chairs
AC_ser = ut.extract_users(df)

# Save the list of Area Chairs
AC_ser.to_csv(output_file_txt, sep='\t', header=False, index=False)
