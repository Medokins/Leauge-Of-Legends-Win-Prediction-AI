import requests
import json
from items import items

f = open("C:/Users/medok/OneDrive/Desktop/Python/Leauge of legends/apiKey.txt", "r") #put the path to yout apiKey
apiKey = f.read()
mainSummoner = "Aaron II" #put your nick here

def getData(mainSummoner, verboose):

    time = 10 #time on which the AI is trained (in minutes)

    #blueTeam:
    #must: blueTotalExperience, blueExperienceDiff, blueAvgLevel

    #redTeam:
    #must: redAvgLevel
    #test: redExperienceDiff, redGoldDiff

    encryptedSummonerID = json.loads(requests.get(f"https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{mainSummoner}?api_key={apiKey}").text)["id"]
    gameDataDict  = json.loads(requests.get(f"https://eun1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{encryptedSummonerID}?api_key={apiKey}").text)
    eventDataDict = json.loads(requests.get("https://127.0.0.1:2999/liveclientdata/eventdata", verify=False).text)

    summonerNames = {"redTeam": [], "blueTeam": []}
    encryptedSummonersID = {"redTeam": [], "blueTeam": []}


    for i in range(len(gameDataDict) - 1):
        if gameDataDict["participants"][i]["teamId"] == 200:
            summonerNames["redTeam"].append(gameDataDict["participants"][i]["summonerName"])
            encryptedSummonersID["redTeam"].append(gameDataDict["participants"][i]["summonerId"])
        elif gameDataDict["participants"][i]["teamId"] == 100:
            summonerNames["blueTeam"].append(gameDataDict["participants"][i]["summonerName"])
            encryptedSummonersID["blueTeam"].append(gameDataDict["participants"][i]["summonerId"])
        else:
            print("He is a spectator")

    blueFirstBlood = 0
    blueTowersDestroyed = 0
    blueDragons = 0
    blueHeralds = 0
    blueEliteMonsters = 0
    blueKills = 0
    blueDeaths = 0
    blueAssists = 0
    blueTotalGold = 0
    blueTotalMinionsKilled = 0
    blueGoldDiff = 0
    blueCSPerMin = 0
    blueGoldPerMin = 0

    redFirstBlood = 0
    redTowersDestroyed = 0
    redDragons = 0
    redEliteMonsters = 0
    redHeralds = 0
    redKills = 0
    redDeaths = 0
    redAssists = 0
    redTotalGold = 0
    redTotalMinionsKilled = 0
    redCSPerMin = 0
    redGoldPerMin = 0


    for event in eventDataDict:
        if event["EventName"] == "FirstBrick":
            if event["KillerName"] in summonerNames["blueTeam"]:
                blueFirstBlood = 1            
        if event["EventName"] == "TurretKilled":
            if event["KillerName"] in summonerNames["blueTeam"]:
                blueTowersDestroyed += 1
            else:
                redTowersDestroyed += 1
        if event["EventName"] == "DragonKill":
            if event["KillerName"] in summonerNames["blueTeam"]:
                blueDragons += 1
            else:
                redDragons += 1
        if event["EventName"] == "HeraldKill":
            if event["KillerName"] in summonerNames["blueTeam"]:
                blueHeralds += 1
            else:
                redHeralds += 1

    blueEliteMonsters = blueDragons + blueHeralds
    redEliteMonsters = redDragons + redHeralds

    #Blue team:
    for _ in range(len(summonerNames["blueTeam"])):

        summoner = summonerNames["blueTeam"][_]
        summonerScore = json.loads(requests.get(f"https://127.0.0.1:2999/liveclientdata/playerscores?summonerName={summoner}", verify=False).text)
        blueKills += summonerScore["kills"]
        blueDeaths += summonerScore["deaths"]
        blueAssists += summonerScore["assists"]
        summonerItems = json.loads(requests.get(f"https://127.0.0.1:2999/liveclientdata/playeritems?summonerName={summoner}", verify=False).text)

        totalSummonerGold = 0
        for i in range(len(summonerItems)):
            itemPrice = items[summonerItems[i]["displayName"]]
            totalSummonerGold += itemPrice

        blueTotalGold += totalSummonerGold

        blueTotalMinionsKilled += summonerScore["creepScore"]

    blueCSPerMin = blueTotalMinionsKilled / time
    blueGoldPerMin = blueTotalGold / time


    #Red team:
    for _ in range(len(summonerNames["redTeam"])):

        summoner = summonerNames["redTeam"][_]
        summonerScore = json.loads(requests.get(f"https://127.0.0.1:2999/liveclientdata/playerscores?summonerName={summoner}", verify=False).text)
        redKills += summonerScore["kills"]
        redDeaths += summonerScore["deaths"]
        redAssists += summonerScore["assists"]
        summonerItems = json.loads(requests.get(f"https://127.0.0.1:2999/liveclientdata/playeritems?summonerName={summoner}", verify=False).text)

        totalSummonerGold = 0
        for i in range(len(summonerItems)):
            itemPrice = items[summonerItems[i]["displayName"]]
            totalSummonerGold += itemPrice
        redTotalGold += totalSummonerGold

        redTotalMinionsKilled += summonerScore["creepScore"]

    redCSPerMin = redTotalMinionsKilled / time
    redGoldPerMin = redTotalGold / time
    blueGoldDiff = blueTotalGold - redTotalGold

    if verboose:
        print(f"Blue Kills {blueKills}\
                \nblueDeaths {blueDeaths}\
                \nblueAssits {blueAssists}\
                \nblueTotalGold {blueTotalGold}\
                \nblueTotalMinionsKilled {blueTotalMinionsKilled}\
                \nblueGoldDiff {blueGoldDiff}\
                \nblueCSPerMin {blueCSPerMin}\
                \nblueGoldPerMin {blueGoldPerMin}\
                \nredAssists {redAssists}\
                \nredTotalGold {redTotalGold}\
                \nredTotalMinionsKilled {redTotalMinionsKilled}\
                \nredCSPerMin {redCSPerMin}\
                \nredGoldPerMin {redGoldPerMin}")

    return [summonerNames, blueKills, blueDeaths, 
            blueAssists, blueTotalGold, blueTotalMinionsKilled,
            blueGoldDiff, blueCSPerMin, blueGoldPerMin, redAssists,
            redTotalGold, redTotalMinionsKilled, redCSPerMin, redGoldPerMin]
