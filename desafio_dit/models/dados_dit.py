import pandas as pd

csv_path = "~\desafio\dados_ficha_a_desafio.csv"

def model(dbt, session):
    df_pandas = pd.read_csv(csv_path)
    
    return df_pandas

  


