import pandas as pd
from processing import sales_processing
from processing import sales_utils
from pandas import DataFrame

def test_remove_null():
    input_df=sales_utils.load_data("/Users/sarasolis/python-test/src/data/raw/sales_data.csv")
    input_nulls = input_df.isnull().values.any()

    output_df = sales_processing.clean_null_values(input_df)
    output_nulls = input_df.isnull().values.any()
    print(input_nulls)

    assert input_nulls != output_nulls 
  


def test_cast_typer():
    schema = {
        'order_id': 'Int64',
        'customer_id': 'Int64',     
        'date': 'datetime64[ns]',
        'product': 'string',          
        'category': 'string',
        'price': 'string',
        'quantity': 'Int64',
        'store': 'string'
    }

    input_df=sales_utils.load_data("/Users/sarasolis/python-test/src/data/raw/sales_data.csv")
    output_df=sales_processing.cast_schema(input_df, schema)
    
    same_schema = input_df.dtypes.equals(output_df.dtypes)

    assert False==same_schema
 
def test_cast_date():
    schema = {
        'order_id': 'Int64',
        'customer_id': 'Int64',     
        'date': 'string',
        'product': 'string',          
        'category': 'string',
        'price': 'string',
        'quantity': 'Int64',
        'store': 'string'
    }
    input_df=sales_utils.load_data("/Users/sarasolis/python-test/src/data/raw/sales_data.csv")
    output_df=sales_processing.cast_schema(input_df, schema)
    output_df=sales_processing.cast_date(output_df)

    same_schema = input_df.dtypes.equals(output_df.dtypes)

    assert input_df['date'].dtypes !=  output_df['date'].dtypes


def test_cast_dicc():
    input_df=sales_utils.load_data("/Users/sarasolis/python-test/src/data/raw/sales_data.csv")
    schema = {
        'order_id': 'Int64',
        'customer_id': 'Int64',     
        'date': 'string',
        'product': 'string',          
        'category': 'string',
        'price': 'string',
        'quantity': 'Int64',
        'store': 'string'
    }

    print(input_df.dtypes)
    output_df = sales_processing.cast_dicc(input_df, schema)
    same_schema = input_df.dtypes.equals(output_df.dtypes) #why equal if not 

    print(output_df.dtypes)

    assert False==same_schema