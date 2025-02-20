import pandas as pd
import numpy as np

from functions import religiao, renda_familiar, obito, meios_transporte, sexo_biologico, doencas_condicoes, identidade_genero
from functions import ids_repetidas, luz_eletrica, em_situacao_de_rua, meios_comunicacao, possui_plano_saude, vulnerabilidade_social
from functions import fam_aux_bra, cria_matr_cre, data_at_cad, data_nasc, data_cad, updated_at, em_caso_doenca_procura
from functions import raca_cor, altura, peso, pressao_sistolica, pressao_diastolica, situ_prof

def model(dbt, session):
    
    # Configuração do modelo
    dbt.config(materialized="table")

    csv_path = "~\desafio\dados_ficha_a_desafio.csv"  

    # Ler arquivo csv
    df = pd.read_csv(csv_path)

    ## Transformacoes na tabela
    # item 0
    sexo_biologico(df)

    # item 1
    ids_repetidas(df)

    # item 2
    obito(df)

    # item 3
    religiao(df, 'religiao')

    # item 4
    luz_eletrica(df)

    # item 5
    em_situacao_de_rua(df)

    # item 6
    meios_transporte(df)

    # item 7
    doencas_condicoes(df)

    # item 8
    identidade_genero(df)

    # item 9
    meios_comunicacao(df)

    # item 10
    possui_plano_saude(df)

    # item 11
    em_caso_doenca_procura(df)

    # item 12
    vulnerabilidade_social(df)

    # item 13
    fam_aux_bra(df)
    
    # item 14
    cria_matr_cre(df)

    # item 15
    raca_cor(df)

    # item 16
    data_at_cad(df)

    # item 17
    data_cad(df)

    # item 18
    data_nasc(df)

    # item 19
    updated_at(df)

    # item 20
    altura(df)

    # item 21
    peso(df)

    # item 22
    pressao_diastolica(df)

    # item 23
    pressao_sistolica(df)

    # item 24
    renda_familiar(df)
    
    # item 25
    situ_prof(df)

    return session.create_dataframe
