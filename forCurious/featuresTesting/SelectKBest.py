import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

df = pd.read_csv("../datasets/LeaugeOfLegends.csv")

X = df.drop('blueWins', axis = 1).values
X.clip(0,1)
y = df['blueWins'].values

bestfeatures = SelectKBest(score_func=chi2, k=15)
fit = bestfeatures.fit(X,y) #but this doesnt work since my data contains opposing values like blueKills = redDeaths, so redDeaths will have negative impact on blueWins