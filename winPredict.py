import pandas as pd
import sklearn
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from getDataApi import getData

mainSummonerName = "Aaron II"
liveGame = False

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

neverSeenData = [0,6,6,6,0,0,0,0,16400,7.0,210,-1004,21.0,1640.0,1,6,6,7,1,1,0,0,17404,7.0,225,1004,22.5,1740.4]

random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, y_train)

if liveGame:
    gameData = getData(mainSummoner=mainSummonerName, verboose=True)
    print(gameData[0])
    if random_forest.predict([gameData[1:]]) == 1:
        print("blue team will most likely win")
    else:
        print("red team will most likely win")
else:
    if random_forest.predict([neverSeenData]) == 1:
        print("blue team will most likely win")
    else:
        print("red team will most likely win")
