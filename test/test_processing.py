from processing import sales_utils
import pandas as pd

def test_load_csv():
    input_df= pd.DataFrame()
    output_df = sales_utils.load_data("/Users/sarasolis/python-test/src/data/raw/sales_data.csv")
    output_cols = len(output_df.columns) 
    input_cols = len(input_df.columns)
    
    assert output_cols != input_cols
