import pandas as pd
from pandas import DataFrame


def clean_null_values(df:DataFrame) -> DataFrame:
    for col in df.columns:
        if df[col].dtype in ['string', 'object']:
            df[col] = df[col].fillna('NA')
        elif df[col].dtype in ['Int64', 'float']:
            df[col] = df[col].fillna(0)

    print(df)
    return df

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

