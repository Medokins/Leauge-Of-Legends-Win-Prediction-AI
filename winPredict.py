import pandas as pd
import sklearn
from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from getDataApi import getData

mainSummonerName = "Aaron II"
liveGame = False

df = pd.read_csv("datasets/LeaugeOfLegends.csv")
df = df.drop('gameId', axis=1)

#values of corelation of particular feature with "blueWins" based on Heatmap from featureTesting

df = df.drop('blueWardsPlaced', axis=1) #irrelevant
df = df.drop('blueWardsDestroyed', axis=1) #irrelevant
df = df.drop('blueFirstBlood', axis=1) #0.2 => I'll try to implement this
df = df.drop('blueEliteMonsters', axis=1) #0.22 => I'll try to implement this
df = df.drop('blueDragons', axis=1) #0.21 => I'll try to implement this
df = df.drop('blueHeralds', axis=1) #irrelevant
df = df.drop('blueTowersDestroyed', axis=1) # 0.12 need to test how much it inpacts data
df = df.drop('blueTotalExperience', axis=1) # 0.4 => MUST implement that
df = df.drop('blueTotalJungleMinionsKilled', axis=1) # 0.13 but It's impossible to implement with riot's API
df = df.drop('blueExperienceDiff', axis=1) # 0.49 MUST implement that
df = df.drop('blueAvgLevel', axis=1) # 0.36 MUST implement that

df = df.drop('redWardsPlaced', axis=1) #irrelevant
df = df.drop('redWardsDestroyed', axis=1) #irrelevant
df = df.drop('redFirstBlood', axis=1) # opposite of blueFirstBlood, need to do some testing with that
df = df.drop('redEliteMonsters', axis=1) # opposite of blueEliteMonsters 
df = df.drop('redDragons', axis=1) #opposite of blueDragons
df = df.drop('redHeralds', axis=1) #opposite of blueHeralds => irrelevant
df = df.drop('redTowersDestroyed', axis=1) # -0.1 => can try to implement that but not that important
df = df.drop('redTotalExperience', axis=1) # -0.39 => MUST implement that
df = df.drop('redTotalJungleMinionsKilled', axis=1) # -0.11 but same as in blue team, impossible to do with riot's API
df = df.drop('redKills', axis=1) #-0.34 opposite of blueDeaths => will do some testing
df = df.drop('redDeaths', axis=1) #0.34 MUST implement that (although it's opposite of blueKills)
df = df.drop('redExperienceDiff', axis=1) #-0.49 oppoiste of blueExperienceDiff
df = df.drop('redGoldDiff', axis=1) # -0.51 opposite of blueGoldDiff
df = df.drop('redAvgLevel', axis=1) # -0.35 MUST implement that


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
