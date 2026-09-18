import pandas as pd
import calendar as cc
from aa import converter



def CalcMes(mes,valores):
    diasValidos = 0


    for i in range(len(mes)):
        texto = mes[i]
        estacao = valores[i]
        partes = texto.replace(";", "").split("_")

        dias = cc.monthrange(int(partes[1]), int(partes[0]))

        diasValidos = ((int(estacao) / 100) * dias[1])+diasValidos

    print(f"Estação:º {valores.name}")
    print(f"Dias Validos:º {diasValidos}")
    diasTotais = converter(mes[0], mes[len(mes)-1])
    print(f"Dias Totais:º {diasTotais} \n\n Porcentagem%:º {int(diasValidos) / diasTotais * 100}")
    print("==========º")
    
    
df = pd.read_csv('consistencia editada.csv',sep=';')
mes =df['MONTH_YEAR / STATION']
valores = df['1043001.00']
colunas = df.columns


for i in range(1,len(colunas)):
    CalcMes(mes,df[colunas[i]])

#CalcMes(mes, valores)