# Calculadora de Matrizes em Python

Este projeto é uma calculadora de matrizes interativa desenvolvida em Python, que permite ao usuário inserir duas matrizes e realizar operações matemáticas básicas, como soma, subtração, multiplicação, divisão elemento a elemento e transposta.
O programa foi estruturado para ser simples, didático e acessível para leitura em terminal (inclusive por leitores de tela).

## Funcionalidades

* Inserção manual de duas matrizes (A e B)
* Soma de matrizes (A + B)
* Subtração (A - B)
* Multiplicação de matrizes (A × B)
* Divisão elemento a elemento (A / B)
* Transposta de A e B
* Tratamento de erros de dimensão incompatível

## Acessibilidade

O código contém mensagens descritivas e claras para facilitar o uso por pessoas com deficiência visual, permitindo que leitores de tela interpretem corretamente cada etapa do processo.

## Tecnologias utilizadas

* [Python 3.x](https://www.python.org/)
* [NumPy](https://numpy.org/) (para operações matriciais)

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/TainaDr/calculadora-matrizes.git
cd calculadora-matrizes
```

### 2. Instale o NumPy

```bash
pip install numpy
```

### 3. Execute o programa

```bash
python calculadora_matrizes.py
```

---

## Exemplo de uso

```
Quantas linhas tem a matriz A? 2
Quantas colunas tem a matriz A? 2
Digite os elementos da matriz A, separados por espaço:
Linha 1: 1 2
Linha 2: 3 4

Quantas linhas tem a matriz B? 2
Quantas colunas tem a matriz B? 2
Digite os elementos da matriz B, separados por espaço:
Linha 1: 5 6
Linha 2: 7 8

 Calculadora de Matrizes 
1 - Soma (A + B)
2 - Subtração (A - B)
3 - Multiplicação (A x B)
4 - Divisão elemento a elemento (A / B)
5 - Transposta (Aᵀ e Bᵀ)
0 - Sair
Escolha uma opção: 1

Resultado da soma:
[[ 6.  8.]
 [10. 12.]]
```

## Licença

Este projeto é de uso livre para fins educacionais.
Você pode modificá-lo, distribuir e utilizar conforme necessário, citando a autoria.
