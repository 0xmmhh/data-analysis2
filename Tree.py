import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

FraudDataFrame = pd.read_csv('FraudData.csv', delimiter=',', decimal='.')

feature_columns = [
    'TransactionAmount', 'TransactionType', 'CustomerAge',
    'TransactionDuration', 'LoginAttempts',
    'AccountBalance'
]

target_column = 'Fraud'

FraudDataFrame['TransactionDate'] = pd.to_datetime(FraudDataFrame['TransactionDate'])
FraudDataFrame['PreviousTransactionDate'] = pd.to_datetime(FraudDataFrame['PreviousTransactionDate'])
FraudDataFrame['TransactionDate'] = (FraudDataFrame['TransactionDate'] - pd.Timestamp("1970-01-01")).dt.total_seconds()
FraudDataFrame['PreviousTransactionDate'] = (
            FraudDataFrame['PreviousTransactionDate'] - pd.Timestamp("1970-01-01")).dt.total_seconds()

categorical_columns = ['TransactionType', 'Location', 'MerchantID', 'Channel', 'CustomerOccupation']
label_encoders = {}
for column in categorical_columns:
    le = LabelEncoder()
    FraudDataFrame[column] = le.fit_transform(FraudDataFrame[column])
    label_encoders[column] = le

FraudFeaturesDataFrame = FraudDataFrame[feature_columns]
IsFraudDataFrame = FraudDataFrame[[target_column]]

FraudFeaturesList = FraudFeaturesDataFrame.values
IsFraudList = IsFraudDataFrame.values.ravel()

X_train, X_test, y_train, y_test = train_test_split(FraudFeaturesList, IsFraudList, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Export drzewa do obrazu na stronce: http://webgraphviz.com/
dot_data = tree.export_graphviz(  # Nie jest potrzebny jako że w grafach dodałem generację drzewa
    clf,
    out_file=None,
    feature_names=feature_columns,
    class_names=['NotFraud', 'Fraud'],
    filled=True,
    rounded=True
)

print("\nDOT data for the decision tree: \n")
print(dot_data)

# wyniki algorytmu (1: oszustwa, 0: legit)

# Faktyczna suma oszustw wg. danych z pliku
fraud_counts = FraudDataFrame['Fraud'].value_counts()
print(fraud_counts)

# suma oszustw wg. drzewa decyzyjnego
predictions = clf.predict(FraudFeaturesList)

predicted_counts = pd.Series(predictions).value_counts()
print(predicted_counts)
# suma oszustw odczytanych z drzewa (Bez części testowej czyli 80% próbek)
train_counts = pd.Series(y_train).value_counts()
print("Training Data Fraud Counts:", train_counts)
