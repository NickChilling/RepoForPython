import pandas as pd 
import numpy as np 
import random as rnd 

import seaborn as sns
import matplotlib.pyplot as plt 
%matplotlib inline 
#visualization

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

# 查看数据
train_df.columns.values # 列属性
train_df.head() , train_df.head()
train_df.info()

train_df.describe() # describe numerical feature
train_df.describe(include=['0'])

#数据清理
#对一些特征进行假设检验
# 根据以下特性删除
# 相关性
# 数据完整性
# 新增特征，年龄分类？缺失数据需要补充吗？ 

#验证相关性
train_df[['Pclass','Survived']].groupby(['Pclass'],as_index=False).mean().sort_values(by='Survived',ascend=False)
train_df[['Sex','Survived']].groupby(['Sex'],as_index=False).mean().sort_values(by="Survived",ascend=False)

g = sns.FacetGrid(train_df,col='Survived')
g.map(plt.hist,'Age',bins=20) # 绘制直方图(histogram) 
# 似乎是使用sns这一个方法，sns似乎是基于pandas，plt

train_df = train_df.drop(['Ticket','Cabin',axis=1])
# so does test_df
for dataset in combine:
    dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+\.')
# 提取title
pd.crosstab(train.df['Title'],train_df['Sex'])
for dataset in combine:
    dataset['Title'] = dataset['Title'].replace(['lady','countess'],'rare')
    #替换词

title_mapping = {'Mr':1,"miss":2,"Master":4}
for dataset in combine:
    dataset["Title"] = dataset["Title"].map(title_mapping) # map 


