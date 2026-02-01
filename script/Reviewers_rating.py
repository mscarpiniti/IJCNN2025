# -*- coding: utf-8 -*-
"""
Script used to elaborate all Reviewer ratings provided by the Meta-Reviewers.
It is used with the rating file downloaded from Microsoft CMT system.

Created on Mon Mar 31 21:56:35 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import pandas as pd
import IJCNN_utils as ut


# Set file names
path = './data/'
dest = './report/'
input_file = path + 'ReviewRatings.txt'
rev_file   = path + 'Reviewers_AllTracks.xlsx'
output_file = dest + 'RatingScore.xlsx'


# Loading the rating data
data = ut.load_reviewratings(input_file)
reviewers = ut.load_reviewers(rev_file)
reviewers.set_index('Email', inplace=True)


# Set the mapping between rating and score
Rc = {'Failed to Meet Expectations':0, 'Met Expectations':1, 'Exceeded Expectations':2}

# Mapping the rates to score
s = []
for i in range(data.shape[0]):
    s.append(Rc[data.iloc[i]['Rating']])

data.insert(2, 'Score', s)


# Compute score
rev = pd.Series(pd.unique(data.Reviewer))

data_sum  = data.groupby(by=['Reviewer'],as_index=False)['Score'].sum()
data_sum.set_index('Reviewer', inplace=True)
data_sum.rename(columns={'Score': 'Sum'}, inplace=True)
data_mean = data.groupby(by=['Reviewer'],as_index=False)['Score'].mean()
data_mean.set_index('Reviewer', inplace=True)
data_mean.rename(columns={'Score': 'Mean'}, inplace=True)
rev_count = data.groupby(by=['Reviewer'])['Reviewer'].count()
rev_count.name = 'Count'

data_score = data_mean.join(data_sum).join(rev_count)


# Save the rating file
data_score.to_excel(output_file)


# %% Sort for mean and count
data_score_sort = data_score.sort_values(by=['Mean', 'Count'], ascending=False)

# Print the best 10 Reviewers
revs = list(data_score_sort.index)
for i in range(10):
    print(reviewers.loc[revs[i]]['First Name'],
          reviewers.loc[revs[i]]['Last Name'], '\b:', revs[i],
          reviewers.loc[revs[i]]['Percent Completed'])


# Join also assignment information
reviewers_full = reviewers.join(data_score)
reviewers_full_sort = reviewers_full.sort_values(by=['Mean', 'Count', 'Percent Completed'], ascending=False)

# Print the best 10 Reviewers
for i in range(10):
    print(reviewers_full_sort.iloc[i]['First Name'],
          reviewers_full_sort.iloc[i]['Last Name'],
          '\b:', reviewers_full_sort.iloc[i].name,
          reviewers_full_sort.iloc[i]['Percent Completed'])
