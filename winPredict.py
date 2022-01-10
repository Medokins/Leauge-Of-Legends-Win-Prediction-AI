import pandas as pd
import sklearn
from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from getDataApi import getData

mainSummonerName = "Aaron II"
liveGame = True

df = pd.read_csv("datasets/LeaugeOfLegends.csv")
df = df.drop('gameId', axis=1)

df = df.drop('blueWardsPlaced', axis=1)
df = df.drop('blueWardsDestroyed', axis=1)
df = df.drop('blueFirstBlood', axis=1)
df = df.drop('blueEliteMonsters', axis=1)
df = df.drop('blueDragons', axis=1)
df = df.drop('blueHeralds', axis=1)
df = df.drop('blueTowersDestroyed', axis=1)
df = df.drop('blueTotalExperience', axis=1)
df = df.drop('blueTotalJungleMinionsKilled', axis=1)
df = df.drop('blueExperienceDiff', axis=1)
df = df.drop('blueAvgLevel', axis=1)

df = df.drop('redWardsPlaced', axis=1)
df = df.drop('redWardsDestroyed', axis=1)
df = df.drop('redFirstBlood', axis=1)
df = df.drop('redEliteMonsters', axis=1)
df = df.drop('redDragons', axis=1)
df = df.drop('redHeralds', axis=1)
df = df.drop('redTowersDestroyed', axis=1)
df = df.drop('redTotalExperience', axis=1)
df = df.drop('redTotalJungleMinionsKilled', axis=1)
df = df.drop('redKills', axis=1)
df = df.drop('redDeaths', axis=1)
df = df.drop('redExperienceDiff', axis=1)
df = df.drop('redGoldDiff', axis=1)
df = df.drop('redAvgLevel', axis=1)


df = sklearn.utils.shuffle(df)

X = df.drop('blueWins', axis = 1).values
X = preprocessing.scale(X)
y = df['blueWins'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 0)

clf = svm.SVC(kernel = 'linear')
clf.fit(X_train, y_train) 

#print(clf.score(X_test, y_test))
#neverSeenData = [blueKills, blueDeaths, blueAssists, blueTotalGold, blueTotalMinionsKilled, blueGoldDiff, blueCSPerMin, blueGoldPerMin, redAssists, redTotalGold, redTotalMinionsKilled,redCSPerMin, redGoldPerMin]
neverSeenData=[26, 19, 58, 11450, 100, -10050,10, 4145, 35, 21500, 60, 6, 3140]

if liveGame:
    gameData = getData(mainSummoner=mainSummonerName, verboose=True)
    print(gameData[0])
    if clf.predict([gameData[1:]]) == 1:
        print("blue team will most likely win")
    else:
        print("red team will most likely win")
else:
    if clf.predict([neverSeenData]) == 1:
        print("blue team will most likely win")
    else:
        print("red team will most likely win")
