# -*- coding: utf-8 -*-
"""
This script is used to make the list of all authors of acceptad papers at
IJCNN 2025 (e.g., for using in the proceedings).
It is used with the submission file downloaded from Microsoft CMT system.

Created on Sat Jun 21 13:21:44 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import pandas as pd
import IJCNN_utils as ut


# Set file names
path = './data/'
dest = './report/'
paper_file = path + 'All_Accepted_Papers.xlsx'
author_file1 = dest + 'Authors_list_all.xlsx'
author_file2 = dest + 'Authors_list.xlsx'


# Load paper data
papers = ut.load_submissions(paper_file)


# Define all the columns of the file format
columns = ['First Name', 'Last Name', 'Paper ID']

# Create empty lists
F_NAMES = []
L_NAMES = []
IDs = []


# %% Main loop
for i in range(len(papers)):
    idx = papers.iloc[i]['ID']
    a = ut.getAuthorList(papers.iloc[i]['Author Names'])

    for j in range(len(a)):
        s = a[j].split(',')
        F_NAMES.append(s[1].strip().title())
        L_NAMES.append(s[0].strip().title())
        IDs.append(idx)


# Create a first DataFrame with First Name, Last Name, and Paper ID
df1 = pd.DataFrame(zip(F_NAMES,L_NAMES,IDs), columns=columns)

# Create a second DataFrame with only First Name and Last Name
df2 = pd.DataFrame(zip(F_NAMES,L_NAMES), columns=columns[:2])


# Remove duplicates from the data in second DataFrame
df2.drop_duplicates(inplace=True)


# Save the two DataFrames as excel files
df1.to_excel(author_file1, index=False)
df2.to_excel(author_file2, index=False)
