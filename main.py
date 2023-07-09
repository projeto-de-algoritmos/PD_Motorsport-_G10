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


# Exemplo de utilização
peças = ["Pneu", "Motor", "Chassi"]
valor = [100, 300, 200]
peso = [2, 5, 10]
capacidade_maxima = 20
valor_maximo = 2000

valor_total, peças_selecionadas = mochila(valor, peso, capacidade_maxima, valor_maximo)

print("Valor total da mochila:", valor_total)
print("Peças selecionadas:")
for peça in peças_selecionadas:
    print(peças[peça])
