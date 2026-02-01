# IJCNN 2025

Some useful scripts used to manage the entire review process of the [IJCNN 2025](https://2025.ijcnn.org/) conference, held in Rome from June 30 to July 5, 2025. Additional details in the conference review process and adopted strategies are available in \[1].

This repository contains 20 Python scripts and related Jupyter Notebooks implementing different steps of the Whole conference process, from importing Reviewers to making the final program in .docx format.

Specifically, all scripts and notebooks resort to the Python module IJCNN\_utils, which is a long file (about 1,500 lines) containing the definition of 40 function used in the scripts and notebooks.





## Content

The scripts and related notebooks are organized into 4 groups, detailed as follows.



### Pre-review phase

1. Split\_longFile \[\[script](script/Split\_longFile.py)]\[\[notebook](Notebooks/Split\_longFile.ipynb)]: used to split a long .xlsx file containing Reviewers or Meta-Reviewers into 10 smaller files, easier to be imported in CMT for invitation.

2\. Write\_XML \[script]\[notebook]: used for generating the XML file for automatically importing reviewers, meta-reviewers, and senior meta-reviewers in CMT.

3\. Check\_emailAddresses \[script]\[notebook]: used to check if any of the emai addresses associated with a user (Reviewer, Meta-Reviewer, etc.) is incorrect.

4\. Reviewers\_invitation \[script]\[notebook]: used to create CMT-compliant Tab Delimited text files used for inviting Reviewers in CMT.

5\. Primary\_Authors\_list \[script]\[notebook]: used to extract a list of all primary Authors of submitted papers at IJCNN 2025 (e.g., for using them as addition reviewers, in the proceedings, etc.).



### Utilities

6\. Move\_files \[script]\[notebook]: used to move files from a tree-based source folder to a specific single folder.

7\. Proposals\_list \[script]\[notebook]: used for manipulating the Special Session/Tutorial/Competition/Workshop proposals received to IJCNN 2025 conference. Specifically, it makes three tasks: i) it moves files from a tree-based source folder to a single folder and rename them according to the Paper ID; ii) it extract uself information from the CMT report exporting a simple xlsx file; and, iii) it generates a list in .docx format of all submitted proposals.

8\. Count\_pages \[script]\[notebook]: used to count the number of pages of PDF files ot check if these are compliant with the conference rules.



### Review phase

9\. ScoreIndex \[script]\[notebook]: to compute the Score Index (SI) used to set a threshold for the paper acceptance at IJCNN 2025. This experimental approach is based on that introduced by Cortes and Lawrence for NeurIPS 2014. More detail can be found in \[1].

10\. Reviewers\_rating \[script]\[notebook]: used to elaborate all Reviewer ratings provided by the Meta-Reviewers.





### After review phase

11\. AreaChairs\_list \[script]\[notebook]: used to make the list of all Area Chairs at IJCNN 2025 (e.g., for recognition in the the program).

12\. Authors\_list \[script]\[notebook]: used to make the list of all authors of acceptad papers at IJCNN 2025 (e.g., for using in the proceedings).

13\. Reviewers\_list \[script]\[notebook]: used to make the list of all Reviewers at IJCNN 2025 (e.g., for recognition in the the program).

14\. Count\_authors \[script]\[notebook]: Script used to count all the authors of accepted papers. Be aware that authors of multiple papers could be counted several times if names are written slightly differently.

15\. Country\_statistics \[script]\[notebook]: used to estimante the number of submission and/or accepted papers for each country.

16\. Find\_registeredID \[script]\[notebook]: used to retrieve IDs of papers whose authors have been registered but did not explicitly write their papers' ID.

17\. Registered\_Papers \[script]\[notebook]: used to generate a list of all registered papers at IJCNN 2025.

18\. Search\_Copyright\_ID \[script]\[notebook]: used to extract a list of all paper IDs which have a valid associated Copyright form in IEEE.

19\. Make\_Program \[script]\[notebook]: used to generate the conference program from the report of accepted papers containing the full information.

20\. Make\_VideoList \[script]\[notebook]:  used to generate a list of the video presentations in the conference program.





## Reference

1. Michele Scarpiniti and Danilo Comminiello, "The IJCNN 2025 Review Process," *arXiv*, DOI:
