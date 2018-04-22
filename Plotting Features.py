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
import numpy as np
import math


#%% Read data
train_pp = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/train_pp.csv')
train_rs = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/train_rs.csv')

train_rs.dtypes
train_pp.dtypes
train_pp['is_attributed'] = train_pp['is_attributed'].astype('int64')
train_pp['ip'] = train_pp['ip'].astype('int64')




#%%
################################################################################################
################################# Number of Unique Values ######################################
################################################################################################
#%% 
plt.figure(figsize=(20, 15))
plt.rcParams['axes.facecolor'] = 'gainsboro'
sns.set(font = "serif")

cols = ['ip', 'app', 'device', 'os', 'channel'] # bars
uniques = [len(train[col].unique()) for col in cols]
log_uniq = [math.log(len(train[col].unique())) for col in cols] # height
y_pos = np.arange(len(cols))

plt.bar(y_pos, log_uniq, color = ['mistyrose', 'navajowhite', 'azure', 'honeydew', 'khaki'])
#plt.rc('font', family = 'serif', size = 25) # font style
font_label = {'family' : 'serif', 'weight' : 'normal','size' : 22,}
# x axis
plt.xticks(y_pos, cols, fontsize = 22)
plt.xlabel('Features', font_label)
# y axis
plt.yticks(fontsize = 22)
plt.ylabel('Log(number of unique values)', font_label)
# add title
font_title = {'family' : 'serif', 'weight' : 'bold', 'size' : 28,}
plt.title('Number of Unique Values for Each Feature', font_title)
# set grid
plt.grid(color = 'black', linestyle = '--', linewidth = 1, axis = 'y')
# set tag
x = np.arange(5)
for a,b in zip(x, uniques):
    plt.text(a, math.log(b)+0.01, '%.0f' %b, ha = 'center', va = 'bottom', fontsize = 22)

plt.savefig("//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/count_uniq.jpg") 
plt.show()






################################################################################################
##################################### Explain IP ###############################################
################################################################################################
#%% 
ip_6 = train_pp[['ip', 'app', 'device', 'os', 'channel']]
ip_6 = ip_6[ip_6['ip'] == 6]
ip_6.to_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/ip_app.csv', index = None)




#%%
################################################################################################
############################## Correlation Between Features ####################################
################################################################################################
#%% 
import seaborn as sns
trn = train[['ip', 'app', 'device', 'os', 'channel', 'click_time', 'is_attributed']]
corr = trn.corr()

sns.set(style = 'white')
# font style
font_title = {'family' : 'serif', 'weight' : 'bold', 'size' : 28,}
font_label = {'family' : 'serif', 'weight' : 'normal','size' : 22,}
sns.set(font = "serif", font_scale = 2)

f, ax = plt.subplots(figsize = (18,18))
cmap = sns.color_palette("Pastel1")
sns.heatmap(corr, cmap = cmap, vmax = .3, center = 0, square = True, linewidths = .5, cbar_kws = {"shrink": .82}, annot = True, annot_kws = {'size': 18, 'family': 'serif'})
# x axis
plt.xticks(fontsize = 22)
plt.xlabel('Features', font_label)
# y axis
plt.yticks(fontsize = 22)
plt.ylabel('Features', font_label)
# add title
plt.title('Feature Correlation', font_title)

plt.savefig("//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/feature_corr.jpg")
plt.show()




#%%
################################################################################################
#################################### Conversion Rates ##########################################
################################################################################################
#%% Conversion Rates over Counts of Click Time (nip_wday_hour)
##### Create the data
counts = train_o[['day_of_week', 'click_hour', 'is_attributed']].groupby(by = [ 'day_of_week', 'click_hour'], as_index = False).count() 
counts.dtypes
proportion = train_o[['day_of_week', 'click_hour', 'is_attributed']].groupby(by = ['day_of_week', 'click_hour'], as_index = False).mean() 
proportion.dtypes
merge = counts.merge(proportion, on = ['day_of_week', 'click_hour'], how = 'left')
merge.columns = ['day_of_week', 'click_hour', 'click_count', 'prop_downloaded']
merge['x_axis'] = merge['day_of_week'].map(str) + "d" + merge['click_hour'].map(str) + "h" 
merge = merge.sort_values(by = ['day_of_week', 'click_hour'],  ascending = True)

x_axis = merge['x_axis']
y_left = merge[['click_count']]
y_right = merge[['prop_downloaded']]

###### Plot the data
fig = plt.figure(figsize=(25,14))
ax1 = fig.add_subplot(111)
# font style
font_label = {'family' : 'serif', 'weight' : 'normal','size' : 25,}
font_title = {'family' : 'serif', 'weight' : 'bold','color'  : 'dimgray', 'size' : 35,}
#sns.set(font = "serif")
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
ax1.set_title("Conversion Rates over Counts of Click Time", font_title) 
# add grid
plt.rc('grid', linestyle="--", color='gray')
plt.grid(True)
# add legend
plt.legend(handles = [l1, l2,], labels = ['Count of clicks', 'Proportion downloaded'], loc = 'best', fontsize = 20)

#plt.savefig("//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/d_h_train.jpg") ########################################
plt.show()



#%%
################################################################################################
########################## Conversion Rates on Attributed Time #################################
################################################################################################
#%%
train = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/train.csv')
train_1 = train[train['is_attributed'] == 1]
#
def ppAttributedTime(df):
    df['attributed_time'] = pd.to_datetime(df['attributed_time'])
    df['day_of_week'] = df['attributed_time'].dt.dayofweek
    df['click_hour'] = df['attributed_time'].dt.hour
    return df

train_1_pp = ppAttributedTime(train_1)

#%%
counts = train_1_pp[['day_of_week', 'click_hour', 'is_attributed']].groupby(by = ['day_of_week', 'click_hour'], as_index = False).count() 
counts.columns = ['day_of_week', 'click_hour', 'click_count']
counts['x_axis'] = counts['day_of_week'].map(str) + "d" + counts['click_hour'].map(str) + "h" 
counts = counts.sort_values(by = ['day_of_week', 'click_hour'],  ascending = True)

x = counts['x_axis']
y = counts[['click_count']]
#%%
fig = plt.figure(figsize=(25,14))
ax1 = fig.add_subplot(111)
# font style
font_label = {'family' : 'serif', 'weight' : 'normal','size' : 25,}
font_title = {'family' : 'serif', 'weight' : 'bold','color'  : 'dimgray', 'size' : 35,}
sns.set(font = "serif")
# plot left y axis
n = len(counts)
latent = [i for i in range(n)]
ax1.plot(latent, y, 'gold')
plt.xticks(arange(n), x)
plt.xticks(fontsize = 17, rotation = 60)
plt.yticks(fontsize = 23)
ax1.set_ylabel('Count of Clicks', font_label)
# add title
ax1.set_title("Count of Clicks on attributed time", font_title) 
# add grid
plt.rc('grid', linestyle="--", color='gray')
plt.grid(True)
# add legend
plt.legend( labels = ['Count of clicks'], loc = 'best', fontsize = 20)

#plt.savefig("//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Undersampling/d_h_train.jpg") ########################################
plt.show()












