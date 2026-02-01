# -*- coding: utf-8 -*-
"""
This script is used to move files from a tree-based source folder to a specific
single folder.
It is used for moving files downloaded from Microsoft CMT system to a unique folder.

Created on Wed Oct 23 19:29:07 2024

@author: Michele Scarpiniti -- DIET Dpt. (Sapienza University of Rome)
"""

import os
import shutil


# Set file names
path_src = './data/Submissions/'
path_dst = './data/Papers/'


# Choose file type
sub_type = '/Submission/'
# sub_type = '/CameraReady/'
# sub_type = '/Copyright/'

copy = 0  # 0: move files,  1: copy files


# Scan the current folder
folders  = os.listdir(path_src)
N_papers = len(folders)


# Loop for moving files
for i in range(len(folders)):
    p1 = path_src + folders[i] + sub_type
    # p2 = path_dst #+ folders[i] + '/'
    name_src = os.listdir(p1)[0]
    ext = '.' + name_src.split('.')[-1]
    name_dst = 'Paper_' + folders[i] + ext
    if copy:
        shutil.copy2(p1+name_src, path_dst+name_dst)
    else:
        shutil.move(p1+name_src, path_dst+name_dst)
        # shutil.move(p1+name_src, p2+name_dst)
        os.rmdir(p1)


print("End of moving {} files".format(N_papers))
