# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 15:06:05 2018

@author: zhao1020
"""
#%%
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

from sklearn.model_selection import train_test_split 
from sklearn.utils import resample

#%% Load in data
train = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/train.csv')
train_sample = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/train_sample.csv')
test = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/test.csv')

#%% Random Undersampling
# Separate the 2 classes
train_0 = train[train['is_attributed'] == 0]
train_1 = train[train['is_attributed'] == 1]

# Undersample class 0 (without replacement)
train0_undersampled = resample(train_0, replace=False, n_samples=len(train_1), random_state=142)

# Combine minority class with downsampled majority class
train_us = pd.concat([train0_undersampled, train_1])

#%% Feature Engineering
# Set categorical variables
cat = ['ip', 'app', 'device', 'os', 'channel']
for c in cat:
    train_us[c] = train_us[c].astype('category')
    test[c]=test[c].astype('category')

# Only training data has is_attributed
train_us['is_attributed'] = train_us['is_attributed'].astype('category')

# Extract features from click_time
def ppClicktime(df):
    df['click_time'] = pd.to_datetime(df['click_time'])
    df['day_of_week'] = df['click_time'].dt.dayofweek
    df['week'] = df['click_time'].dt.week
    df['click_hour'] = df['click_time'].dt.hour
    df['click_minute'] = df['click_time'].dt.minute
    return df

train_pp = ppClicktime(train_us)

# Drop click_time
train_pp.drop('click_time', axis = 1, inplace = True)


#%% Random Sampling
train_rs = train.sample(n = 10000000, replace = False)
train_rs = ppClicktime(train_rs)
train_rs.drop('click_time', axis = 1, inplace = True)

#%% Original training data
train_o = ppClicktime(train)
train_o.drop('click_time', axis = 1, inplace = True)


#%% Write out data
train_pp.to_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/train_pp.csv', index = None)
train_rs.to_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/train_rs.csv', index = None)
