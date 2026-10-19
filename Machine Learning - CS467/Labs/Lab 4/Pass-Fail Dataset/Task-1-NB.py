import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset from a URL
df = pd.read_csv("Pass-Fail Data.csv")
print(df.columns)

class NaiveBayes:
    def fit(self, X, y):
        # to be implemented
        X = np.asarray(X, dtype=float)
        y = np.asarray(y)
        self.classes = np.unique(y)
        self.means = {}
        self.variances = {}
        self.priors = {}

        for class_label in self.classes:
            class_features = X[y == class_label]
            self.means[class_label] = np.mean(class_features, axis=0)
            self.variances[class_label] = np.var(class_features, axis=0)
            self.priors[class_label] = len(class_features) / len(y)

        return self

    def predict(self, X):
        # to be implemented
        X = np.asarray(X, dtype=float)
        predictions = []

        for sample in X:
            log_probabilities = {}
            for class_label in self.classes:
                mean = self.means[class_label]
                variance = np.maximum(self.variances[class_label], 1e-9)
                log_density = -0.5 * (
                    np.log(2 * np.pi * variance)
                    + ((sample - mean) ** 2 / variance)
                )
                log_probabilities[class_label] = (
                    np.log(self.priors[class_label]) + np.sum(log_density)
                )
            predictions.append(max(log_probabilities, key=log_probabilities.get))

        return np.asarray(predictions)

# Split dataset into features and target
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # 70% training and 30% test

# Create a Naive Bayes Classifier
nb = NaiveBayes()

# Train the model using the training sets
nb.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = nb.predict(X_test)

# Model Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))