import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load CSV data
csv_file = 'C:\workspace\didiksha\project\data'
target_column = 'target'

data = pd.read_csv(csv_file)

# Split data into features and target
X = data.drop(columns=[target_column])
y = data[target_column]

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
accuracy = model.score(X_test, y_test)
