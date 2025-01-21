from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

import numpy as np
import pydotplus
from IPython.display import Image

from sklearn.datasets import load_iris

iris = load_iris()

print(iris.feature_names) # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print(iris.target_names) # ['setosa' 'versicolor' 'virginica']

print(iris.data[0]) #first flower - features
print(iris.target[0]) #first flower - class

test_idx = [0, 3, 5, 50, 53, 55, 100, 103, 105]

test_data = iris.data[test_idx]
test_target = iris.target[test_idx]

train_data = np.delete(iris.data, test_idx, axis=0)
train_target = np.delete(iris.target, test_idx)

clf = DecisionTreeClassifier(random_state=1234)

model = clf.fit(train_data, train_target)

print(test_target) # should be
print(clf.predict(test_data)) # is

model

dot_data = tree.export_graphviz(model, 
                                out_file=None, 
                                feature_names=iris.feature_names, 
                                class_names=iris.target_names, 
                                filled=True, 
                                rounded=True, 
                                impurity=False)

print(dot_data)