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

def rel(x):
    """
        Padroniza os resultados da pergunta 'religiao'. 
        
        Inputs:
            x: str

    """
    outras = ['Sim', 'ORQUIDEA', '10 EAP 01', 'ESB ALMIRANTE', 'Acomp. Cresc. e Desenv. da Criança']
    religioes = ['Sem religião', 'Católica', 'Outra', 'Evangélica', 'Espírita',
                    'Religião de matriz africana', 'Nao declarado', 'Budismo',
                    'Judaísmo', 'Islamismo']
    if x in outras:
        x = 'Outra'
    elif x == 'Candomblé':
        x = 'Religião de matriz africana'
    elif x == 'Não':
        x = 'Nao declarado'
    elif x not in religioes:
        x = 'Nao declarado'
    return x

def renda(x):
    """
        Padroniza os resultados da pergunta 'renda_familiar'.
        
        Inputs:
            x: str 

    """
    if x == '1/2 Salário Mínimo' or x == '1/4 Salário Mínimo':
        x = 'Menos de 1'
    elif x == '1 Salário Mínimo':
        x = '1'
    elif x == '2 Salários Mínimos':
        x = '2'
    elif x == '3 Salários Mínimos':
        x = '3'
    elif x == '4 Salários Mínimos' or x == 'Mais de 4 Salários Mínimos':
        x = '4 ou mais'
    else:
        x = 'Nao declarado'
    return x

def size(x):
    """
        Força resultados maiores que 4 serem 'Outros'.
        
        Inputs:
            x: str 

    """
    num = len(x.split())
    if num > 4:
        x = 'Outros'
    return x

def sort_and_correct(x):
    """
        Ordena e remove colchetes e aspas de string.

        Inputs:
            x: str
    """
    num = len(x.split())
    if num > 1:
            x = str(sorted(x.split(', '))).replace("[", '').replace(']', '').replace("'", '')
    return x

def gen(x):
    """
        Corrige as entradas da coluna 'identidade_genero'.
        Inputs:
            x: str
    """
    if x == 'Não':
        x = 'Nao declarado'
    if x == 'Mulher transexual' or x == 'Homem transexual' or x == 'Travesti':
        x = 'Trans'
    if x == 'Bissexual' or x =='Homossexual (gay / lésbica)' or x == 'Heterossexual' or x == 'Sim':
        x = 'Nao se aplica'
    return x

def racacor(x):
    """
        Corrige as entradas da coluna 'raca_cor'.
        Inputs:
            x: str
    """
    racas = ['Parda', 'Branca', 'Preta', 'Amarela', 'Indígena', 'Nao declarado']
    if x not in racas:
        x = 'Outro'
    return x

def alt(x):
    """
        Força resultados maiores que 258.0 serem np.nan.
        
        Inputs:
            x: str 

    """
    if x > 258.0:
        x = np.nan
    return x

def peso(x):
    """
        Força resultados maiores que 200.0 serem np.nan.
        
        Inputs:
            x: str 

    """
    if x > 200.0:
        x = np.nan
    return x

def press(x):
    """
        Força resultados maiores que 250.0 serem np.nan.
        
        Inputs:
            x: str 

    """
    if x > 250.0:
        x = np.nan
    return x

def prof(x):
    """
            Corrige entradas da coluna 'situacao_profissional'.
            
            Inputs:
                x: str 

    """
    if x == 'Não trabalha':
        x = 'Desempregado'
    elif x == 'Médico Urologista':
        x = 'Emprego Formal'
    elif x == 'SMS CAPS DIRCINHA E LINDA BATISTA AP 33':
        x = 'Não se aplica'
    elif x == 'Autônomo sem previdência social' or x == 'Autônomo com previdência social':
        x = 'Autônomo'

    situs = ['Emprego Formal', 'Não se aplica', 'Desempregado', 
        'Emprego Informal', 'Pensionista / Aposentado', 'Autônomo', 'Outro', 'Empregador' ]
    
    if x not in situs:
        x = 'Outro'
    return x