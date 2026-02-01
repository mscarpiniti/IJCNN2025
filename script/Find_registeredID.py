# -*- coding: utf-8 -*-
"""
This script is used to retrieve IDs of papers whose authors have been registered
but did not explicitly write their papers' ID.
It is used in conjuction with:
- a file containing al the accepted papers
- a file contained all IDs registered by authors
- a file containing all the authors informations that did not indicate the ID

Created on Tue May 20 19:51:54 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import pandas as pd
import IJCNN_utils as ut


# Set file names
path = './data/'
dest = './report/'
file_paper = path + 'All_Accepted_Papers.xlsx'
file_ID = path + 'Registered_ID.xlsx'
file_NoID = path + 'No_ID.xlsx'

file_new = dest + 'New_IDs.xlsx'


# Load data
papers = ut.load_submissions(file_paper)
reg_ID = pd.read_excel(file_ID)
df = pd.read_excel(file_NoID)


# Find Authors' surnames with no IDs
surnames = []

for i in range(len(df)):
    nn = df.iloc[i]['Full Name']
    surnames.append(nn.split(',')[0])


# Extract Authors' surnames from the list of papers
authors = []
IDs  = []
for j in range(len(papers)):
    aa  = ut.getAuthorList(papers.iloc[j]['Authors'])
    idx = papers.iloc[j]['ID']
    for a in aa:
        authors.append(a.split('(')[0].split()[-1])
        IDs.append(idx)


# Find matches between registered users and authors
matches = {'Author': [], 'ID': []}
for sur in surnames:
    if sur in authors:
        k = authors.index(sur)
        matches['Author'].append(sur)
        matches['ID'].append(IDs[k])

print('Found {} authors'.format(len(matches['Author'])))


# Find all papers not yet registered
all_IDs = list(set(matches['ID']))
new_IDs = []
for l in all_IDs:
    if l in reg_ID:
        continue
    else:
        new_IDs.append(l)

new_IDs.sort()
new_IDs_df = pd.DataFrame(new_IDs)
new_IDs_df.columns = ['ID']
print('Found {} new papers'.format(len(new_IDs)))


# Save the file with recovered IDs
new_IDs_df.to_excel(file_new)
