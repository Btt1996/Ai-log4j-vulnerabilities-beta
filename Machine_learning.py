import json
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier

class Machine_learning:
    def __init__(self):
        self.classifier = RandomForestClassifier()
        self.model_filename = "vulnerability_model.pkl"

    def train(self, vulnerabilities):
        # Prepare the data for training
        # Extract features and labels
        X, y = self.prepare_data(vulnerabilities)
        # Train the classifier
        self.classifier.fit(X, y)
        # Save the model to disk
        joblib.dump(self.classifier, self.model_filename)

    def prepare_data(self, vulnerabilities):
        # Prepare the data for training
        X = []
        y = []
        for vulnerability in vulnerabilities:
            # Extract features and labels from the vulnerability
            features = self.extract_features(vulnerability)
            label = self.extract_label(vulnerability)
            X.append(features)
            y.append(label)
        return X, y

    def extract_features(self, vulnerability):
        # Extract features from the vulnerability
        # Example:
        return [vulnerability['severity'], vulnerability['age']]

    def extract_label(self, vulnerability):
        # Extract the label from the vulnerability
        # Example:
        return vulnerability['is_exploitable']

    def predict(self, vulnerabilities):
        # Load the model from disk
        classifier = joblib.load(self.model_filename)
        # Prepare the data for prediction
        X = []
        for vulnerability in vulnerabilities:
            # Extract features from the vulnerability
            features = self.extract_features(vulnerability)
            X.append(features)
        # Predict the labels for the vulnerabilities
        predictions = classifier.predict(X)
        return predictions

if __name__ == '__main__':
    # Load the vulnerabilities from File2
    with open('vulnerabilities.json') as f:
        vulnerabilities = json.load(f)
    # Initialize the Machine_learning class
    ml = Machine_learning()
    # Train the classifier
    ml.train(vulnerabilities)
    # Predict the labels for the vulnerabilities
    predictions = ml.predict(vulnerabilities)
    print(predictions)
