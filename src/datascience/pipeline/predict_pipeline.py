import joblib
from pathlib import Path

class PredictionPipeline():
    def __init__(self):
        self.model = joblib.load("artifacts/model_trainer/model.joblib")

    def predicts(self, data):
        result = self.model.predict(data)
        return result