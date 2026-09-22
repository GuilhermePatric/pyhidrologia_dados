import pandas as pd


def converter(inicio, fim):
    inicio = pd.to_datetime(inicio, format='%m_%Y')
    fim = pd.to_datetime(fim, format='%m_%Y')
    return (fim - inicio).days
