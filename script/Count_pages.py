# -*- coding: utf-8 -*-
"""
This script is used to count the number of pages of PDF files ot check if these
are compliant with the conference rules:
    - normal paper has a maximum length of 8 pages
    - 2 overlength pages are allowed by payment for a total of 10 pages
    - no papers can exceed 10 pages

The script is used with files downloaded from Microsoft CMT system.

Created on Wed Oct 23 20:04:21 2024

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import pandas as pd
import os
import IJCNN_utils as ut


# Settings
path = './data/Papers/'
dest = './report/'

save_file = dest + 'Page_Count.xlsx'


# Create a dataframe where insert all page length
df = pd.DataFrame(columns = ['ID', 'Pages', 'Overlength', 'Compliant'])


# Retrieve all files
files = os.listdir(path)
files.sort(key=ut.getID)
N_papers = len(files)


# Count the number of pages
df = ut.countPage(path, files, df)


# Save the Excel report
df.to_excel(save_file, index=False)

print("End of checking {} files".format(N_papers))
