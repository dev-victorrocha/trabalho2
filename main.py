# bibliotecas e definições
import pandas as pd
import numpy as np
import funcoes as f
import matplotlib.pyplot as plt
cores = [
  "#6390F0",
  "#A8A77A",
  "#7AC74C",
  "#A6B91A",
  "#F95587",
  "#B7B7CE",
  "#B6A136",
  "#E2BF65",
  "#6F35FC",
  "#EE8130",
  "#96D9D6",
  "#000000",
  "#C22E28",
  "#F7D02C",
  "#735797",
  "#A33EA1"
]

# parte 1
df = pd.read_csv('Pokemon.csv')
print('PARTE 01')
f.linha()
print(df.head()) # mostra os 5 primeiros
f.linha()
print(df.shape) # (linhas, colunas)
f.linha()
print(df.dtypes) # tipos dos arquivos da coluna
f.linha()
df.info() # resumo
f.linha()
print(df.describe()) # descrição numerica
f.linha()

# parte 2
print('PARTE 02')
f.linha()
print(df.isnull().sum()) # verifica valores nulos
df["Type 2"] = df["Type 2"].fillna("Tipo único") # preenche a coluna Type 2
# colunas vazias foram preenchidas com "Tipo unico", pois os pokemons que possuem essa coluna sem registro, possuem apenas um tipo
f.linha()
print(df.isnull().sum()) # verificar se o df foi corretamente preenchido
df = df.drop("Generation", axis=1) # remove a coluna Generation (todos sao da gen 3)
print(df.duplicated().sum()) # verifica valores duplicados
f.linha()
print(df.shape)
f.linha()
df.info()
f.linha()

# parte 3
# a
print('PARTE 03')
f.linha()
filtro1 = df[(df["Attack"] > 100) & (df["Legendary"] == False)]
f.mostrar_filtro(1, "Mostra os pokémons com ataque maior que 100 e que não são lendários", filtro1)

f.linha()
filtro2 = df[(df["Type 1"] == "Fire") | (df["Speed"] > 120)]
f.mostrar_filtro(2, "Mostra os pokémons do tipo fogo ou com speed maior que 120", filtro2)

f.linha()
filtro3 = df[(df["Type 1"] != "Water") & (df["Type 2"] == "Tipo único")]
f.mostrar_filtro(3, "Mostrar os pokémons que não são do tipo água e possuem apenas um tipo ", filtro3)

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
variancia = np.var(df["Attack"])
print(f'Desvio padrão da coluna ATTACK: {desvio:.2f}. Variancia da coluna ATTACK: {variancia:.2f}')
matriz_correlacao = np.corrcoef(df["Attack"], df["Sp. Atk"])
print(f'Matriz de correlação entre a matriz ATTACK E SP.ATTACK:\n{matriz_correlacao}')
f.linha()
df["Attack/Sp. Atk"] = df["Attack"] / df["Sp. Atk"]
print(df.head())
f.linha()

# parte 4
# Grafico 1 - Dispersao - Relação entre HP e Defesa
plt.figure(figsize=(10, 6))
plt.scatter(df["HP"], df["Defense"]) # cria grafico
plt.title("Relação entre HP e Defesa", fontsize=16, pad=15)
plt.xlabel("HP", fontsize=12)
plt.ylabel("Defesa", fontsize=12)
plt.grid(True, alpha=0.7)
f.salvar_imagem_grafico('dispersão')

# Grafico 2 - Pizza - Distribuição de tipos entre lendários
lendarios = df[df["Legendary"] == True]
quantidade_tipos = lendarios["Type 1"].value_counts()
plt.figure(figsize=(10,8))
plt.pie(quantidade_tipos, labels=quantidade_tipos.index, autopct='%1.1f%%', startangle=140, colors=cores, pctdistance=0.85, explode=[0.05] * len(quantidade_tipos))
plt.title("Distribuição de tipagens entre pokémons lendários", fontsize=15, pad=20)
plt.axis('equal')
f.salvar_imagem_grafico('pizza')

# Grafico 3 - Linha - Média de ataque e defesa por tipo
medias = df.groupby("Type 1")[["Attack", "Defense"]].mean()
quantidade_tipos = df["Type 1"].value_counts()
plt.figure(figsize=(14,6))
plt.plot(medias.index, medias["Attack"], marker='s', color="#6F35FC", label='Ataque')
plt.plot(medias.index, medias["Defense"], marker='o', color="#EE8130", label='Defesa')
plt.title("Média de Ataque vs. Defesa por tipo primário", fontsize=16, pad=15)
plt.xlabel("Tipo do Pokémon")
plt.ylabel("Média")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.6)
plt.legend(frameon=True, shadow=True)
f.salvar_imagem_grafico('linha')

# Grafico 4 - Barras - Quantidade de pokemon por tipo primario
tipos = df['Type 1'].value_counts()
plt.figure(figsize=(12, 6))
plt.bar(tipos.index, tipos.values, color=cores, edgecolor='black', alpha=0.8)
plt.title("Quantidade de Pokémons por tipo primário", fontsize=16, pad=15)
plt.xlabel("Tipo do Pokémon", fontsize=12)
plt.ylabel("Quantidade total", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.7)
plt.locator_params(axis='y', nbins=20)
f.salvar_imagem_grafico('barras')