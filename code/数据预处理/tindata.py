# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 12:20:07 2018

@author: Administrator
"""

import pandas as pd

#划分数据集，便于测试
cache_path = 'tindata/'
train_path = 'data/train.csv'
test_path = 'data/test.csv'
result1_path = cache_path + 'train.csv' 
result2_path = cache_path + 'test.csv' 


if __name__ == "__main__":
    
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    train1 = train[train['userid']<55555]
    test2 = test[(test['userid']<55555)]
    train1.to_csv(result1_path)
    test2.to_csv(result2_path)