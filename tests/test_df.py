import pandas as pd 
import numpy as np

def test_df_shape(path = 'data/UCI_Credit_Card.csv'):

    """
    Our dataset must have a shape of (30000, 25)
    
    """


    df = pd.read_csv(path)
    assert df.shape == (30000, 25)


def test_df_columns(path = 'data/UCI_Credit_Card.csv'):
    """
    Our dataset must have the following columns:
    ['ID', 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0',
       'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
       'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
       'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6',
       'default.payment.next.month']
    """

    df = pd.read_csv(path)
    assert df.columns.tolist() == ['ID', 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0',
       'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
       'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
       'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6',
       'default.payment.next.month']
    

def test_df_dtypes(path = 'data/UCI_Credit_Card.csv'):
    """
    Our dataset must have the following dtypes:
    ID                              int64
    LIMIT_BAL                     float64
    SEX                             int64
    EDUCATION                       int64
    MARRIAGE                        int64
    AGE                             int64
    PAY_0                           int64
    PAY_2                           int64
    PAY_3                           int64
    PAY_4                           int64
    PAY_5                           int64
    PAY_6                           int64
    BILL_AMT1                     float64
    BILL_AMT2                     float64
    BILL_AMT3                     float64
    BILL_AMT4                     float64
    BILL_AMT5                     float64
    BILL_AMT6                     float64
    PAY_AMT1                      float64
    PAY_AMT2                      float64
    PAY_AMT3                      float64
    PAY_AMT4                      float64
    PAY_AMT5                      float64
    PAY_AMT6                      float64
    default.payment.next.month      int64
    dtype: object
    """
    
    df = pd.read_csv(path)
    assert df.dtypes.to_dict() == {'ID': np.int64,
    'LIMIT_BAL': np.float64,
    'SEX': np.int64,
    'EDUCATION': np.int64,
    'MARRIAGE': np.int64,
    'AGE': np.int64,
    'PAY_0': np.int64,
    'PAY_2': np.int64,
    'PAY_3': np.int64,
    'PAY_4': np.int64,
    'PAY_5': np.int64,
    'PAY_6': np.int64,
    'BILL_AMT1': np.float64,
    'BILL_AMT2': np.float64,
    'BILL_AMT3': np.float64,
    'BILL_AMT4': np.float64,
    'BILL_AMT5': np.float64,
    'BILL_AMT6': np.float64,
    'PAY_AMT1': np.float64,
    'PAY_AMT2': np.float64,
    'PAY_AMT3': np.float64,
    'PAY_AMT4': np.float64,
    'PAY_AMT5': np.float64,
    'PAY_AMT6': np.float64,
    'default.payment.next.month': np.int64}
