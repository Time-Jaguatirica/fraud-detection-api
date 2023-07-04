import pandas as pd

path = "./src/static/creditcard.csv"
default_df = pd.read_csv(path)

class DataFrame():
    def __init__(self, dataframe=default_df):
        self.dataframe = dataframe

    def get_features(self) -> list:
        return list(self.dataframe.columns)
