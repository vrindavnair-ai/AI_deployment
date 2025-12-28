from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class IrisModel:
    def __init__(self):
        self.model = None
        self.target_names = None

    def train(self):
        data = load_iris()
        X = data.data
        y = data.target
        self.target_names = data.target_names

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        clf = LogisticRegression(max_iter=200)
        clf.fit(X_train, y_train)
        self.model = clf

    def predict(self, features):
        """
        features: [sepal_length, sepal_width, petal_length, petal_width]
        """
        pred_idx = self.model.predict([features])[0]
        return {
            "class_index": int(pred_idx),
            "class_name": self.target_names[pred_idx],
        }


iris_model = IrisModel()
iris_model.train()
