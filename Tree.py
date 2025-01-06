import pandas as pd
# import io # useless bo bez colaba robimy lub nie ale to się dogada
# from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
# import pydotplus
# from IPython.display import Image

print("Diamond rank league of legends statistics at minute 10.")
#narazie tylko dla blue side robię bo nwm co robię
lolDataFrame = pd.read_csv('data.csv',  delimiter=',', decimal='.')
lolFeaturesDataFrame = pd.DataFrame(lolDataFrame, columns=['blueFirstBlood', 'blueKills', 'blueDeaths', 'blueAssists', 'blueEliteMonsters', 'blueDragons', 'blueHeralds', 'blueTowersDestroyed', 'blueGoldDiff', 'blueExperienceDiff'])
lolWinDataFrame = pd.DataFrame(lolDataFrame, columns=['blueWins'])

lolFeaturesNames = ['blueFirstBlood', 'blueKills', 'blueDeaths', 'blueAssists', 'blueEliteMonsters', 'blueDragons', 'blueHeralds', 'blueTowersDestroyed', 'blueGoldDiff', 'blueExperienceDiff']
lolFeaturesList = lolFeaturesDataFrame.values.tolist()
lolWinList = lolWinDataFrame.values.tolist()

print(lolFeaturesNames)
print(lolFeaturesDataFrame)
print(lolWinDataFrame)

clf = tree.DecisionTreeClassifier(max_depth=3)
clf = clf.fit(lolFeaturesList, lolWinList)

print(lolWinList)
print(clf.predict(lolFeaturesList))


dot_data = tree.export_graphviz(clf,
                                out_file = None,
                                feature_names=lolFeaturesNames,
                                class_names=['blueWin', 'blueLoss'],
                                filled=True,
                                rounded=True,
                                impurity=False)
print(dot_data)