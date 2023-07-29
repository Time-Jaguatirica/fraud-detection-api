import boto3
import pickle
from shared.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

class S3Manager():
    def load_dataframe(self):
        return pickle.loads(s3.get_object(Bucket='fraud-detection-models', Key='creditcard-dataframe.pkl').get('Body').read())

    def load_model(self):
        return pickle.loads(s3.get_object(Bucket='fraud-detection-models', Key='random-forest-model.pkl').get('Body').read())
