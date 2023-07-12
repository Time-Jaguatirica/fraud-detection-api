from imblearn.over_sampling import SMOTE

class SmoteSampler():
    def __init__(self, dataframe) -> None:
        self.dataframe = dataframe

    def get_xy(self):
        X = self.dataframe.drop('Class', axis=1)
        y = self.dataframe['Class']

        sm = SMOTE(random_state=42,sampling_strategy='minority')
        X_smote, y_smote = sm.fit_resample(X, y)

        return X_smote, y_smote
