import pandas as pd
import boto3
import pickle

s3 = boto3.client('s3')

class KNNClassificator():
    def __init__(self, n_neighbors=3):
        self.dataframe = self.load_dataframe()
        self.model = self.load_model()
        self.n_neighbors = 3

    def load_dataframe(self):
        return pickle.loads(s3.get_object(Bucket="fraud-detection-models", Key="creditcard-dataframe.pkl").get("Body").read())

    def load_model(self):
        return pickle.loads(s3.get_object(Bucket="fraud-detection-models", Key="smote-3nn-model.pkl").get("Body").read())

    def get_features(self) -> list:
        return list(self.dataframe.columns)
