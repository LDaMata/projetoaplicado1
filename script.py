import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Lê o arquivo CSV do mesmo diretório do script
data = pd.read_csv('agrofood_co2_emission.csv')


#-----------TABELA DE INFORMAÇÕES ESTATÍSTICAS BÁSICAS-----------#
# 1. Número de exemplares (linhas)
num_rows = data.shape[0]

# 2. Informações estatísticas básicas para cada coluna
basic_stats = data.describe(include='all').transpose()
print("Número de exemplares (linhas): ", num_rows)
print(basic_stats[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']])


#-----------VALORES NULOS E OUTLIERS-----------#
#Quantidade de valores ausentes (NAs) por coluna
na_counts = data.isnull().sum()
print("Valores null: ",na_counts)


#-----------TABELA DE EMISSÃO DE CO2 POR PAÍS-----------#
# 20 países com maior emissão de CO2
data.groupby('Area')['total_emission'].sum().sort_values(ascending=False).head(20).plot.bar()
plt.show()

# 20 países com menor emissão de CO2
df.groupby('Area')['total_emission'].sum().sort_values(ascending=True).head(20).plot.bar()


#-----------TABELA DE EMISSÃO DE CO2 POR ANO-----------#
sns.lineplot(data=data[(data['Area']=='Russian Federation')|(data['Area']=='China')],x='Year',y='total_emission',hue='Area')
plt.show()


#-----------TABELA DE TEMPERATURA POR ANO-----------#
sns.lineplot(data=data[(data['Area']=='Russian Federation')|(data['Area']=='China')],x='Year',y='Average Temperature °C',hue='Area')
plt.show()
