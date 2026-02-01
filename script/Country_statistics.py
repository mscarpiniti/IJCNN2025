# -*- coding: utf-8 -*-
"""
This script is used to estimante the number of submission and/or accepted papers
for each country. The paper and user data are extracted from CMT.
The data are approximaetd since the country information in CMT is only related to
users, but it is a non-mandatory information.
The script seqauentially test all authors until a country information is present,
otherwise the information is skipped.

Created on Mon Apr 28 23:02:25 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import pandas as pd
import IJCNN_utils as ut
import matplotlib.pyplot as plt


# Set file names
path = './data/'
dest = './report/'
users_file = path + 'Users.txt'
paper_file = path + 'All_Accepted_Papers.xlsx'

country_file = dest + 'Country_accepted-papers.xlsx'
org_file = dest + 'Organization_Accepted.xlsx'


# Load data
df = ut.load_users(users_file)
df.set_index('Email', inplace=True)
papers = ut.load_submissions(paper_file)


# Extract country information
country = df['Country']
print('There are {} missing data'.format(country.isnull().sum()))

country.dropna(inplace=True)
print('There are {} valid data'.format(len(country)))

country_names = list(set(country))
print('Users come from {} different countries'.format(len(country_names)))

country_count = country.value_counts()
plt.figure()
country_count.plot(kind='bar')


# Count papers for each country
paper_country = {el:0 for el in country_names}

pap_per_count = ut.count_country(df, papers, country_names, sort='value')

print('Total number of papers with country information:', pap_per_count.sum())


# Save to excel the paper per country
pap_per_count.to_excel(country_file)


# Print the top three contries
print('\n')
for i in range(3):
    print(pap_per_count.index[i], ':', round(100*pap_per_count.iloc[i]/pap_per_count.sum(),2))



# %% Extract the main organization from each paper

organizations = []
for i in range(len(papers)):
    o = ut.getMainOrganization(papers.iloc[i]['Authors'])
    organizations.append(o)


# Create the DataFram with organization information
org_df = pd.DataFrame(organizations)
org_df.columns = ['Organization']

org_df.to_excel(org_file)
