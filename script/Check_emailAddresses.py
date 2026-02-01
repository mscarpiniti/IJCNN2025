# -*- coding: utf-8 -*-
"""
This script is used to check if any of the emai addresses associated with a
user (Reviewer, Meta-Reviewer, etc.) is incorrect.

This to avoid to be spanned by email providers.

Created on Mon Jul 28 15:24:44 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import pandas as pd
import IJCNN_utils as ut



# Load a user file
path = './data/'

input_file = path + 'Reviewers.xlsx'
df = pd.read_excel(input_file)
# input_file = path + 'Reviewers.txt'
# df = pd.read_csv(input_file, sep='\t', header=None)


# Check for email validity
em = list(df['Email'])
_, res = ut.test_emails(em)

# Print the incorrect email addresses
if len(res) > 0:
    print("Please, check the following email addresses:")
    for n, j in enumerate(res):
        print(n+1, ':', em[j])
else:
    print("All email addresses are correct")
