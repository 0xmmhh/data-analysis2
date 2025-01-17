import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load dataset
print("Diamond rank league of legends statistics at minute 10.")
lolDataFrame = pd.read_csv('FraudData.csv', delimiter=',', decimal='.')

# Define feature and target columns
feature_columns = [
    'TransactionAmount', 'TransactionDate', 'TransactionType', 'Location',
    'DeviceID', 'IP Address', 'MerchantID', 'Channel', 'CustomerAge',
    'CustomerOccupation', 'TransactionDuration', 'LoginAttempts',
    'AccountBalance', 'PreviousTransactionDate'
]

target_column = 'Fraud'

# Preprocess data
lolDataFrame['TransactionDate'] = pd.to_datetime(lolDataFrame['TransactionDate'])
lolDataFrame['PreviousTransactionDate'] = pd.to_datetime(lolDataFrame['PreviousTransactionDate'])
lolDataFrame['TransactionDate'] = (lolDataFrame['TransactionDate'] - pd.Timestamp("1970-01-01")).dt.total_seconds()
lolDataFrame['PreviousTransactionDate'] = (lolDataFrame['PreviousTransactionDate'] - pd.Timestamp("1970-01-01")).dt.total_seconds()

categorical_columns = ['TransactionType', 'Location', 'DeviceID', 'IP Address', 'MerchantID', 'Channel', 'CustomerOccupation']
label_encoders = {}
for column in categorical_columns:
    le = LabelEncoder()
    lolDataFrame[column] = le.fit_transform(lolDataFrame[column])
    label_encoders[column] = le

# Prepare features and target
lolFeaturesDataFrame = lolDataFrame[feature_columns]
lolWinDataFrame = lolDataFrame[[target_column]]

# Convert DataFrame to values for the model
lolFeaturesList = lolFeaturesDataFrame.values
lolWinList = lolWinDataFrame.values.ravel()

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(lolFeaturesList, lolWinList, test_size=0.2, random_state=42)

# Train Decision Tree Classifier
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Display predictions
predictions = clf.predict(X_test)
print("Predictions:", predictions)

# Export decision tree to DOT format
dot_data = tree.export_graphviz(
    clf,
    out_file=None,
    feature_names=feature_columns,
    class_names=['NotFraud', 'Fraud'],
    filled=True,
    rounded=True,
    impurity=False
)

print("DOT data for the decision tree:")
print(dot_data)
