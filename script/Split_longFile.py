# -*- coding: utf-8 -*-
"""
This script is used to split a long file containing Reviewers or Meta-Reviewers
into 10 smaller files. In this way, it is easier to upload users in CMT.

Created on Mon Jul 28 15:22:10 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import pandas as pd


# Load the long file
path = './data/'
dest = './report/'

input_file = path + 'Reviewers.xlsx'
df = pd.read_excel(input_file)
# input_file = path + 'Reviewers.txt'
#df = pd.read_csv(input_file, sep='\t', header=None)

N = int(len(df)/10)  # Length of each file


# Selecting sub-parts
df1 = df.iloc[:N]
df2 = df.iloc[N:2*N]
df3 = df.iloc[2*N:3*N]
df4 = df.iloc[3*N:4*N]
df5 = df.iloc[4*N:5*N]
df6 = df.iloc[5*N:6*N]
df7 = df.iloc[6*N:7*N]
df8 = df.iloc[7*N:8*N]
df9 = df.iloc[8*N:9*N]
df10 = df.iloc[9*N:]


# Saving separate files
df1.to_csv(dest + 'Reviewers1.txt', sep='\t', header=False, index=False)
df2.to_csv(dest + 'Reviewers2.txt', sep='\t', header=False, index=False)
df3.to_csv(dest + 'Reviewers3.txt', sep='\t', header=False, index=False)
df4.to_csv(dest + 'Reviewers4.txt', sep='\t', header=False, index=False)
df5.to_csv(dest + 'Reviewers5.txt', sep='\t', header=False, index=False)
df6.to_csv(dest + 'Reviewers6.txt', sep='\t', header=False, index=False)
df7.to_csv(dest + 'Reviewers7.txt', sep='\t', header=False, index=False)
df8.to_csv(dest + 'Reviewers8.txt', sep='\t', header=False, index=False)
df9.to_csv(dest + 'Reviewers9.txt', sep='\t', header=False, index=False)
df10.to_csv(dest + 'Reviewers10.txt', sep='\t', header=False, index=False)
