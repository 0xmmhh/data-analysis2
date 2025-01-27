from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np
import pydotplus
from IPython.display import Image

features = [[1,3],[2,3],[3,1],[3,1],[2,2]]
labels = [1,1,2,2,3]
# 1 for green, 2 for yellow, 3 for red
# 1 for apple, 2 for grape, 3 for lemon

# declare the classifier
clf = tree.DecisionTreeClassifier()

# fit on training data
model = clf.fit(features, labels)

# check on training data
print(labels) # should be
print(clf.predict(features)) # is

# take a look at the tree
clf

# create DOT data
dot_data = tree.export_graphviz(clf, 
                                out_file=None, 
                                feature_names=['color','diameter'], 
                                class_names=['apple','grape','lemon'], 
                                filled=True, 
                                rounded=True, 
                                impurity=False)
            
print(dot_data)
def fruitstree():
    plt.figure(figsize=(32, 12))
    tree.plot_tree(clf, feature_names=['color','diameter'], class_names=['apple','grape','lemon'], filled=True)

    plt.show()

fruitstree()