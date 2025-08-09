import pandas as pd 
from pandas import DataFrame

def load_data(path:str) -> DataFrame:
    return pd.read_csv(path)

def write_data(path:str) -> DataFrame:
    pass
