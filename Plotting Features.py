#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:54:48 2018

@author: echozhao
"""
#%%
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *


#%% Read data
train_pp = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/train_pp.csv')
train_rs = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/train_rs.csv')

train_rs.dtypes
train_pp.dtypes
train_pp['is_attributed'] = train_pp['is_attributed'].astype('int64')
train_pp['ip'] = train_pp['ip'].astype('int64')


#%% Number of unique values




#%% Explain IP
ip_6 = train_pp[['ip', 'app', 'device', 'os', 'channel']]
ip_6 = ip_6[ip_6['ip'] == 6]
ip_6.to_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/ip_app.csv', index = None)



#%% Conversion Rates over Counts of Click Time (nip_wday_hour)
##### Create the data
counts = train[['day_of_week', 'click_hour', 'is_attributed']].groupby(by = ['day_of_week', 'click_hour'], as_index = False).count() ###################
counts.dtypes
proportion = train[['day_of_week', 'click_hour', 'is_attributed']].groupby(by = ['day_of_week', 'click_hour'], as_index = False).mean() ###############
proportion.dtypes
merge = counts.merge(proportion, on = ['day_of_week', 'click_hour'], how = 'left')
merge.columns = ['day_of_week', 'click_hour', 'click_count', 'prop_downloaded']
merge['x_axis'] = merge['day_of_week'].map(str) + "d" + merge['click_hour'].map(str) + "h" ###################
merge = merge.sort_values(by = ['day_of_week', 'click_hour'],  ascending = True)

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
ax1.set_title("Conversion Rates over Counts of Click Time", font_title) ###################################
# add grid
plt.rc('grid', linestyle="--", color='gray')
plt.grid(True)
# add legend
plt.legend(handles = [l1, l2,], labels = ['Count of clicks', 'Proportion downloaded'], loc = 'best', fontsize = 20)

plt.savefig("//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/d_h_train.jpg") ########################################
plt.show()



















