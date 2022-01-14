import pandas as pd
import sklearn
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("datasets/LeaugeOfLegends.csv")
df = df.drop('gameId', axis=1)

df = df.drop('blueWardsPlaced', axis=1)
df = df.drop('blueWardsDestroyed', axis=1)
df = df.drop('blueTotalExperience', axis=1)
df = df.drop('blueTotalJungleMinionsKilled', axis=1)
df = df.drop('blueExperienceDiff', axis=1)

df = df.drop('redWardsPlaced', axis=1)
df = df.drop('redWardsDestroyed', axis=1)
df = df.drop('redTotalExperience', axis=1)
df = df.drop('redTotalJungleMinionsKilled', axis=1)
df = df.drop('redExperienceDiff', axis=1)

df = sklearn.utils.shuffle(df)

X = df.drop('blueWins', axis = 1).values
X = preprocessing.scale(X)
y = df['blueWins'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 0)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

pickle.dump(logreg, open('model.pkl', 'wb'))