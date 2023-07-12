import tkinter as tk

def mochila(valor, peso, capacidade, valor_maximo):
    n = len(valor)
    # Inicializa uma matriz para armazenar os valores da solução ótima
    matriz = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacidade + 1):
            if peso[i - 1] > j:
                # Se o peso da peça atual for maior que a capacidade disponível,
                # copie o valor da célula acima
                matriz[i][j] = matriz[i - 1][j]
            else:
                # Caso contrário, verifique se vale a pena incluir a peça atual
                valor_incluindo = matriz[i - 1][j - peso[i - 1]] + valor[i - 1]
                valor_excluindo = matriz[i - 1][j]
                # Verifica a restrição de valor máximo
                if valor_incluindo > valor_excluindo and valor_incluindo <= valor_maximo:
                    matriz[i][j] = valor_incluindo
                else:
                    matriz[i][j] = valor_excluindo

    # Constrói a lista de peças selecionadas
    selecionadas = []
    i, j = n, capacidade
    while i > 0 and j > 0:
        if matriz[i][j] != matriz[i - 1][j]:
            selecionadas.append(i - 1)
            j -= peso[i - 1]
        i -= 1
    selecionadas.reverse()

    # Retorna o valor total e a lista de peças selecionadas
    return matriz[n][capacidade], selecionadas


def calcular_mochila():
    # Função chamada ao clicar no botão "Calcular"

    # Obtém os valores inseridos pelo usuário
    valores = [int(valor_entry.get()) for valor_entry in valor_entries]
    pesos = [int(peso_entry.get()) for peso_entry in peso_entries]
    capacidade = int(capacidade_entry.get())
    valor_maximo = int(valor_maximo_entry.get())

    # Chama o algoritmo da mochila
    valor_total, pecas_selecionadas = mochila(valores, pesos, capacidade, valor_maximo)

    # Atualiza os rótulos com os resultados
    valor_total_label.config(text="Valor total da mochila: {}".format(valor_total))
    pecas_selecionadas_label.config(text="Peças selecionadas: {}".format(pecas_selecionadas))

# Cria a janela principal
window = tk.Tk()
window.title("Algoritmo da Mochila")

# Cria os rótulos e entradas para os valores
valor_labels = []
valor_entries = []
peso_labels = []
peso_entries = []

for i in range(3):
    valor_label = tk.Label(window, text="Valor {}: ".format(i + 1))
    valor_label.grid(row=i, column=0, padx=5, pady=5)
    valor_labels.append(valor_label)

    valor_entry = tk.Entry(window, width=10)
    valor_entry.grid(row=i, column=1)
    valor_entries.append(valor_entry)

    peso_label = tk.Label(window, text="Peça {}: ".format(i))
    peso_label.grid(row=i, column=2, padx=5, pady=5)
    peso_labels.append(peso_label)

    peso_entry = tk.Entry(window, width=10)
    peso_entry.grid(row=i, column=3)
    peso_entries.append(peso_entry)

# Cria os rótulos e entradas para a capacidade e valor máximo
capacidade_label = tk.Label(window, text="Capacidade máxima:")
capacidade_label.grid(row=3, column=2, padx=5, pady=5)

capacidade_entry = tk.Entry(window, width=10)
capacidade_entry.grid(row=3, column=3)

valor_maximo_label = tk.Label(window, text="Valor máximo:")
valor_maximo_label.grid(row=3, column=0, padx=5, pady=5)

valor_maximo_entry = tk.Entry(window, width=10)
valor_maximo_entry.grid(row=3, column=1)

# Cria o botão de calcular
calcular_button = tk.Button(window, text="Calcular", command=calcular_mochila)
calcular_button.grid(row=4, column=0, columnspan=4, pady=10)

# Cria os rótulos para exibir os resultados
valor_total_label = tk.Label(window, text="Valor total da mochila: ")
valor_total_label.grid(row=5, column=0, columnspan=4)

pecas_selecionadas_label = tk.Label(window, text="Peças selecionadas: ")
pecas_selecionadas_label.grid(row=6, column=0, columnspan=4)

# Inicia o loop principal da janela
window.mainloop()
