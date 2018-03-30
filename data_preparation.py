# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:00:57 2018

@author: Chunni Zhao
"""
#%% Import
import pandas as pd

#%% Load data
train = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/train.csv')
test = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/test.csv')
test_supplement = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/test_supplement.csv')


#########################################################
################# Taining data set ######################
#########################################################
#%% Drop attributed_time
train.drop('attributed_time', axis = 1, inplace = True)

# Check for NA
train.isnull().sum() 
train.dropna(axis = 0, how = 'any')

# Extract day of week as a new feature from click_time
train['click_time'] = pd.to_datetime(train['click_time'])
train['day_of_week'] = train['click_time'].dt.dayofweek

# Extract hour as a new feature from click_time
train['hour'] = train.click_time.apply(lambda x: x.hour)

# Drop click_time
train.drop('click_time', axis = 1, inplace = True)


#%% Get the active observations (is_attributed == 1)
train_is = train[train["is_attributed"] == 1]




#########################################################
################# Testing data set ######################
#########################################################
#%% Join "test" and "test_supplement" together to get a larger test data set
test = test.append(test_supplement)

#%% Subset columns that match training data
test['click_time'] = pd.to_datetime(test['click_time'])
test['day_of_week'] = test['click_time'].dt.dayofweek
test['hour'] = test.click_time.apply(lambda x: x.hour)
test.drop('click_time', axis = 1, inplace = True)


#########################################################
############ Write output into csv files ################
#########################################################
#%%
train.to_csv('Train.csv', index = None)
train_is.to_csv('Train.csv', index = None)
test.to_csv('Test.csv', index = None)


