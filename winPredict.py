from getDataApi import getData
import pickle

mainSummonerName = "Aaron II"
liveGame = False

neverSeenData = [0,6,7,6,0,0,0,0,16400,7.0,210,-1004,21.0,1640.0,1,7,6,7,1,1,0,0,17404,7.0,225,1004,22.5,1740.4]

model = pickle.load(open('model.pkl', 'rb'))

if liveGame:
    gameData = getData(mainSummoner=mainSummonerName, verboose=True)
    print(gameData[0])
    if model.predict([gameData[1:]]) == 1:
        print("blue team will most likely win")
    else:
        print("red team will most likely win")
else:
    if model.predict([neverSeenData]) == 1:
        print("blue team will most likely win")
    else:
        print("red team will most likely win")
