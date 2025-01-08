import matplotlib as plt
import numpy as np
import pandas as pd

lolDataFrame = pd.read_csv('datav2.csv',  delimiter=',', decimal='.')
lolFeaturesDataFrame = pd.DataFrame(lolDataFrame, columns=['blueKillDiff', 'blueGoldDiff', 'blueExperienceDiff'])
lolWinDataFrame = pd.DataFrame(lolDataFrame, columns=['blueWins'])

plt.hist(lolFeaturesDataFrame)
plt.show()
