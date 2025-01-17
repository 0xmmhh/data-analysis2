import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

lolDataFrame = pd.read_csv('datav2.csv',  delimiter=',', decimal='.')
x = pd.DataFrame(lolDataFrame, columns=['blueKillDiff', 'blueGoldDiff', 'blueExperienceDiff'])
h = pd.DataFrame(lolDataFrame, columns=['blueGoldDiff', 'redGoldDiff'])
lolWinDataFrame = pd.DataFrame(lolDataFrame, columns=['blueWins'])
y = pd.DataFrame(lolDataFrame, columns=['blueTotalExperience'])
z = pd.DataFrame(lolDataFrame, columns=['redTotalExperience'])
i = pd.DataFrame(lolDataFrame, columns=['blueTotalGold'])
j = pd.DataFrame(lolDataFrame, columns=['redTotalGold'])
plt.hist(h)
plt.show()
plt.scatter(y, i, color='#0000FF',  alpha=0.3)
plt.scatter(z, j, color='#FF0000', alpha=0.1)
plt.show()