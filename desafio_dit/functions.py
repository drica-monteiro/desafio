import numpy as np
import pandas as pd

from utils import true_false, replace_all, data
from utils import rel, renda, size, sort_and_correct, gen, racacor, alt, press, peso, prof

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
    """
        Muda o nome da coluna 'sexo' para 'sexo_biologico'.
        
        Inputs:
            df: dataframe 

    """
    df.rename(columns={'sexo': 'sexo_biologico'}, inplace = True)


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
    df['meios_transporte'] = df['meios_transporte'].apply(size)
    n = df.shape[0]
    index = df.columns.get_loc('meios_transporte')


    # Ordena as entradas para identificar entradas iguais mas com ordem diferente
    df['meios_transporte'] = df['meios_transporte'].apply(sort_and_correct)
    
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
    df['doencas_condicoes'] = df['doencas_condicoes'].apply(size)

    # Ordena as entradas para identificar entradas iguais mas com ordem diferente
    df['doencas_condicoes'] = df['doencas_condicoes'].apply(sort_and_correct)

    # Conta as entradas possíveis restantes
    series = df['doencas_condicoes'].value_counts()

     # Lista das entradas com mais de 10 aparições
    ind = int(np.where(series.values == 10)[0][0])
    condicoes = [cond for cond in series[0:ind].index]

    # Retira as entradas com menos de 10 aparições e força quaisquer entradas ser alguma dessa lista
    n = df.shape[0]
    index = df.columns.get_loc('doencas_condicoes')
    for i in range(n):
        if df.iloc[i,index] not in condicoes:
            df.iloc[i,index] = 'Outros'


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
    df['meios_comunicacao'] = df['meios_comunicacao'].apply(size)

    # Ordena as entradas para identificar entradas iguais mas com ordem diferente
    df['meios_comunicacao'] = df['meios_comunicacao'].apply(sort_and_correct)

    # Conta as entradas possíveis restantes
    series = df['meios_comunicacao'].value_counts()

     # Lista das entradas com mais de 10 aparições
    ind = int(np.where(series.values == 10)[0][0])
    condicoes = [cond for cond in series[0:ind].index]

    # Retira as entradas com menos de 10 aparições e força quaisquer entradas ser alguma dessa lista
    n = df.shape[0]
    index = df.columns.get_loc('meios_comunicacao')

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
    df['raca_cor'] = df['raca_cor'].apply(racacor)



def altura(df):
    """
            Corrige entradas da coluna 'altura'.
            Como alturas maiores que 258.0 cm são extremamente raras,
            valores maiores que esse serao considerados um erro.
            
            Inputs:
                df: dataframe 

    """
    # Entradas maiores que 258.0 cm viram Nan
    df['altura'] = df['altura'].apply(alt)

def peso(df):
    """
            Corrige entradas da coluna 'peso'.
            Como pesos maiores que 200.0 kg são extremamente raras,
            valores maiores que esse serao considerados um erro.
            
            Inputs:
                df: dataframe 

    """
    # Entradas maiores que 200.0 cm viram Nan
    df['peso'] = df['peso'].apply(alt)


def pressao_sistolica(df):
    """
            Corrige entradas da coluna 'pressao_sistolica'.
            Como pressoes que 250 são extremamente raras,
            valores maiores que esse serao considerados um erro.
            
            Inputs:
                df: dataframe 

    """
    # Entradas maiores que 250.0 cm viram Nan
    df['pressao_sistolica'] = df['pressao_sistolica'].apply(press)


def pressao_diastolica(df):
    """
            Corrige entradas da coluna 'pressao_diastolica'.
            Como pressoes que 200 são extremamente raras,
            valores maiores que esse serao considerados um erro.
            
            Inputs:
                df: dataframe 

    """
    # Entradas maiores que 200.0 cm viram Nan
    df['pressao_diastolica'] = df['pressao_diastolica'].apply(peso)


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

