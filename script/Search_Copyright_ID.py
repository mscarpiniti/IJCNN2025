# -*- coding: utf-8 -*-
"""
Script used to extract a list of all paper IDs which have a valid associated
Copyright form in IEEE.
It is used with the Copyright file downloaded from IEEE system.

Created on Mon May 26 22:15:32 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import pandas as pd


# Set path and input file
path = './data/'
dest = './report/'
file = path + 'Copyright.xlsx'
output_file_txt = dest + 'Copyright_ID.txt'


# Load Copyright file
df = pd.read_excel(file)


# The IEEE identifier has the form: IJCNN2025-PaperID
identifiers = list(df['ARTICLE IDENTIFIER'])


# Main loop over the data
cpf_idx = []
for i in range(len(identifiers)):
    s = identifiers[i]
    cpf_idx.append(s.split('-')[-1])


# Converting retrieved data to DataFrame and save the file
cfp_df = pd.DataFrame(cpf_idx)
cfp_df.columns = ['ID']

cfp_df.to_excel(output_file_txt)
