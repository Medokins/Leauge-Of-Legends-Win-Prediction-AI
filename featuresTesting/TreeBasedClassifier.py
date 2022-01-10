import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/LeaugeOfLegends.csv")
df = df.drop('gameId', axis=1)

X = df.drop('blueWins', axis = 1).values
y = df['blueWins'].values
