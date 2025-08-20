# src/cleaning.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[column] = df[column].fillna(df[column].median())
    return df


def drop_missing(df: pd.DataFrame, threshold: float = 0.7) -> pd.DataFrame:
    return df.dropna(axis=1, thresh=int(threshold * len(df)))


def normalize_data(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df
