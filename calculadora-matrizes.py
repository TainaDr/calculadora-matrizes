import numpy as np

def ler_matriz(nome):
    print(f"Vamos criar a matriz {nome}.")
    linhas = int(input(f"Digite o número de linhas da matriz {nome}: "))
    colunas = int(input(f"Digite o número de colunas da matriz {nome}: "))
    matriz = []
    print(f"Digite os elementos da matriz {nome}. Fale ou digite cada linha com {colunas} números separados por espaço.")
    for i in range(linhas):
        linha = list(map(float, input(f"Digite agora a linha número {i+1}: ").split()))
        while len(linha) != colunas:
            print(f"A linha deve ter exatamente {colunas} valores. Tente novamente.")
            linha = list(map(float, input(f"Digite novamente a linha número {i+1}: ").split()))
        matriz.append(linha)
    print(f"Matriz {nome} registrada.")
    return np.array(matriz)

def menu():
    print("\nEscolha uma operação digitando o número correspondente.")
    print("1 - Soma das matrizes.")
    print("2 - Subtração das matrizes.")
    print("3 - Multiplicação das matrizes.")
    print("4 - Divisão das matrizes.")
    print("5 - Transposta das matrizes.")
    print("0 - Sair do programa.")
    return input("Digite sua escolha: ")

A = ler_matriz("A")
B = ler_matriz("B")

while True:
    opcao = menu()
    if opcao == "1" and A.shape == B.shape:
        print("Resultado da soma:")
        print(A + B)
    elif opcao == "2" and A.shape == B.shape:
        print("Resultado da subtração:")
        print(A - B)
    elif opcao == "3" and A.shape[1] == B.shape[0]:
        print("Resultado da multiplicação:")
        print(np.dot(A, B))
    elif opcao == "4" and A.shape == B.shape:
        with np.errstate(divide='ignore', invalid='ignore'):
            resultado = np.divide(A, B)
            resultado[np.isnan(resultado)] = 0
        print("Resultado da divisão elemento a elemento:")
        print(resultado)
    elif opcao == "5":
        print("Transposta da matriz A:")
        print(A.T)
        print("Transposta da matriz B:")
        print(B.T)
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Operação inválida ou dimensões incompatíveis. Tente novamente.")
