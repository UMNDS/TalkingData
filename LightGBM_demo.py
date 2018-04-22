# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:37:12 2018

@author: Chunni Zhao
"""
############################################################################
# Regerence: https://www.kaggle.com/aharless/try-pranav-s-r-lgbm-in-python
############################################################################


#%% Import
import pandas as pd
import time
import numpy as np
from sklearn.model_selection import train_test_split
import lightgbm as lgb
import gc

#%% Read the data in
train = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Train.csv')
test = pd.read_csv('//Files.umn.edu/cse/UmSaveDocs/zhao1020/Desktop/TalkingData_data/Test.csv')

#%% Define function: lgb_modelfit_nocv
def lgb_modelfit_nocv(params, dtrain, dvalid, predictors, target = 'target', objective = 'binary', metrics = 
                      'auc', feval = None, early_stopping_rounds = 20, num_boost_round = 3000, verbose_eval = 10, categorical_features = None):
    lgb_params = {
            'boosting_type': 'gbdt',
            'objective': objective,
            'metric': metrics,
            'learning_rate': 0.01,
            'num_leaves': 31, # < 2^(max_depth)
            'max_depth': -1, # -1 means no limit
            'min_child_samples': 20, # Minimum number of data need in a child(min_data_in_leaf)
            'max_bin': 255, # Number of bucketed bin for feature values
            'subsample': 0.6, # Subsample ratio of the training instance.
            'subsample_freq': 0, # frequence of subsample, <=0 means no enable
            'colsample_bytree': 0.3, # Subsample ratio of columns when constructing each tree.
            'min_child_weight': 5, # Minimum sum of instance weight(hessian) needed in a child(leaf)
            'subsample_for_bin': 200000, # Number of samples for constructing bin
            'min_split_gain': 0, # lambda_l1, lambda_l2 and min_gain_to_split to regularization
            'reg_alpha': 0, # L1 regularization term on weights
            'reg_lambda': 0, # L2 regularization term on weights
            'nthread': 4,
            'verbose': 0,
            'metric': metrics}
    lgb_params.update(params)
    
    xgtrain = lgb.Dataset(dtrain[predictors].values, label = dtrain[target].values, feature_name = predictors, categorical_feature = categorical_features)
    xgvalid = lgb.Dataset(dvalid[predictors].values, label = dvalid[target].values, feature_name = predictors, categorical_feature = categorical_features)
    evals_results = {}
    
    bst1 = lgb.train(lgb_params,
                     xgtrain,
                     valid_sets = [xgtrain, xgvalid],
                     valid_names = ['train', 'valid'],
                     evals_result = evals_results,
                     num_boost_round = num_boost_round,
                     early_stopping_rounds = early_stopping_rounds,
                     varbose_eval = 10,
                     feval = feval)
    
    n_estimators = bst1.best_iteration
    return bst1

#%%


































