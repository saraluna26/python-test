import pandas as pd
from pandas import DataFrame


def null_values(df:DataFrame) -> DataFrame:
    pass
# fillna ()

def group_by_customer(df:DataFrame, customer_id: int) -> DataFrame: 
    pass

def group_by_category(df:DataFrame, customer_id: int) -> DataFrame: 
    pass

def normalize_string_cols(df:DataFrame) -> DataFrame: 
    pass

def cast_schema(df:DataFrame, schema) -> DataFrame:
    return df.astype(schema)

def cast_date(df:DataFrame) -> DataFrame:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df

def get_category_income(df:DataFrame) -> DataFrame:
    pass

