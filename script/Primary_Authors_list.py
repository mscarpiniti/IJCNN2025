# -*- coding: utf-8 -*-
"""
Script used to extract a list of all primary Authors of submitted papers at
IJCNN 2025 (e.g., for using them as additional reviewers, in the proceedings, etc.).
It is used with the submission file downloaded from Microsoft CMT system.

Created on Fri Jan 31 17:37:53 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import pandas as pd
import IJCNN_utils as ut


# Set path and input file
path = './data/'
dest = './report/'
file = path + 'Papers.xlsx'
output_file_txt = dest + 'AllFirstAuthors.txt'


# Load papers
papers = ut.load_submissions(file)

N = papers.shape[0]


# Initialize empty lists
first_name = []
mid_name = []
last_name = []
email = []
organization = []


# Main loop
for i in range(N):
    x = papers.iloc[i]['Primary Contact']
    e = papers.iloc[i]['Primary Contact Email']
    a = papers.iloc[i]['Authors']
    n, m, s = ut.split_name(x)
    o = ut.get_organization(a)

    first_name.append(n)
    mid_name.append(m)
    last_name.append(s)
    email.append(e)
    organization.append(o)


# Create the DataFrame
columns_titles = ['First Name', 'Middle Initial', 'Last Name', 'Email', 'Organization']
df = pd.DataFrame(zip(first_name, mid_name, last_name, email, organization),
              columns=columns_titles)


# Write to the "Tab Delimited" text file
df.to_csv(output_file_txt, sep='\t', header=False, index=False)
