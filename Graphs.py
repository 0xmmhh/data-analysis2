import matplotlib.pyplot as plt
from Tree import FraudDataFrame, clf, X_test, y_test, tree, feature_columns, label_encoders
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
    plt.figure(figsize=(24, 14))
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
    plt.xticks(range(len(feature_columns)), np.array(feature_columns)[indices], rotation=12)
    plt.title('Feature Importance')
    plt.show()

def fraud_by_day_of_week():
    # Grupowanie po dniu tygodnia i zliczanie oszustw
    fraud_by_day = FraudDataFrame.groupby('DayOfWeek')['Fraud'].sum()

    # Wykres słupkowy
    fraud_by_day.plot(kind='bar', color='purple')
    plt.title('Fraudulent Transactions by Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Count of Fraudulent Transactions')
    plt.xticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], rotation=0)
    plt.show()

def decode_labels(encoded_column, label_encoder):
    return label_encoder.inverse_transform(encoded_column)

# Oszustwa na tle zawodów (przykład użycia inverse_transform)
def fraud_by_occupation():
    fraud_by_occupation = FraudDataFrame.groupby('CustomerOccupation')['Fraud'].sum()
    fraud_by_occupation_sorted = fraud_by_occupation.sort_values(ascending=False)

    # Dekodowanie zawodów
    occupation_names = decode_labels(fraud_by_occupation_sorted.index, label_encoders['CustomerOccupation'])

    # Wykres
    fraud_by_occupation_sorted.plot(kind='barh', color='teal', figsize=(10, 7))
    plt.yticks(ticks=range(len(occupation_names)), labels=occupation_names)
    plt.title('Fraudulent Transactions by Customer Occupation')
    plt.xlabel('Count of Fraudulent Transactions')
    plt.ylabel('Customer Occupation')
    plt.show()


def fraud_by_location():
    # Grupowanie po lokalizacji i zliczanie oszustw
    fraud_by_location = FraudDataFrame.groupby('Location')['Fraud'].sum().sort_values(ascending=False)

    # Dekodowanie lokalizacji
    location_names = decode_labels(fraud_by_location.index, label_encoders['Location'])

    # Tworzymy wykres słupkowy
    ax = fraud_by_location.plot(kind='bar', color='orange', figsize=(12, 6))

    # Dodajemy etykiety lokalizacji na słupkach (tuż nad osią X)
    for i, label in enumerate(location_names):
        ax.text(i, 0.05, label, ha='center', va='bottom', rotation=90, fontsize=10)  # Ustawiamy etykiety tuż nad osią X

    # Dodajemy liczby oszustw nad słupkami
    ax.bar_label(ax.containers[0], labels=fraud_by_location.values, padding=3, fontsize=10)

    # Ustawienie tytułów i etykiet
    plt.title('Fraudulent Transactions by Location')
    plt.xlabel('Location')
    plt.ylabel('Count of Fraudulent Transactions')
    plt.show()



def fraud_by_transaction_type():
    # Grupowanie po typie transakcji i zliczanie oszustw
    fraud_by_type = FraudDataFrame.groupby('TransactionType')['Fraud'].sum()

    # Dekodowanie typu transakcji
    transaction_type_names = decode_labels(fraud_by_type.index, label_encoders['TransactionType'])

    # Wykres
    fraud_by_type.plot(kind='bar', color='brown', figsize=(8, 6))
    plt.xticks(ticks=range(len(transaction_type_names)), labels=transaction_type_names, rotation=0)
    plt.title('Fraudulent Transactions by Transaction Type')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count of Fraudulent Transactions')
    plt.show()






bar_plot()
fraudtree()
dif_matrix()
fraudDetectionOT()
feature_importance()
fraud_by_day_of_week()
fraud_by_occupation()
fraud_by_location()
fraud_by_transaction_type()