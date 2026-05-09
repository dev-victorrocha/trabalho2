import matplotlib.pyplot as plt

def mostrar_filtro(indice, descricao, arquivo):
    print(f'Filtro {indice}: {descricao}')
    print(f'Total de resultados: {len(arquivo)}')
    print(arquivo.head())

def linha():
    print('='*150)

def salvar_imagem_grafico(nome_grafico):
    plt.tight_layout()
    plt.savefig(f'{nome_grafico}.png', dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()