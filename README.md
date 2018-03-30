# TalkingData

## Reference: 
- https://www.kaggle.com/pranav84/talkingdata-eda-to-model-evaluation-lb-0-9683
- https://www.kaggle.com/kailex/talkingdata-eda-and-class-imbalance
- https://www.kaggle.com/chubing/feature-engineering-and-xgboost
- https://www.kaggle.com/aharless/try-pranav-s-r-lgbm-in-python


## data_preparation
Here are some operations that I did to the training and test data:
- Delete rows with NA
- Drop attributed_time
- Extract day_of_week and hour as new features from click_time
- Drop click_time

I did not delete the variable ip becasue I think it may be helpful while doing visualization (sum(ip))

train_is is the data from training data set with is_attributed == 1 , which may be useful for data visualization later

As for the GroupBys, they are the subdataset of the training/test data set with various grouping by

The Train.csv, Train_is.csv, Test.csv are shared with by Google Drive, they are in the previous shared file "WiDS", and I changed the name of that file to "Endless Project"
