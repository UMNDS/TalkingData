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


#%% Create new features by 
ip_day_h = train[['ip', 'day_of_week', 'hour', 'channel']].groupby(by = ['ip', 'day_of_week', 'hour'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_day_h'})
train = train.merge(ip_day_h, on = ['ip', 'day_of_week', 'hour'], how = 'left')

ip_h_os = train[['ip', 'hour', 'os', 'channel']].groupby(by = ['ip', 'hour', 'os'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'ip_h_os'})
train = train.merge(ip_h_os, on = ['ip', 'hour', 'os'], how = 'left')

ip_h_app = train[['ip', 'hour', 'app', 'channel']].groupby(by = ['ip', 'hour', 'app'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_h_app'})
train = train.merge(ip_h_app, on = ['ip', 'hour', 'app'], how = 'left')

ip_h_dev = train[['ip', 'hour', 'device', 'channel']].groupby(by = ['ip', 'hour', 'device'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_h_dev'})
train = train.merge(ip_h_dev, on = ['ip', 'hour', 'device'], how = 'left')


#%% Write the subdataset out
ip_day_h.to_csv('ip_day_h_trn.csv', index = None)
ip_h_os.to_csv('ip_h_os_trn.csv', index = None)
ip_h_app.to_csv('ip_h_app_trn.csv', index = None)
ip_h_dev.to_csv('ip_h_dev_trn.csv', index = None)



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

#%% Group bys
ip_day_h = test[['ip', 'day_of_week', 'hour', 'channel']].groupby(by = ['ip', 'day_of_week', 'hour'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_day_h'})
test = test.merge(ip_day_h, on = ['ip', 'day_of_week', 'hour'], how = 'left')

ip_h_os = test[['ip', 'hour', 'os', 'channel']].groupby(by = ['ip', 'hour', 'os'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'ip_h_os'})
test = test.merge(ip_h_os, on = ['ip', 'hour', 'os'], how = 'left')

ip_h_app = test[['ip', 'hour', 'app', 'channel']].groupby(by = ['ip', 'hour', 'app'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_h_app'})
test = test.merge(ip_h_app, on = ['ip', 'hour', 'app'], how = 'left')

ip_h_dev = test[['ip', 'hour', 'device', 'channel']].groupby(by = ['ip', 'hour', 'device'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_h_dev'})
test = test.merge(ip_h_dev, on = ['ip', 'hour', 'device'], how = 'left')

#%% Write the subdataset out
ip_day_h.to_csv('ip_day_h_tst.csv', index = None)
ip_h_os.to_csv('ip_h_os_tst.csv', index = None)
ip_h_app.to_csv('ip_h_app_tst.csv', index = None)
ip_h_dev.to_csv('ip_h_dev_tst.csv', index = None)



#########################################################
############ Write output into csv files ################
#########################################################
#%% Get the active observations (is_attributed == 1)
train_is = train[train["is_attributed"] == 1]

#%%
train.to_csv('Train.csv', index = None)
train_is.to_csv('Train_is.csv', index = None)
test.to_csv('Test.csv', index = None)




