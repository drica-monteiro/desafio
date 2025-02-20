import numpy as np
import pandas as pd

from utils import true_false, replace_all, data

def ids_repetidas(df):
    """
        Remove as ids repetidas na coluna 'id_paciente'.
        Adiciona '__int' nas ids repetidas.
        
        Inputs:
            df: dataframe 

    """
    # Conta todas as ids e as repetidas
    ids_todas = pd.DataFrame(df['id_paciente'].value_counts())
    ids_repetidas = ids_todas[ids_todas['count'] != 1]

    # Adiciona '__i' nas repetidas
    n = df.shape[0]
    for i in range(n):
        if df.iloc[i,0] in ids_repetidas.index:
            df.iloc[i,0] = df.iloc[i,0] + f'__{i}'

def obito(df):
    """
        Aplica as correções possíveis na coluna 'obito'.
        Padroniza os resultados de perguntas binárias. Quando a entrada
        é 'False' ou '0', ela se tornará 0. Quando 'True' ou '1', será
        1.
        
        Inputs:
            df: dataframe 

    """
    # Aplica a funcao true_false
    df['obito'] = df['obito'].apply(true_false)

def luz_eletrica(df):
    """
        Aplica as correções possíveis na coluna 'luz_eletrica'.
        Padroniza os resultados de perguntas binárias. Quando a entrada
        é 'False' ou '0', ela se tornará 0. Quando 'True' ou '1', será
        1.
        
        Inputs:
            df: dataframe 

    """
    # Aplica a funcao true_false
    df['luz_eletrica'] = df['luz_eletrica'].apply(true_false)

def em_situacao_de_rua(df):
    """
        Aplica as correções possíveis na coluna 'em_situacao_de_rua'.
        Padroniza os resultados de perguntas binárias. Quando a entrada
        é 'False' ou '0', ela se tornará 0. Quando 'True' ou '1', será
        1.
        
        Inputs:
            df: dataframe 

    """
    # Aplica a funcao true_false
    df['em_situacao_de_rua'] = df['em_situacao_de_rua'].apply(true_false)
    

def possui_plano_saude(df):
    """
        Aplica as correções possíveis na coluna 'possui_plano_saude'.
        Padroniza os resultados de perguntas binárias. Quando a entrada
        é 'False' ou '0', ela se tornará 0. Quando 'True' ou '1', será
        1.
        
        Inputs:
            df: dataframe 

    """
    # Aplica a funcao true_false
    df['possui_plano_saude'] = df['possui_plano_saude'].apply(true_false)


def vulnerabilidade_social(df):
    """
        Aplica as correções possíveis na coluna 'vulnerabilidade_social'.
        Padroniza os resultados de perguntas binárias. Quando a entrada
        é 'False' ou '0', ela se tornará 0. Quando 'True' ou '1', será
        1.
        
        Inputs:
            df: dataframe 

    """
    # Aplica a funcao true_false
    df['vulnerabilidade_social'] = df['vulnerabilidade_social'].apply(true_false)


def fam_aux_bra(df):
    """
        Aplica as correções possíveis na coluna 'familia_beneficiaria_auxilio_brasil'.
        Padroniza os resultados de perguntas binárias. Quando a entrada
        é 'False' ou '0', ela se tornará 0. Quando 'True' ou '1', será
        1.
        
        Inputs:
            df: dataframe 

    """
    # Aplica a funcao true_false
    df['familia_beneficiaria_auxilio_brasil'] = df['familia_beneficiaria_auxilio_brasil'].apply(true_false)


def cria_matr_cre(df):
    """
        Aplica as correções possíveis na coluna 'crianca_matriculada_creche_pre_escola'.
        Padroniza os resultados de perguntas binárias. Quando a entrada
        é 'False' ou '0', ela se tornará 0. Quando 'True' ou '1', será
        1.
        
        Inputs:
            df: dataframe 

    """
    # Aplica a funcao true_false
    df['crianca_matriculada_creche_pre_escola'] = df['crianca_matriculada_creche_pre_escola'].apply(true_false)



def sexo_biologico(df):
    df.rename(columns={'sexo': 'sexo_biologico'}, inplace = True)

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

def religiao(df):
    """
        Padroniza os resultados da pergunta 'religiao'. As possíveis 
        respostas serão: 'Sem religião', 'Católica', 'Outra', 'Evangé-
        lica', 'Espírita', 'Religião de matriz africana', 'Nao declarado',
        'Budismo', 'Judaísmo', 'Islamismo'. Quaisquer respostas diferentes
        serão alteradas para 'Nao declarado'.
        
        Inputs:
            df: dataframe 
            col: coluna do dataframe cujos resultados serão alterados

    """
    df['religiao'] = df['religiao'].apply(rel)
    # Lista de entradas inadequadas
    # outras = ['Sim', 'ORQUIDEA', '10 EAP 01', 'ESB ALMIRANTE', 'Acomp. Cresc. e Desenv. da Criança']
    
    # # Corrige entradas inadequadas
    # n = df.shape[0]
    # index = df.columns.get_loc(col)
    # for i in range(n):
    #     if df.iloc[i,index] in outras:
    #         df.iloc[i,index] = 'Outra'
    #     elif df.iloc[i,index] == 'Candomblé':
    #         df.iloc[i,index] = 'Religião de matriz africana' # Candomblé é religiao de matriz africada
    #     elif df.iloc[i,index] == 'Não':
    #         df.iloc[i,index] = 'Nao declarado'

    # # Lista de religioes possiveis
    # religioes = ['Sem religião', 'Católica', 'Outra', 'Evangélica', 'Espírita',
    #             'Religião de matriz africana', 'Nao declarado', 'Budismo',
    #             'Judaísmo', 'Islamismo']
    
    # # Forca todas as entradas estarem nessa lista 
    # for i in range(n):
    #     if df.iloc[i,index] not in religioes:
    #         df.iloc[i,index] = 'Nao declarado'


def renda(x):
    """
        Padroniza os resultados da pergunta 'renda_familiar'.
        
        Inputs:
            x: str 

    """
    # Conserta as respostas
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

def renda_familiar(df):
    """
        Padroniza os resultados da pergunta 'renda_familiar'. As possíveis 
        respostas serão em número de salário: 'Menos de 1', '1', '2','3',
        '4 ou mais' e 'Nao declarado'. Quaisquer respostas diferentes
        serão alteradas para 'Nao declarado'.
        
        Inputs:
            df: dataframe 
    """

    # Aplica a funcao renda
    df['renda_familiar'] = df['renda_familiar'].apply(renda)
 

def meios_transporte(df):
    """
        Aplica as correções possíveis na coluna 'meios_transporte'.
        
        Inputs:
            df: dataframe 

    """
    # Remove entrada '[]'
    df.loc[df['meios_transporte'] == '[]','meios_transporte'] = 'Nao declarado'

    # Corrige erros de codificacao
    replace_all(df, 'meios_transporte')

    # Remove entradas com 5 ou mais opçoes
    n = df.shape[0]
    index = df.columns.get_loc('meios_transporte')
    for i in range(n):
        num = len(df.iloc[i,index].split())
        if num > 4:
            df.iloc[i,index] = 'Outros'

    # Ordena as entradas para identificar entradas iguais mas com ordem diferente
    for i in range(n):
        if num > 1:
            df.iloc[i,index] = str(sorted(df.iloc[i,index].split(', '))).replace("[", '').replace(']', '').replace("'", '')

    # Conta as entradas possíveis restantes
    series = df['meios_transporte'].value_counts()

    # Lista das entradas com mais de 95 aparições
    ind = int(np.where(series.values == 95)[0])
    meios = [meio for meio in series[0:ind].index]

    # Retira as entradas com menos de 95 aparições e força quaisquer entradas ser alguma dessa lista
    for i in range(n):
        if df.iloc[i,index] not in meios:
            df.iloc[i,index] = 'Outros'


def doencas_condicoes(df):
    """
        Aplica as correções possíveis na coluna 'doencas_condicoes'.
        
        Inputs:
            df: dataframe 

    """
    # Remove entrada '[]'
    df.loc[df['doencas_condicoes'] == '[]','doencas_condicoes'] = 'Nao declarado'

    # Corrige erros de codificacao
    replace_all(df, 'doencas_condicoes')

    # Remove entradas com 5 ou mais opçoes
    n = df.shape[0]
    index = df.columns.get_loc('doencas_condicoes')
    for i in range(n):
        num = len(df.iloc[i,index].split())
        if num > 4:
            df.iloc[i,index] = 'Outros'

    # Ordena as entradas para identificar entradas iguais mas com ordem diferente
    for i in range(n):
        if num > 1:
            df.iloc[i,index] = str(sorted(df.iloc[i,index].split(', '))).replace("[", '').replace(']', '').replace("'", '')

    # Conta as entradas possíveis restantes
    series = df['doencas_condicoes'].value_counts()

     # Lista das entradas com mais de 10 aparições
    ind = int(np.where(series.values == 10)[0][0])
    condicoes = [cond for cond in series[0:ind].index]

    # Retira as entradas com menos de 10 aparições e força quaisquer entradas ser alguma dessa lista
    for i in range(n):
        if df.iloc[i,index] not in condicoes:
            df.iloc[i,index] = 'Outros'

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

def identidade_genero(df):
    """
        Aplica as correções possíveis na coluna 'identidade_genero'.
        
        Inputs:
            df: dataframe 

    """
    df['identidade_genero'] = df['identidade_genero'].apply(gen)


def meios_comunicacao(df):
    """
        Aplica as correções possíveis na coluna 'meios_comunicacao'.
        
        Inputs:
            df: dataframe 

    """
    # Remove entrada '[]'
    df.loc[df['meios_comunicacao'] == '[]','meios_comunicacao'] = 'Nao declarado'

    # Corrige erros de codificacao
    replace_all(df, 'meios_comunicacao')

    # Remove entradas com 5 ou mais opçoes
    n = df.shape[0]
    index = df.columns.get_loc('meios_comunicacao')
    for i in range(n):
        num = len(df.iloc[i,index].split())
        if num > 4:
            df.iloc[i,index] = 'Outros'

    # Ordena as entradas para identificar entradas iguais mas com ordem diferente
    for i in range(n):
        if num > 1:
            df.iloc[i,index] = str(sorted(df.iloc[i,index].split(', '))).replace("[", '').replace(']', '').replace("'", '')

    # Conta as entradas possíveis restantes
    series = df['meios_comunicacao'].value_counts()

     # Lista das entradas com mais de 10 aparições
    ind = int(np.where(series.values == 10)[0][0])
    condicoes = [cond for cond in series[0:ind].index]

    # Retira as entradas com menos de 10 aparições e força quaisquer entradas ser alguma dessa lista
    for i in range(n):
        if df.iloc[i,index] not in condicoes:
            df.iloc[i,index] = 'Outros'

def em_caso_doenca_procura(df):
    """
        Aplica as correções possíveis na coluna 'em_caso_doenca_procura'.
        
        Inputs:
            df: dataframe 

    """
    # Remove entrada '[]'
    df.loc[df['em_caso_doenca_procura'] == '[]','em_caso_doenca_procura'] = 'Nao declarado'

    # Corrige erros de codificacao
    replace_all(df, 'em_caso_doenca_procura')


    # Conta as entradas possíveis restantes
    series = df['em_caso_doenca_procura'].value_counts()

     # Lista das entradas com mais de 10 aparições
    ind = int(np.where(series.values == 10)[0][0])
    condicoes = [cond for cond in series[0:ind].index]

    # Retira as entradas com menos de 10 aparições e força quaisquer entradas ser alguma dessa lista
    n = df.shape[0]
    index = df.columns.get_loc('em_caso_doenca_procura')
    for i in range(n):
        if df.iloc[i,index] not in condicoes:
            df.iloc[i,index] = 'Outros'

def data_at_cad(df):
    """
        Aplica a funcao data para a coluna 'data_atualizacao_cadastro'.
        Transforma a coluna com informação de data em datetime.
        
        Inputs:
            df: dataframe 

    """
    # Aplica a funcao data
    data(df, 'data_atualizacao_cadastro')

def data_nasc(df):
    """
        Aplica a funcao data para a coluna 'data_nascimento'.
        Transforma a coluna com informação de data em datetime.
        
        Inputs:
            df: dataframe 

    """
    # Aplica a funcao data
    data(df, 'data_nascimento')

def data_cad(df):
    """
        Aplica a funcao data para a coluna 'data_cadastro'.
        Transforma a coluna com informação de data em datetime.
        
        Inputs:
            df: dataframe 

    """
    # Aplica a funcao data
    data(df, 'data_cadastro')

def updated_at(df):
    """
        Aplica a funcao data para a coluna 'updated_at'.
        Transforma a coluna com informação de data em datetime.
        
        Inputs:
            df: dataframe 

    """
    # Aplica a funcao data
    data(df, 'updated_at')

def raca_cor(df):
    """
        Corrige entradas da coluna 'raca_cor'.
        As possibilidades são: 'Parda', 'Branca', 'Preta', 
        'Amarela', 'Indígena', 'Nao declarado'.
        
        Inputs:
            df: dataframe 

    """
    # Corrige as entradas 
    racas = ['Parda', 'Branca', 'Preta', 'Amarela', 'Indígena', 'Nao declarado']
    n = df.shape[0]
    index = df.columns.get_loc('raca_cor')
    for i in range(n):
        if df.iloc[i,index] not in racas:
            df.iloc[i,index] = 'Outro'


def altura(df):
    """
            Corrige entradas da coluna 'altura'.
            Como alturas maiores que 258.0 cm são extremamente raras,
            valores maiores que esse serao considerados um erro.
            
            Inputs:
                df: dataframe 

    """
    # Entradas maiores que 258.0 cm viram Nan
    n = df.shape[0]
    index = df.columns.get_loc('altura')
    for i in range(n):
        if df.iloc[i,index] > 258.0:
            df.iloc[i,index] = np.nan

def peso(df):
    """
            Corrige entradas da coluna 'peso'.
            Como pesos maiores que 200.0 kg são extremamente raras,
            valores maiores que esse serao considerados um erro.
            
            Inputs:
                df: dataframe 

    """
    # Entradas maiores que 200.0 cm viram Nan
    n = df.shape[0]
    index = df.columns.get_loc('peso')
    for i in range(n):
        if df.iloc[i,index] > 200.0:
            df.iloc[i,index] = np.nan


def pressao_sistolica(df):
    """
            Corrige entradas da coluna 'pressao_sistolica'.
            Como pressoes que 250 são extremamente raras,
            valores maiores que esse serao considerados um erro.
            
            Inputs:
                df: dataframe 

    """
    # Entradas maiores que 250.0 cm viram Nan
    n = df.shape[0]
    index = df.columns.get_loc('pressao_sistolica')
    for i in range(n):
        if df.iloc[i,index] > 250.0:
            df.iloc[i,index] = np.nan


def pressao_diastolica(df):
    """
            Corrige entradas da coluna 'pressao_diastolica'.
            Como pressoes que 200 são extremamente raras,
            valores maiores que esse serao considerados um erro.
            
            Inputs:
                df: dataframe 

    """
    # Entradas maiores que 200.0 cm viram Nan
    n = df.shape[0]
    index = df.columns.get_loc('pressao_diastolica')
    for i in range(n):
        if df.iloc[i,index] > 200.0:
            df.iloc[i,index] = np.nan

def prof(x):
    """
            Corrige entradas da coluna 'situacao_profissional'.
            
            Inputs:
                x: str 

    """
    # Corrige as entradas 
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

    # Remove outras entradas erradas e forca somente as entradas da lista
    if x not in situs:
        x = 'Outro'
    return x



def situ_prof(df):
    """
            Corrige entradas da coluna 'situacao_profissional'. 
            Evita entradas diferentes das seguintes: 'Emprego Formal', 
            'Não se aplica', 'Desempregado', 'Emprego Informal', 
            'Pensionista / Aposentado', 'Autônomo', 'Outro'
             e 'Empregador'.
            
            Inputs:
                df: dataframe 

    """
    # Aplica a funcao prof
    df['situacao_profissional'] = df['situacao_profissional'].apply(prof)

