# -*- coding: utf-8 -*-
"""
Script used for generating the XML file for automatically importing reviewers,
meta-reviewers, and senior meta-reviewers in CMT.

This script generates a template similar to:
<assignments>
  <submission submissionId="ID1">
    <user email="USER1 EMAIL" />
    <user email="USER2 EMAIL" />
    <user email="USER3 EMAIL" />
  </submission>
  <submission submissionId="ID2">
    <user email="USER1 EMAIL" />
    <user email="USER2 EMAIL" />
    <user email="USER3 EMAIL" />
  </submission>
  <submission submissionId="ID3">
    <user email="USER1 EMAIL" />
    <user email="USER2 EMAIL" />
    <user email="USER3 EMAIL" />
  </submission>
</assignments>

The submission file should at least contain a column with the paper ID.

Created on Wed Apr  2 22:42:22 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""


import pandas as pd


# Set file names
path = './data/'
dest = './report/'
submission_file = path + "Paper_Selection.xlsx" # should contain at least the paper ID
out_file = dest + "SMR_assignment.xml"


# Set the Senior Meta-Reviewers
USER1_EMAIL = 'my_email1@aa.it'
USER2_EMAIL = 'my_email2@bb.it'
USER3_EMAIL = 'my_email3@qq.it'
# Repeat as needed

USER_EMAILS = [USER1_EMAIL, USER2_EMAIL, USER3_EMAIL]


# Read paper
papers = pd.read_excel(submission_file)

N_R = len(USER_EMAILS)
N_P = len(papers)


# Write the XML file
with open(out_file, "w") as file:
    file.write('<assignments>\n')
    for i in range(N_P):
        file.write('  <submission submissionId="%s">\n' % str(papers.iloc[i]['ID']))
        for j in range(N_R):
            file.write('    <user email="%s" />\n' % USER_EMAILS[j])
        file.write('  </submission>\n')
    file.write('</assignments>')
