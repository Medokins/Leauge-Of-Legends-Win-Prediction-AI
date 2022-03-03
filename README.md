# Leauge-Win-Prediction-AI

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This a ML algorithm to predict which team will most likely win based on 10min of in-game data

## Technologies
* Riot's API for acquiring data
* sklearn for model selection
* seaborn + matplotlib for data visualisation
* pickle for model loading
* [Kaggle Leauge Of Legends dataset](https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min)

## Setup
To run this project, paste Your API key [here](https://github.com/Medokins/Leauge-Of-Legends-Win-Prediction-AI/blob/main/apiKey.txt).
* To get Your API key go [here](https://developer.riotgames.com/)
And Your in-game nick [here](https://github.com/Medokins/Leauge-Of-Legends-Win-Prediction-AI/blob/main/winPredict.py) and [here](https://github.com/Medokins/Leauge-Of-Legends-Win-Prediction-AI/blob/main/getDataApi.py)

## Note
This was trained and tested in Diamond elo, the lower Your division is the less accurate this model will be.