import numpy as np
import pandas as pd

def true_false(x):
    """
        Padroniza os resultados de perguntas binárias. Quando a entrada
        é 'False' ou '0', ela se tornará 0. Quando 'True' ou '1', será
        1.
        
        Inputs:
            df: dataframe 
            col: str coluna do dataframe cujos resultados serão alterados

    """
    if x == 'False' or x == '0':
        x = 0
    if x == 'True'or x == '1':
        x = 1
    return x

def replace_all(df, col):
    """
        Aplica as correções possíveis.
        
        Inputs:
            df: dataframe 
            col: str coluna do dataframe cujos resultados serão alterados

    """
    df[col] = df[col].apply(lambda x: x.replace('\\u00d4', 'Ô'))
    df[col] = df[col].apply(lambda x: x.replace('\\u00f4', 'ô'))
    df[col] = df[col].apply(lambda x: x.replace('\\u00e3o', 'ão'))
    df[col] = df[col].apply(lambda x: x.replace('\\u00e7a',  'ça'))
    df[col] = df[col].apply(lambda x: x.replace("\\u00f",  'ú'))
    df[col] = df[col].apply(lambda x: x.replace("\\u00e2",  'â'))
    df[col] = df[col].apply(lambda x: x.replace("\\u00ea",  'ê'))
    df[col] = df[col].apply(lambda x: x.replace("\\u00e9",  'é'))
    df[col] = df[col].apply(lambda x: x.replace("\\u00e1",  'á'))
    df[col] = df[col].apply(lambda x: x.replace("\\u00f3",  'ó'))
    df[col] = df[col].apply(lambda x: x.replace("\\u00ed",  'í'))
    df[col] = df[col].apply(lambda x: x.replace("tú3rio",  'tório'))
    df[col] = df[col].apply(lambda x: x.replace("lú3gico",  'lógico'))
    df[col] = df[col].apply(lambda x: x.replace('[', ''))
    df[col] = df[col].apply(lambda x: x.replace(']',  ''))
    df[col] = df[col].apply(lambda x: x.replace('"', ''))
    df[col] = df[col].apply(lambda x: x.replace("'", ''))
    
    
def data(df, col):
    """
        Transforma a coluna com informação de data em datetime.
        
        Inputs:
            df: dataframe 
            col: str coluna do dataframe cujos resultados serão alterados

    """
    df[col] = pd.to_datetime(df[col], format='mixed')

