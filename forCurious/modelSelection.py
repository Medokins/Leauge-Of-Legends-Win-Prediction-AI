import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm

test = False

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

if test:
    df = df.drop("blueTotalMinionsKilled", axis=1)
    df = df.drop("blueCSPerMin", axis=1)
    df = df.drop("blueGoldPerMin", axis=1)
    df = df.drop("redFirstBlood", axis=1)
    df = df.drop("redKills", axis=1)
    df = df.drop("redDeaths", axis=1)
    df = df.drop("redAssists", axis=1)
    df = df.drop("redEliteMonsters", axis=1)
    df = df.drop("redTotalMinionsKilled", axis=1)
    df = df.drop("redCSPerMin", axis=1)
    df = df.drop("blueEliteMonsters", axis=1)
    df = df.drop("blueDragons", axis=1)
    df = df.drop("blueHeralds", axis=1)
    df = df.drop("blueTowersDestroyed", axis=1)
    df = df.drop("redDragons", axis=1)
    df = df.drop("redHeralds", axis=1)
    df = df.drop("redTowersDestroyed", axis=1)
    df = df.drop("redGoldDiff", axis=1)
    df = df.drop("redGoldPerMin", axis=1)



X = df.drop('blueWins', axis = 1).values
X = preprocessing.scale(X)
y = df['blueWins'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 0)

sgd = linear_model.SGDClassifier(max_iter=5, tol=None)
sgd.fit(X_train, y_train)
sgd.score(X_train, y_train)
acc_sgd = round(sgd.score(X_train, y_train) * 100, 2)

random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, y_train)
random_forest.score(X_train, y_train)
acc_random_forest = round(random_forest.score(X_train, y_train) * 100, 2)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
acc_log = round(logreg.score(X_train, y_train) * 100, 2)

knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, y_train)
acc_knn = round(knn.score(X_train, y_train) * 100, 2)

gaussian = GaussianNB() 
gaussian.fit(X_train, y_train)
acc_gaussian = round(gaussian.score(X_train, y_train) * 100, 2)

decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, y_train)
acc_decision_tree = round(decision_tree.score(X_train, y_train) * 100, 2)

scv_model = svm.SVC(kernel = 'linear')
scv_model.fit(X_train, y_train) 
acc_svm = round(scv_model.score(X_train, y_train) * 100, 2)

results = pd.DataFrame({
    'Model': ['KNN', 'Logistic Regression', 
              'Random Forest', 'Naive Bayes',
              'Stochastic Gradient Decent', 
              'Decision Tree', 'Svm'],
    'Score': [acc_knn, acc_log, 
              acc_random_forest, acc_gaussian, 
              acc_sgd, acc_decision_tree, acc_svm]})
result_df = results.sort_values(by='Score', ascending=False)
result_df = result_df.set_index('Score')
print(result_df.head(7))

models = [knn, logreg, random_forest, gaussian,sgd, decision_tree, scv_model]
names = ['KNN', 'Logistic Regression', 'Random Forest', 'Naive Bayes', 'Stochastic Gradient Decent', 'Decision Tree', 'Svm']
i = 0
print("\n")

for model in models:
    scores = cross_val_score(model, X_test, y_test, cv=10, scoring = "accuracy")
    print(names[i])
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard Deviation:", scores.std())
    print("\n")
    i += 1