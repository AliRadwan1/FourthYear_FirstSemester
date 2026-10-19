import numpy as np
from collections import Counter
import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.spatial import distance

# k-NN Classifier
class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        # to be implemented
        X = np.asarray(X, dtype=float)
        predictions = []
        
        for sample in X:
            distances = np.linalg.norm(self.X_train - sample, axis=1)
            nearest_indices = np.argsort(distances)[:self.k]
            nearest_labels = self.y_train[nearest_indices]
            predictions.append(Counter(nearest_labels).most_common(1)[0][0])

        return np.asarray(predictions)

# Load the dataset from CSV file.
df = pd.read_csv("Pass-Fail Data.csv")

# Split dataset into features and target
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=1)  # 85% training and 15% test

# Create a k-NN Classifier
knn = KNN(k=3)

# Train the model using the training set
knn.fit(X_train, y_train)

# Predict the response for test set
y_pred = knn.predict(X_test)

# Model Accuracy
print("Accuracy:", np.sum(y_pred == y_test) / len(y_test))