# Leauge-Win-Prediction-AI

This is an alpha version of the AI, some things might still need some tweaking.

Model was trained based on [this](https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min) dataset (it is also available in forCurious directory). I'm leaving the training file (modelTraining.py), modelSelection.py and featureTesting directory in "forCurious" directory if You're curious how it works and what led me to choosing this classifier/those features.

However, all You need to do to use this in Your games is paste the API key in apiKey.txt file,and write Your in-game nick in winPredict and GetDataApi file.

Note that this was trained and tested in Diamond elo, the lower Your division is the less accurate this model will be.