# TalkingData

## Reference: 
- https://www.kaggle.com/pranav84/talkingdata-eda-to-model-evaluation-lb-0-9683
- https://www.kaggle.com/kailex/talkingdata-eda-and-class-imbalance
- https://www.kaggle.com/chubing/feature-engineering-and-xgboost
- https://www.kaggle.com/aharless/try-pranav-s-r-lgbm-in-python
- https://www.kaggle.com/graf10a/lightgbm-lb-0-9675
- https://www.kaggle.com/aharless/variation-on-alexander-kireev-s-dl   [Neural Network]
- https://www.kaggle.com/yuliagm/be-careful-about-ips-as-a-signal
- https://www.kaggle.com/pranav84/lightgbm-fixing-unbalanced-data-lb-0-9680  [Using var() and mean()]
- https://www.kaggle.com/yuliagm/talkingdata-eda-plus-time-patterns [Data Visualization]
- https://www.kaggle.com/andreikhropov/krishna-s-lgbm-to-catboost-undrsmpl-1-1/code (CatBoost)



## data_preparation
Here are some operations that I did to the training and test data:
- Delete rows with NA
- Drop attributed_time
- Extract day_of_week and hour as new features from click_time
- Drop click_time
- Create new features with groupby(ip, hour, os/app/day_of_weak/device).count(# channel)


train_is is the data from training data set with is_attributed == 1 , which may be useful for data visualization later

As for the GroupBys, they are the subdataset of the training/test data set with various grouping by, used for data visualization.

The Train.csv, Train_is.csv, Test.csv are shared with by Google Drive, they are in the previous shared file "WiDS", and I changed the name of that file to "Endless Project"

## Time_Series

## LightGBM
https://medium.com/@pushkarmandot/https-medium-com-pushkarmandot-what-is-lightgbm-how-to-implement-it-how-to-fine-tune-the-parameters-60347819b7fc

## XGBoost

## Semi_Supervised

## Neural Network



