# bibliotecas
import pandas as pd
import numpy as np
import funcoes as f
import matplotlib.pyplot as plt

# parte 1
df = pd.read_csv('Pokemon.csv')
'''
print('PARTE 01')
f.linha()
print(df.head()) # mostra os 5 primeiros
f.linha()
print(df.shape) # (linhas, colunas)
f.linha()
print(df.dtypes) # tipos dos arquivos da coluna
f.linha()
print(df.info()) # resumo
f.linha()
print(df.describe()) # descrição numerica
f.linha()'''

# parte 2

#print('PARTE 02')
#f.linha()
#print(df.isnull().sum()) # verifica valores nulos
df["Type 2"] = df["Type 2"].fillna("Tipo único") # preenche a coluna Type 2
# colunas vazias foram preenchidas com "Tipo unico", pois os pokemons que possuem essa coluna sem registro, possuem apenas um tipo
#f.linha()
#print(df.isnull().sum()) # verificar se o df foi corretamente preenchido
df = df.drop("Generation", axis=1) # remove a coluna Generation (todos sao da gen 3)
#print(df.duplicated().sum()) # verifica valores duplicados
#f.linha()
#print(df.shape)
#f.linha()
#print(df.info())
#f.linha()

'''# parte 3
# a
f.linha()
filtro1 = df[(df["Attack"] > 100) & (df["Legendary"] == False)]
f.mostrar_filtro(1, "Mostra os pokémons com ataque maior que 100 e que não são lendários", len(filtro1))
print(filtro1.head())

f.linha()
filtro2 = df[(df["Type 1"] == "Fire") | (df["Speed"] > 120)]
f.mostrar_filtro(2, "Mostra os pokémons do tipo fogo ou com speed maior que 120", len (filtro2))
print(filtro2.head())

f.linha()
filtro3 = df[(df["Type 1"] != "Water") & (df["Type 2"] == "Tipo único")]
f.mostrar_filtro(3, "Mostrar os pokémons que não são do tipo água e possuem apenas um tipo ", len(filtro3))
print(filtro3.head())

# b
f.linha()
maiores = df.sort_values("Total", ascending=False) # maiores valores de status total
print('Pokemons com maiores status TOTAL')
print(maiores.head(10))
f.linha()
menores = df.sort_values("Total") # menores valores de status total
print('Pokemons com menores status TOTAL')
print(menores.head(10))
f.linha()

# c
print(f'Média de ataque por tipo primário \n{df.groupby("Type 1")["Attack"].mean()}') # media de atk por tipo
f.linha()
print(f'Valor máximo de defesa por tipo primário \n{df.groupby("Type 1")["Defense"].max()}') # maximo defesa por 

# d
f.linha()
desvio = np.std(df["Attack"])
print(f'Desvio padrão da coluna ATTACK: {desvio:.2f}')
matriz_correlacao = np.corrcoef(df["Attack"], df["Sp. Atk"])
print(f'Matriz de correlação entre a matriz ATTACK E SP.ATTACK:\n{matriz_correlacao}')
f.linha()
df["Attack/Sp. Atk"] = df["Attack"] / df["Sp. Atk"]
#print(df.head())
f.linha()'''

# 4
# Grafico 1 - Dispersao - Combinações de tipos
plt.scatter(df["HP"], df["Defense"])

# Adicionando títulos e rótulos
plt.title("Relação entre HP e Defesa")
plt.xlabel("HP")
plt.ylabel("Defesa")

# Exibindo o gráfico
plt.show()

# Grafico 2 - Pizza
'''lendarios = df[df["Legendary"] == True]
quantidade_tipos = lendarios["Type 1"].value_counts()
plt.figure(figsize=(10,7))
plt.pie(quantidade_tipos, labels=quantidade_tipos.index, autopct='%1.1f%%')

plt.title("Tipagens primárias dos pokémons lendários")
plt.axis('equal')
plt.show()'''

# Grafico 3 - Linha
'''quantidade_tipos = df["Type 1"].value_counts()
plt.plot(quantidade_tipos.index, df.groupby("Type 1")["Attack"].mean(), marker='s', color='blue', label='Ataque')
plt.plot(quantidade_tipos.index, df.groupby("Type 1")["Defense"].mean(), marker='s', color='red', label='Defesa')

plt.title("Média de Ataque e Defesa por tipo primário")
plt.xlabel("Tipo")
plt.ylabel("Média de ataque")
plt.legend()
plt.show()'''

# Grafico 4