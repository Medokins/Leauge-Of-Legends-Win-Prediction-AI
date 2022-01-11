import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

df = pd.read_csv("../datasets/LeaugeOfLegends.csv")

X = df.drop('blueWins', axis = 1).values
y = df['blueWins'].values

bestfeatures = SelectKBest(score_func=chi2, k=10)
#in progress