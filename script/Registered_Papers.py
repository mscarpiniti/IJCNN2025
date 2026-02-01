# -*- coding: utf-8 -*-
"""
This script is used to generate a list of all registered papers at IJCNN 2025.
It is used in conjuction with:
- a file containing al the accepted papers
- a file contained all IDs registered by authors

Created on Wed May 14 22:58:52 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import pandas as pd
import IJCNN_utils as ut


# Set file names
path = './data/'
dest = './report/'
file_ID = path + 'Registered_ID.xlsx'
file_paper = path + 'All_Accepted_Papers.xlsx'

reg_file = dest + 'Registered_Papers.xlsx'


# Load data
reg_ID = pd.read_excel(file_ID)
papers = ut.load_submissions(file_paper)


IDs = list(reg_ID['ID'])
print('There are {} registered IDs'.format(len(IDs)))

papers = papers.drop(['Abstract', 'Primary Contact', 'Primary Contact Email',
       'Author Names', 'Author Emails'], axis=1)
papers.set_index('ID', inplace=True)

reg_papers = papers.copy()


# Loop over registered IDs
e = 0
for i in papers.index:
    try:
        if i not in IDs:
            reg_papers.drop(i, axis=0, inplace=True)
    except KeyError:
        e += 1
        continue

print('There are {} unrecognized IDs'.format(e))
print('There are {} registered papers'.format(len(reg_papers)))
reg_papers.to_excel(reg_file)
