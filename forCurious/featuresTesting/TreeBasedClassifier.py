import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/LeaugeOfLegends.csv")
df = df.drop('gameId', axis=1)

X = df.drop('blueWins', axis = 1).values
y = df['blueWins'].values

model = ExtraTreesClassifier()
model.fit(X,y)

feat_importances = pd.Series(model.feature_importances_, index=df.columns[1:])
feat_importances.nlargest(20).plot(kind='barh')
plt.show()