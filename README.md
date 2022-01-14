# Leauge-Win-Prediction-AI

This is an alpha version of the AI, some thing might still need some tweaking.

Model was trained based on [this](https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min) dataset. I'm leaving the training file (modelTraining.py), modelSelection.py and featureTesting directory if You're curious how it works and what led me to choosing this classifier/those features.

However, all You need to do to use this in Your games is paste the API key in apiKey.txt file, put path to it in the getDataApi file, and write Your in-game nick in winPredict and GetDataApi file.

Note that this was trained and tested in Diamond elo, the lower You are the less accurate this model will be.