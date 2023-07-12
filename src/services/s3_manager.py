import boto3
import pickle

s3 = boto3.client('s3')

class S3Manager():
    def load_dataframe(self):
        return pickle.loads(s3.get_object(Bucket='fraud-detection-models', Key='creditcard-dataframe.pkl').get('Body').read())

    def load_model(self):
        return pickle.loads(s3.get_object(Bucket='fraud-detection-models', Key='smote-3nn-model.pkl').get('Body').read())
