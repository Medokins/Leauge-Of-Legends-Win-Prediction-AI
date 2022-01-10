from numpy.ma.core import default_fill_value
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/LeaugeOfLegends.csv")
df = df.drop('gameId', axis=1)

X = df.drop('blueWins', axis = 1).values
y = df['blueWins'].values

corrmat = df.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(40,40))

g=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")

plt.show()