import pandas as pd
from processing import sales_processing
from processing import sales_utils
from pandas import DataFrame

def test_remove_null():
    # input_df=sales_utils.load_data("/Users/sarasolis/python-test/src/data/raw/sales_data.csv")
    # output_df=input_df 
    # input_df.isnull
    # output_df

    # assert 
    pass


def test_cast_typer():
    schema = {
        'order_id': 'int64',
        'customer_id': 'int64',     
        'date': 'string',
        'product': 'string',          
        'category': 'string',
        'price': 'string',
        'quantity': 'int64',
        'store': 'string'
    }

    input_df=sales_utils.load_data("/Users/sarasolis/python-test/src/data/raw/sales_data.csv")
    output_df=sales_processing.cast_schema(input_df, schema)
    
    same_schema = input_df.dtypes.equals(output_df.dtypes)

    assert False==same_schema
 
def test_cast_date():
    schema = {
        'order_id': 'int64',
        'customer_id': 'int64',     
        'date': 'string',
        'product': 'string',          
        'category': 'string',
        'price': 'string',
        'quantity': 'int64',
        'store': 'string'
    }
    input_df=sales_utils.load_data("/Users/sarasolis/python-test/src/data/raw/sales_data.csv")
    output_df=sales_processing.cast_schema(input_df, schema)
    output_df=sales_processing.cast_date(output_df)

    same_schema = input_df.dtypes.equals(output_df.dtypes)

    assert input_df['date'].dtypes !=  output_df['date'].dtypes

