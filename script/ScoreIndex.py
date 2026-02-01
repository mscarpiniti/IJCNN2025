# -*- coding: utf-8 -*-
"""
A script to compute the Score Index (SI) used to set a threshold for the paper
acceptance at IJCNN 2025.

This experimental approach is based on that introduced by Cortes and Lawrence for
NeurIPS 2014. More detail can be found here:
- https://inverseprobability.com/2014/08/02/reviewer-calibration-for-nips
- https://github.com/lawrennd/neurips2014
- https://github.com/lawrennd/neurips2014/blob/master/notebooks/Reviewer%20Calibration.ipynb

The script does the following tasks. It:
    - dequantizes and calibrates the reviewers and meta-reviewers
    - merges reviewers' and meta-reviewers's scores
    - finds and exports automatically the papers over threshold, given an
      acceptance rate (in percentage) set by the user;
    - exports a tab delimited txt file with all paper status (Accept or Reject)
      for next uploading in CMT
    - finds and exports best papers for award.


Created on Tue Mar 11 22:22:01 2025

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""


import pandas as pd
import IJCNN_utils as ut


# Setting the path names
path = './data/'
dest = './report/'
track = 'main/'
# track = 'workshop/'
in_path  = path + track
out_path = dest + track


# Setting the file names
input_file_r  = in_path + 'Reviews.xlsx'
input_file_mr = in_path + 'MetaReviews.xlsx'
papers_file = in_path + 'Papers.xlsx'

output_file = out_path + 'Reviews_calibrated.xlsx'
output_file_ord = out_path + 'Reviews_calibrated_ordered.xlsx'
output_file_SI  = out_path + 'Reviews_calibrated_SI.xlsx'
status_file_txt = out_path + 'Status.txt'
prize_file = out_path + 'Prize.xlsx'


# Acceptance rate on SI in percentage (%)
ACTH = 40


# Set the mapping between item and score
Rc = {1:0.8, 2:0.9, 3:1.0, 4:1.1, 5:1.2}
MR = {3:1, 2:0.9, 1:0.75, 0:0.6, -1:0.5, -2:0.4, -3:0.3}


print('Loading the Reviews.....')

# Reading the Reviews from the input file
data_r = ut.load_reviews(input_file_r)


# Evaluating the index Sr for each Reviewer
print('Computing score for each Reviewer.....')

w = []
for i in range(data_r.shape[0]):
    w.append(Rc[data_r.iloc[i]['Rc']])
    data_r.loc[i,'Sr'] = data_r.iloc[i]['R'] + (data_r.iloc[i]['C1'] + data_r.iloc[i]['C2'] + data_r.iloc[i]['C3'] + data_r.iloc[i]['C4'])/2 + data_r.iloc[i]['AQ']

data_r.insert(4, 'Weights', w)

# Number of acceptanced papers
paper2accept = int(len(set(data_r['ID']))*ACTH/100)
# paper2accept = 2210


# Dequantize the review scores for each Reviewer
print('De-quantizing scores of each Reviewer.....')
data_r = ut.dequantize(data_r, 100)


# Calibrate the review scores for each Reviewer
print('Calibrating scores of each Reviewer.....')
data_r, revs = ut.calibration(data_r, column='Sr_dq', number_accepts=paper2accept)

data_r.to_excel(output_file)
revs.to_excel(output_file_ord)


# Evaluate the Score Index (SI)
ids = pd.Series(pd.unique(data_r.ID))
titles = pd.Series(pd.unique(data_r.Title))

# Computing the global Score Index (SI) for each paper
data_Sr_mean = data_r.groupby(by=['ID'],as_index=False)['Sr'].mean()
data_Sr_wemean = data_r.groupby(by=['ID'],as_index=False).apply(ut.weighted_avg, 'Sr', 'Weights')
data_Sr_wemean.rename(columns={None: 'Sr'}, inplace=True)

data_AQ_sum = data_r.groupby(by=['ID'],as_index=False)['AQ'].sum()
data_AQ_mean = data_r.groupby(by=['ID'],as_index=False)['AQ'].mean()

data_SrdqCal_mean = data_r.groupby(by=['ID'],as_index=False)['Sr_dq_Calibrated'].mean()
data_SrdqCal_wemean = data_r.groupby(by=['ID'],as_index=False).apply(ut.weighted_avg, 'Sr_dq_Calibrated', 'Weights')
data_SrdqCal_wemean.rename(columns={None: 'Sr_dq_Calibrated'}, inplace=True)

data_Sr_dq_AcceptProbability = data_r.groupby(by=['ID'],as_index=False)['Sr_dq_AcceptProbability'].mean()

Sr_mean_100 = 100 * ut.normalize(data_Sr_mean['Sr'])
Sr_wemean_100 = 100 * ut.normalize(data_Sr_wemean['Sr'])
SrdqCal_mean_100 = 100 * ut.normalize(data_SrdqCal_mean['Sr_dq_Calibrated'])
SrdqCal_wemean_100 = 100 * ut.normalize(data_SrdqCal_wemean['Sr_dq_Calibrated'])

frame = {'ID':ids, 'Title':titles, 'AQ_mean':data_AQ_mean['AQ'], 'AQ_sum':data_AQ_sum['AQ'],
         'Sr_mean':data_Sr_mean['Sr'],
         'Sr_mean_100':Sr_mean_100, 'Sr_weighted_mean_100':Sr_wemean_100,
         'SrdqCal_mean_100':SrdqCal_mean_100, 'SrdqCal_weighted_mean_100':SrdqCal_wemean_100,
         'Sr_dq_AcceptProbability':data_Sr_dq_AcceptProbability['Sr_dq_AcceptProbability']}

data_SI = pd.DataFrame(frame)



# Get the paper authors and status
authorStatus = ut.get_authors_status(papers_file)

# Joint the authors and status to the score sheet
data_SI = data_SI.join(authorStatus.set_index('ID'), on='ID')

column1 = data_SI.pop('Authors')
column2 = data_SI.pop('Status')
data_SI.insert(2, 'Authors', column1)
data_SI.insert(3, 'Status', column2)


# Extract and clibrate Meta-Riewers

# Reading the Reviews from the input file
print('Loading the Meta-Reviews.....')
data_mr = ut.load_metareviews(input_file_mr)


# Add a quality column
Q = []
for i in range(data_mr.shape[0]):
    Q.append(MR[data_mr.iloc[i]['R']])

data_mr.insert(4, 'Q', Q)


# Calibrate the review scores for each Reviewer
print('\nCalibrating scores of each Meta-Reviewer.....')
data_mr, mrevs = ut.calibration(data_mr, column='R', number_accepts=paper2accept, who='Meta-Reviewer')


# Evaluate the Score of Meta-Reviews
dataMR_Sr_mean = data_mr.groupby(by=['ID'],as_index=False)['R'].mean()
dataMR_SrCal_mean = data_mr.groupby(by=['ID'],as_index=False)['R_Calibrated'].mean()
weights = data_mr.groupby(by=['ID'],as_index=False)['Q'].mean()

dataMR_Sr_mean_100 = dataMR_Sr_mean.copy()
dataMR_SrCal_mean_100 = dataMR_SrCal_mean.copy()
dataMR_Sr_mean_100['R'] = 100 * ut.normalize(dataMR_Sr_mean_100['R'])
dataMR_Sr_mean_100.rename(columns={'R': 'R_100'}, inplace=True)
dataMR_SrCal_mean_100['R_Calibrated'] = 100 * ut.normalize(dataMR_SrCal_mean_100['R_Calibrated'])
dataMR_SrCal_mean_100.rename(columns={'R_Calibrated': 'R_Calibrated_100'}, inplace=True)


# Join the evaluated metrics
data_SI = data_SI.join(weights.set_index('ID'), on='ID')
data_SI = data_SI.join(dataMR_Sr_mean.set_index('ID'), on='ID').join(dataMR_SrCal_mean.set_index('ID'), on='ID')
data_SI = data_SI.join(dataMR_Sr_mean_100.set_index('ID'), on='ID').join(dataMR_SrCal_mean_100.set_index('ID'), on='ID')


# Remove the missing data in the meta-reviews
data_SI['Q'] = data_SI['Q'].fillna(value=1)
data_SI['R'] = data_SI['R'].fillna(data_SI['Sr_mean'])


# Fuse reviews and meta-reviews

# Use harmonic_avg or power_avg
merged_score = ut.harmonic_avg(data_SI, 'Sr_weighted_mean_100', 'R_100')
merged_score.name = 'Merged_score'
merged_score_cal = ut.harmonic_avg(data_SI, 'SrdqCal_weighted_mean_100', 'R_Calibrated_100')
merged_score_cal.name = 'Merged_score_calibrated'
merged_score_cal_q = data_SI['SrdqCal_weighted_mean_100']*data_SI['Q']
merged_score_cal_q.name = 'Merged_score_calibrated_Q'

data_SI = data_SI.join(merged_score)#.join(merged_score_q)
data_SI = data_SI.join(merged_score_cal).join(merged_score_cal_q)


# Save the final spreadsheet
data_SI.to_excel(output_file_SI)


# Order and save ranking
df1 = data_SI.sort_values(by='SrdqCal_weighted_mean_100', ascending=False)
df2 = data_SI.sort_values(by='Merged_score', ascending=False)
df3 = data_SI.sort_values(by='Merged_score_calibrated', ascending=False)
df4 = data_SI.sort_values(by='Merged_score_calibrated_Q', ascending=False)
df5 = data_SI.sort_values(by='Sr_dq_AcceptProbability', ascending=False)

df1.to_excel(out_path + 'ScoreIndex_ordered_SrdqCal.xlsx')
df2.to_excel(out_path + 'ScoreIndex_ordered_Merged.xlsx')
df3.to_excel(out_path + 'ScoreIndex_ordered_MergedCal.xlsx')
df4.to_excel(out_path + 'ScoreIndex_ordered_MergedCal_Q.xlsx')
df5.to_excel(out_path + 'ScoreIndex_ordered_SrProbCal.xlsx')


# Provide some basic statistics
print('Some statistics on submitted papers')

print('\nSr_mean:')
print(data_SI['Sr_mean'].describe())

print('\nSr_dqCal_mean:')
print(data_SI['SrdqCal_weighted_mean_100'].describe())



# Filter the Score Index (SI) for accepted papers
papers = data_SI[['ID','Sr_weighted_mean_100']]

TH = data_SI['Sr_weighted_mean_100'].quantile(q=(1-ACTH/100))
accepted = data_SI[['ID', 'Sr_weighted_mean_100']].where(data_SI['Sr_weighted_mean_100']>=TH)
accepted.dropna(inplace=True)
N_acc = len(accepted)
print('\nNumer of accepted papers:', N_acc)
print('Statistics on accepted papers:')
print(accepted['Sr_weighted_mean_100'].describe())


# Bar plot of the Score Index (SI)
ax = data_SI.plot.bar(y='Sr_weighted_mean_100')
ax.axhline(y=TH, color='r')


# Filter the Score Index (SI) for rejected papers
rejected = data_SI[['ID','Sr_weighted_mean_100']].mask(data_SI['Sr_weighted_mean_100']>TH)
rejected.dropna(inplace=True)


# Set and export paper status to a txt file for CMT
status_A = pd.DataFrame(columns=['ID','Status'])
status_A['ID'] = accepted.index
status_A['Status'] = 'Accept'
status_R = pd.DataFrame(columns=['ID','Status'])
status_R['ID'] = rejected.index
status_R['Status'] = 'Reject'
status = pd.concat([status_A, status_R])
status.sort_values('ID', inplace=True)

status.to_csv(status_file_txt, sep='\t', header=False, index=False)


# Save all figures
ut.save_all_figs(out_path + 'Figures.pdf')


# Best paper award
P_th = 2  # Minimum number of Award nominations

prize = data_SI[['ID', 'AQ_mean', 'AQ_sum','Sr_weighted_mean_100']].where(data_SI['AQ_sum']>=P_th)
prize.dropna(inplace=True)
Titles = []
for j in list(prize.index):
    Titles.append(data_SI['Title'].where(data_SI.index==j).dropna().iloc[0])

prize['Title'] = Titles
prize.sort_values(['Sr_weighted_mean_100','AQ_sum'], ascending=False, inplace=True)

# prize.to_excel(prize_file)
prize.to_excel(prize_file, index=False)
