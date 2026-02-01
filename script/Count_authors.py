# -*- coding: utf-8 -*-
"""
Script used to count all the authors of accepted papers.
Be aware that authors of multiple papers could be counted several times if
names are written slightly differently.

Created on Tue Jul  1 22:49:06 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import IJCNN_utils as ut


# Set file names
path = './data/'
paper_file = path + 'All_Accepted_Papers.xlsx'


# Load paper data
papers = ut.load_submissions(paper_file)


# Main loop
L = []
for i in range(len(papers)):
    a = ut.getAuthorList2(papers.iloc[i]['Author Names'])

    b = [s.strip() for s in a]  # Remove spaces
    L = L + b    # COncat to previous authors


# Extract unique entries and count
L_unique = list(set(L))
N_auth = len(L_unique)

print('Number of accepted authors =', N_auth)
