# -*- coding: utf-8 -*-
"""
Spyder Editor
Created on Wed Mar 28 21:00:57 2018

@author: Chunni Zhao
"""
#%% Import
import pandas as pd

#%% Load data
train = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/train.csv')
train_sample = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/train_sample.csv')
test = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/test.csv')
#test_supplement = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/test_supplement.csv')

#########################################################
################# Taining data set ######################
#########################################################
#%% Drop attributed_time
train.drop('attributed_time', axis = 1, inplace = True)

# Check for NA
train.isnull().sum() # there is one column has NA
 #%%
# Extract day of week as a new feature from click_time
train['click_time'] = pd.to_datetime(train['click_time'])
train['day_of_week'] = train['click_time'].dt.dayofweek

# Extract hour as a new feature from click_time
train['hour'] = train.click_time.apply(lambda x: x.hour)

# Drop click_time
train.drop('click_time', axis = 1, inplace = True)

#%% Get the active observations (is_attributed == 1)
train_is = train[train["is_attributed"] == 1]
 
#%% Drop ip
train.drop('ip', axis = 1, inplace = True)



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
train_is.to_csv('Train_is.csv', index = None)
test.to_csv('Test.csv', index = None)



#%%
train_sample = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/train_sample.csv')
train_sample.drop('attributed_time', axis = 1, inplace = True)
train_sample['click_time'] = pd.to_datetime(train_sample['click_time'])
train_sample['day_of_week'] = train_sample['click_time'].dt.dayofweek
train_sample['hour'] = train_sample.click_time.apply(lambda x: x.hour)
train_sample.drop('click_time', axis = 1, inplace = True)
train_sample_is = train_sample[train_sample["is_attributed"] == 1]
#%%
nip_day_h = train_sample.groupby(['day_of_week', 'hour']).size().reset_index(name = 'nip_day_h')
nip_h_chan = train_sample.groupby(['hour', 'channel']).size().reset_index(name = 'nip_h_chan')
nip_h_os = train_sample.groupby(['hour', 'os']).size().reset_index(name = 'nip_h_os')
nip_h_app = train_sample.groupby(['hour', 'app']).size().reset_index(name = 'nip_h_app')
nip_h_dev = train_sample.groupby(['hour', 'device']).size().reset_index(name = 'nip_h_dev')
nnnn = train_sample.groupby(['day_of_week', 'hour', 'channel', 'os', 'app', 'device']).size().reset_index(name = 'nip')

#%%
ip_day_h = train_sample[['ip', 'day_of_week', 'hour', 'channel']].groupby(by = ['ip', 'day_of_week', 'hour'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_day_h'})
train_sample = train_sample.merge(ip_day_h, on = ['ip', 'day_of_week', 'hour'], how = 'left')

ip_h_os = train_sample[['ip', 'hour', 'os', 'channel']].groupby(by = ['ip', 'hour', 'os'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'ip_h_os'})
train_sample = train_sample.merge(ip_h_os, on = ['ip', 'hour', 'os'], how = 'left')

ip_h_app = train_sample[['ip', 'hour', 'app', 'channel']].groupby(by = ['ip', 'hour', 'app'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_h_app'})
train_sample = train_sample.merge(ip_h_app, on = ['ip', 'hour', 'app'], how = 'left')

ip_h_dev = train_sample[['ip', 'hour', 'device', 'channel']].groupby(by = ['ip', 'hour', 'device'])[['channel']].count().reset_index().rename(index = str, columns = {'channel': 'ip_h_dev'})
train_sample = train_sample.merge(ip_h_dev, on = ['ip', 'hour', 'device'], how = 'left')

#%%
ip_day_chan_var_h = train_sample[['ip', 'day_of_week', 'channel', 'hour']].groupby(by = ['ip', 'day_of_week', 'channel'])[['hour']].var().reset_index().rename(index = str, columns = {'hour': 'ip_day_chan_var_h'})
ip_day_chan_var_h.isnull().sum()
ip_day_chan_var_h = ip_day_chan_var_h.fillna(0)



#%%
temp = train_sample[['ip', 'day_of_week', 'channel', 'hour']]
temp.isnull().sum()
temp.groupby(by = ['ip', 'day_of_week', 'channel'])[['hour']].var()

#%%
#train_sample.drop('ip', axis = 1, inplace = True)

#%%
#train_sample.isnull().sum()
#
#
##%%
#train_sample.drop('attributed_time', axis = 1, inplace = True)
#
## Check for NA
#train_sample.isnull().sum() # there is one column has NA
# #%%
## Extract day of week as a new feature from click_time
#train_sample['click_time'] = pd.to_datetime(train_sample['click_time'])
#train_sample['day_of_week'] = train_sample['click_time'].dt.dayofweek
#
## Extract hour as a new feature from click_time
#train_sample['hour'] = train_sample.click_time.apply(lambda x: x.hour)
#
## Drop click_time
#train_sample.drop('click_time', axis = 1, inplace = True)


#%%
temp = train_sample.sample(n = 10, random_state = 2)


ip_app_os_sum_chan = train_sample[['ip', 'app', 'os', 'channel']].groupby(by = ['ip', 'app', 'os'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'ip_app_os_sum_chan'})
temp = train_sample[['ip', 'app', 'os', 'device', 'channel']].groupby(by = ['ip', 'app', 'os', 'device'])[['channel']].count().reset_index().rename(index = str, columns = {'channel' : 'sum_chan'})


#%% 
response = train_pp[['day_of_week', 'click_hour', 'is_attributed']].groupby(by = ['day_of_week', 'click_hour'], as_index = False)[['is_attributed']].count()
temp = train_pp[['day_of_week', 'click_hour', 'ip']].groupby(by = ['day_of_week', 'click_hour'], as_index = False)[['ip']].count()
app = train_pp[['day_of_week', 'click_hour', 'app']].groupby(by = ['day_of_week', 'click_hour'], as_index = False).count()

ip_h = train_pp[['ip', 'click_hour', 'is_attributed']].groupby(by = ['ip', 'click_hour'], as_index = False).count()
ip_h.dropna(axis = 0, how = 'any', inplace = True)



#%%
##### Create the data
counts = train_pp[['ip', 'is_attributed']].groupby(by = ['ip'], as_index = False).count()
counts.dropna(axis = 0, how = 'any', inplace = True)
counts.dtypes
proportion = train_pp[['ip', 'is_attributed']].groupby(by = ['ip'], as_index = False).mean()
proportion.dropna(axis = 0, how = 'any', inplace = True)
#proportion.dtypes
merge = counts.merge(proportion, on = ['ip'], how = 'left')
merge.columns = ['ip', 'click_count', 'prop_downloaded']
merge['x_axis'] = "ip " + merge['ip'].map(str) + " " + merge['click_hour'].map(str) + "h" ###################
merge = merge.sort_values(by = ['ip', 'click_hour'],  ascending = True)

x_axis = merge['x_axis']
y_left = merge[['click_count']]
y_right = merge[['prop_downloaded']]


#%%
###### Plot the data
fig = plt.figure(figsize=(25,14))
ax1 = fig.add_subplot(111)
# font style
font_label = {'family' : 'serif', 'weight' : 'normal','size' : 25,}
font_title = {'family' : 'serif', 'weight' : 'bold','color'  : 'dimgray', 'size' : 35,}
# plot left y axis
n = len(counts)
latent = [i for i in range(n)]
l1, = ax1.plot(latent, y_left, 'gold')
plt.xticks(arange(n), x_axis)
plt.xticks(fontsize = 17, rotation = 60)
plt.yticks(fontsize = 23)
ax1.set_ylabel('Count of Clicks', font_label)
# plot right y axis    
ax2 = ax1.twinx() 
l2, = ax2.plot(latent, y_right,'r', color = "dimgray")
plt.yticks(fontsize = 23)
ax2.set_ylabel('Proportion Downloaded', font_label)
# add title
#ax1.set_title("Conversion Rates over Counts of Click Time", font_title) ###################################
# add grid
plt.rc('grid', linestyle="--", color='gray')
plt.grid(True)
# add legend
plt.legend(handles = [l1, l2,], labels = ['Count of clicks', 'Proportion downloaded'], loc = 'best', fontsize = 20)

#plt.savefig("//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/d_h_train.jpg") ########################################
plt.show()














