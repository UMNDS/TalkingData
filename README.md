# TalkingData


## data_preparation
- Reference: 
https://www.kaggle.com/pranav84/talkingdata-eda-to-model-evaluation-lb-0-9683
https://www.kaggle.com/kailex/talkingdata-eda-and-class-imbalance


Here are some operations that I did to the training and test data:
- Delete rows with NA
- Drop attributed_time
- Extract day_of_week and hour as new features from click_time
- Drop click_time

I did not delete the variable ip becasue I think it may be helpful while doing visualization (sum(ip))

train_is is the data from training data set with is_attributed == 1 , which may be useful for data visualization later
