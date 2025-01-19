import matplotlib.pyplot as plt
from Tree import FraudDataFrame, clf, X_test, y_test, tree, feature_columns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
import numpy as np

def bar_plot():
    fraud_counts = FraudDataFrame['Fraud'].value_counts()
    fraud_counts.plot(kind='bar', color=['blue', 'orange'])
    plt.title('Distribution of Fraudulent vs. Non-Fraudulent Transactions')
    plt.xlabel('Fraud')
    plt.ylabel('Count')
    plt.xticks([0, 1], ['Not Fraud', 'Fraud'], rotation=0)
    plt.show()

def fraudtree():
    plt.figure(figsize=(12, 8))
    tree.plot_tree(clf, feature_names=feature_columns, class_names=['NotFraud', 'Fraud'], filled=True)
    plt.show()

def fraudDetectionOT():
    FraudDataFrame['TransactionDate'] = pd.to_datetime(FraudDataFrame['TransactionDate'], unit='s')
    FraudDataFrame.groupby(FraudDataFrame['TransactionDate'].dt.to_period('M'))['Fraud'].sum().plot(kind='line')
    plt.title('Fraudulent Transactions Over Time')
    plt.xlabel('Month')
    plt.ylabel('Count of Fraudulent Transactions')
    plt.show()


def dif_matrix():
    y_pred = clf.predict(X_test)
    cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Not Fraud', 'Fraud'])
    disp.plot(cmap='Blues')
    plt.show()

def feature_importance():

    importances = clf.feature_importances_
    indices = np.argsort(importances)[::-1]
    plt.bar(range(len(feature_columns)), importances[indices], align='center')
    plt.xticks(range(len(feature_columns)), np.array(feature_columns)[indices], rotation=45)
    plt.title('Feature Importance')
    plt.show()

bar_plot()
fraudtree()
dif_matrix()
fraudDetectionOT()
feature_importance()