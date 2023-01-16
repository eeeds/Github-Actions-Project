import pandas as pd 

def test_df_shape(path = 'data/UCI_Credit_Card.csv'):

    """
    Our dataset must have a shape of (30000, 25)
    
    """


    df = pd.read_csv(path)
    assert df.shape == (30000, 25)

