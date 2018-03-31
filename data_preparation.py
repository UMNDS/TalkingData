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



#####################################################################################
################################# Taining data set ##################################
#####################################################################################
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


#%% Create new features with count(channel) 
ip_sum_chan = train[['ip', 'channel']].groupby(by = ['ip'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'ip_sum_chan'})
train = train.merge(ip_sum_chan, on = ['ip'], how = 'left')

ip_app_sum_chan = train[['ip', 'app', 'channel']].groupby(by = ['ip', 'app'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'ip_app_sum_chan'})
train = train.merge(ip_app_sum_chan, on = ['ip', 'app'], how = 'left')

ip_app_os_sum_chan = train[['ip', 'app', 'os', 'channel']].groupby(by = ['ip', 'app', 'os'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'ip_app_os_sum_chan'})
train = train.merge(ip_app_os_sum_chan, on = ['ip', 'app', 'os'], how = 'left')

ip_day_h_sum_chan = train[['ip', 'day_of_week', 'hour', 'channel']].groupby(by = ['ip', 'day_of_week', 'hour'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_day_h_sum_chan'})
train = train.merge(ip_day_h_sum_chan, on = ['ip', 'day_of_week', 'hour'], how = 'left')

ip_h_os_sum_chan = train[['ip', 'hour', 'os', 'channel']].groupby(by = ['ip', 'hour', 'os'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'ip_h_os_sum_chan'})
train = train.merge(ip_h_os_sum_chan, on = ['ip', 'hour', 'os'], how = 'left')

ip_h_app_sum_chan = train[['ip', 'hour', 'app', 'channel']].groupby(by = ['ip', 'hour', 'app'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_h_app_sum_chan'})
train = train.merge(ip_h_app_sum_chan, on = ['ip', 'hour', 'app'], how = 'left')

ip_h_dev_sum_chan = train[['ip', 'hour', 'device', 'channel']].groupby(by = ['ip', 'hour', 'device'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_h_dev_sum_chan'})
train = train.merge(ip_h_dev_sum_chan, on = ['ip', 'hour', 'device'], how = 'left')


#%% Create new features with var()
ip_day_chan_var_h = train[['ip', 'day_of_week', 'hour', 'channel']].groupby(by = ['ip', 'day_of_week', 'channel'])[['hour']].var().reset_index().rename(index = str, columns = {'hour': 'ip_day_chan_var_h'})
ip_day_chan_var_h = ip_day_chan_var_h.fillna(0)
train = train.merge(ip_day_chan_var_h, on = ['ip', 'day_of_week', 'channel'], how = 'left')

ip_app_os_var_h = train[['ip', 'app', 'os', 'hour']].groupby(by = ['ip', 'app', 'os'])[['hour']].var().reset_index().rename(index = str, columns = {'hour' : 'ip_app_os_var_h'})
ip_app_os_var_h = ip_app_os_var_h .fillna(0)
train = train.merge(ip_app_os_var_h, on = ['ip', 'app', 'os'], how = 'left')

ip_app_chan_var_day = train[['ip', 'day_of_week', 'app', 'channel']].groupby(by = ['ip', 'channel', 'app'])[['day_of_week']].var().reset_index().rename(index = str, columns = {'day_of_week': 'ip_app_chan_var_day'})
ip_app_chan_var_day = ip_app_chan_var_day.fillna(0)
train = train.merge(ip_app_chan_var_day, on = ['ip', 'channel', 'app'], how = 'left')


#%% Create new features with mean()
ip_app_chan_mean_h = train[['ip', 'hour', 'app', 'channel']].groupby(by = ['ip', 'channel', 'app'])[['hour']].mean().reset_index().rename(index = str, columns = {'hour': 'ip_app_chan_mean_h'})
ip_app_chan_mean_h = ip_app_chan_mean_h.fillna(0)
train = train.merge(ip_app_chan_mean_h, on = ['ip', 'channel', 'app'], how = 'left')


#%% Write the subdataset out
ip_sum_chan.to_csv('ip_sum_chan_trn.csv', index = None)
ip_app_sum_chan.to_csv('ip_app_sum_chan_trn.csv', index = None)
ip_app_os_sum_chan.to_csv('ip_app_os_sum_chan_trn.csv', index = None)
ip_day_h_sum_chan.to_csv('ip_day_h_sum_chan_trn.csv', index = None)
ip_h_os_sum_chan.to_csv('ip_h_os_sum_chan_trn.csv', index = None)
ip_h_app_sum_chan.to_csv('ip_h_app_sum_chan_trn.csv', index = None)
ip_h_dev_sum_chan.to_csv('ip_h_dev_sum_chan_trn.csv', index = None)
ip_day_chan_var_h.to_csv('ip_day_chan_var_h_trn.csv', index = None)
ip_app_os_var_h.to_csv('ip_app_os_var_h_trn.csv', index = None)
ip_app_chan_var_day.to_csv('ip_app_chan_var_day_trn.csv', index = None)
ip_app_chan_mean_h.to_csv('ip_app_chan_mean_h_trn.csv', index = None)



#####################################################################################
############################### Testing data set ####################################
#####################################################################################
#%% Join "test" and "test_supplement" together to get a larger test data set
test = test.append(test_supplement)

#%% Subset columns that match training data
test['click_time'] = pd.to_datetime(test['click_time'])
test['day_of_week'] = test['click_time'].dt.dayofweek
test['hour'] = test.click_time.apply(lambda x: x.hour)
test.drop('click_time', axis = 1, inplace = True)

#%% Create new features with count(channel) 
ip_sum_chan = test[['ip', 'channel']].groupby(by = ['ip'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'ip_sum_chan'})
train = test.merge(ip_sum_chan, on = ['ip'], how = 'left')

ip_app_sum_chan = test[['ip', 'app', 'channel']].groupby(by = ['ip', 'app'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'ip_app_sum_chan'})
train = test.merge(ip_app_sum_chan, on = ['ip', 'app'], how = 'left')

ip_app_os_sum_chan = test[['ip', 'app', 'os', 'channel']].groupby(by = ['ip', 'app', 'os'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'ip_app_os_sum_chan'})
train = test.merge(ip_app_os_sum_chan, on = ['ip', 'app', 'os'], how = 'left')

ip_day_h_sum_chan = test[['ip', 'day_of_week', 'hour', 'channel']].groupby(by = ['ip', 'day_of_week', 'hour'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_day_h_sum_chan'})
train = test.merge(ip_day_h_sum_chan, on = ['ip', 'day_of_week', 'hour'], how = 'left')

ip_h_os_sum_chan = test[['ip', 'hour', 'os', 'channel']].groupby(by = ['ip', 'hour', 'os'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'ip_h_os_sum_chan'})
train = test.merge(ip_h_os_sum_chan, on = ['ip', 'hour', 'os'], how = 'left')

ip_h_app_sum_chan = test[['ip', 'hour', 'app', 'channel']].groupby(by = ['ip', 'hour', 'app'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_h_app_sum_chan'})
train = test.merge(ip_h_app_sum_chan, on = ['ip', 'hour', 'app'], how = 'left')

ip_h_dev_sum_chan = test[['ip', 'hour', 'device', 'channel']].groupby(by = ['ip', 'hour', 'device'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_h_dev_sum_chan'})
train = test.merge(ip_h_dev_sum_chan, on = ['ip', 'hour', 'device'], how = 'left')


#%% Create new features with var()
ip_day_chan_var_h = test[['ip', 'day_of_week', 'hour', 'channel']].groupby(by = ['ip', 'day_of_week', 'channel'])[['hour']].var().reset_index().rename(index = str, columns = {'hour': 'ip_day_chan_var_h'})
ip_day_chan_var_h = ip_day_chan_var_h.fillna(0)
train = test.merge(ip_day_chan_var_h, on = ['ip', 'day_of_week', 'channel'], how = 'left')

ip_app_os_var_h = test[['ip', 'app', 'os', 'hour']].groupby(by = ['ip', 'app', 'os'])[['hour']].var().reset_index().rename(index = str, columns = {'hour' : 'ip_app_os_var_h'})
ip_app_os_var_h = ip_app_os_var_h .fillna(0)
train = test.merge(ip_app_os_var_h, on = ['ip', 'app', 'os'], how = 'left')

ip_app_chan_var_day = test[['ip', 'day_of_week', 'app', 'channel']].groupby(by = ['ip', 'channel', 'app'])[['day_of_week']].var().reset_index().rename(index = str, columns = {'day_of_week': 'ip_app_chan_var_day'})
ip_app_chan_var_day = ip_app_chan_var_day.fillna(0)
train = test.merge(ip_app_chan_var_day, on = ['ip', 'channel', 'app'], how = 'left')


#%% Create new features with mean()
ip_app_chan_mean_h = test[['ip', 'hour', 'app', 'channel']].groupby(by = ['ip', 'channel', 'app'])[['hour']].mean().reset_index().rename(index = str, columns = {'hour': 'ip_app_chan_mean_h'})
ip_app_chan_mean_h = ip_app_chan_mean_h.fillna(0)
train = test.merge(ip_app_chan_mean_h, on = ['ip', 'channel', 'app'], how = 'left')


#%% Write the subdataset out
ip_sum_chan.to_csv('ip_sum_chan_tst.csv', index = None)
ip_app_sum_chan.to_csv('ip_app_sum_chan_tst.csv', index = None)
ip_app_os_sum_chan.to_csv('ip_app_os_sum_chan_tst.csv', index = None)
ip_day_h_sum_chan.to_csv('ip_day_h_sum_chan_tst.csv', index = None)
ip_h_os_sum_chan.to_csv('ip_h_os_sum_chan_tst.csv', index = None)
ip_h_app_sum_chan.to_csv('ip_h_app_sum_chan_tst.csv', index = None)
ip_h_dev_sum_chan.to_csv('ip_h_dev_sum_chan_tst.csv', index = None)
ip_day_chan_var_h.to_csv('ip_day_chan_var_h_tst.csv', index = None)
ip_app_os_var_h.to_csv('ip_app_os_var_h_tst.csv', index = None)
ip_app_chan_var_day.to_csv('ip_app_chan_var_day_tst.csv', index = None)
ip_app_chan_mean_h.to_csv('ip_app_chan_mean_h_tst.csv', index = None)



#####################################################################################
############################ Write output into csv files ############################
#####################################################################################
#%% Get the active observations (is_attributed == 1)
train_is = train[train["is_attributed"] == 1]

#%%
train.to_csv('Train.csv', index = None)
train_is.to_csv('Train_is.csv', index = None)
test.to_csv('Test.csv', index = None)




