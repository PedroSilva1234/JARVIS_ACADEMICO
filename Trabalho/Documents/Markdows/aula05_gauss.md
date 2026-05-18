
# Resolução de sistemas lineares - Eliminação de Gauss

# Lilian Berti

# Métodos Numéricos

Lilian Berti Resolução de sistemas lineares - Eliminação de Gauss



# Sistema triangular inferior de ordem n

a11x1 = b1

a21x1 + a22x2 = b2

. . .

. . .

. . .

a(n−1)1x1 + a(n−1)2x2 + · · · + an−1,n−1xn−1 = bn−1

an1x1 + an2x2 + · · · + ann−1xn−1 + annxn = bn

em que aii = 0, i = 1, 2, 3, ..., n.

# Solução:

x1 =




# Resolução de sistemas lineares - Eliminação de Gauss

Portanto,

x1 = b1 / a11

xi = bi - ∑j=1i-1 aijxj / aii, i = 2, . . . , n

# Algoritmo: Resolução de sistema triangular inferior.

Dados: A (matriz triangular inferior), b

x1 = b1 / a11

Para i = 2, 3, . . . , n

soma = bi

Para j = 1, 2, . . . , i - 1

soma = soma - aijxj

fim para

xi = soma / aii

Fim para

Lilian Berti





# Sistema triangular superior de ordem n

a11x1 + a12x2 + · · · + a1nxn = b1

a22x2 + · · · + a2nxn = b2

. .

.

.

an−1n−1xn−1 + an−1nxn = bn−1

annxn = bn

em que aii = 0, i = 1, 2, 3, ..., n.

# Solução:

xn = bn

xn−1 = (bn−1 - an−1nxn) / an−1n−1

x1 = (b1 - a12x1 - · · · - a1n−1xn−1 - a1nxn) / a11

Lilian Berti - Resolução de sistemas lineares - Eliminação de Gauss




# Resolução de sistemas lineares - Eliminação de Gauss

Portanto,

xn = bn

xi = bi − aijxj / aii,  i = n − 1, . . . , 1

Algoritmo: Resolução de sistema triangular superior.

Dados: A (matriz triangular superior), b

xn = bⁿⁿ

Para iaⁿⁿ  −    −

= n      1, n   2, . . . , 1

soma = bi

Para j = i + 1, i + 2, . . . , n

soma = soma − aijxj

fim para

xi = soma

aij

Fim para

Lilian Berti





# Métodos Diretos

Determinam a solução de um sistema linear em um número finito de operações.

# Método da Eliminação de Gauss

Consiste em transformar um sistema linear em um sistema triangular superior equivalente.

# Definição

Dois sistemas lineares são equivalentes quando possuem a mesma solução.

Lilian Berti  Resolução de sistemas lineares - Eliminação de Gauss



Propriedades

A solução do sistema linear Ax = b não se altera ao aplicar uma sequência de operações do tipo:

1. Troca das equações
2. Multiplicar uma equação por uma constante não nula.
3. Soma do múltiplo de uma equação a outra.

Estas operações geram um sistema ˜  ˜ Ax = b equivalente ao sistema original Ax = b.

Lilian Berti

Resolução de sistemas lineares - Eliminação de Gauss




# Exemplo

2x1 + 3x2 − x3 = 5

4x1 + 4x2 − 3x3 = 3

2x1 − 3x2 + x3 = −1

Escrevemos a matriz A e o vetor b na forma de uma matriz aumentada

| 2 | 3  | −1 | | | 5  |
| - | -- | -- | - | -- |---|
| 4 | 4  | −3 | | | 3  |
| 2 | −3 | 1  | | | −1 |

Lilian Berti  Resolução de sistemas lineares - Eliminação de Gauss






# Etapa 1:

|          | 2 | 3  | −1 | | | 5  | |
| -------- | - | -- | -- | - | -- |---|---|
| \[A | b] | 4 | 4  | −3 | | | 3  |
|          | 2 | −3 | 1  | | | −1 | |

pivˆo: a11 = 2 multiplicadores: m21 = a21 = 2  m31 = a31 = 1

L2 ← L2 − m21L1

L3 ← L3 − m31L1

|          | 2 | 3  | −1 | | | 5  | |
| -------- | - | -- | -- | - | -- |---|---|
| \[A | b] | 0 | −2 | −1 | | | −7 |
|          | 0 | −6 | 2  | | | −6 | |

# Etapa 2:

pivˆo: a22 = 2 m32 = a32 = 3

L3 ← L3 − m32L2

|          | 2 | 3  | −1 | | | 5  | |
| -------- | - | -- | -- | - | -- |---|---|
| \[A | b] | 0 | −2 | −1 | | | −7 |
|          | 0 | 0  | 5  | | | 15 | |

Lilian Berti  Resolução de sistemas lineares - Eliminação de Gauss






# Resolução de sistemas lineares - Eliminação de Gauss

Assim,

2x1 + 3x2 − x3 = 5
− 2x2 − x3 = −7
+ 5x3 = 15

x* = 2

x3





# Exercício: Resolva o sistema linear utilizando a Eliminação de Gauss.

0,25x1 + 0,36x2 + 0,12x3 = 7
0,112x1 + 0,16x2 + 0,24x3 = 8
0,147x1 + 0,21x2 + 0,25x3 = 9

Lilian Berti Resolução de sistemas lineares - Eliminação de Gauss




# Generalizando

|        | a11 | a12   | a1n   |     | b1 |    |   | | |
| ------ | --- | ----- | ----- | --- | -- | -- | - |---|---|
| \[A|b] | a21 | a22   | · · · | a2n | |  | b2 |   |
|        | .   | .     | .     | .   | .  | |  | . | |
|        | .   | .     | .     | .   | .  | |  | . | |
| an1    | an2 | · · · | ann   | |   | bn |    |   | |

# Etapa 1 (Elimina¸c˜ao na primeira coluna)

pivˆo: a11 = 0

mi1 = aⁱ¹ ,       i = 2, 3, . . . , n

Li ← Li − mi L1

Para i = 2, 3, . . . , n

Para j = 2, 3, . . . , n

aij = aij − mi1a1j

fim para

bi = bi − mi1b1

Fim para

Lilian Berti  Resolu¸c˜ao de sistemas lineares - Elimina¸c˜ao de Gauss





# Etapa 2 (Elimina¸c˜ao na segunda coluna)

pivˆo: a22 = 0

mi2 = ai2, i = 3, 4, . . . , n

Li ← Li − mi L2

a22

Para i = 3, 4, . . . , n

Para j = 3, 4, . . . , n

aij = aij − mi2a2j

fim para

bi = bi − mi2b2

Fim para

Continuamos o processo at´e a etapa (n-1) obtendo um sistema triangular superior.

Lilian Berti  Resolu¸c˜ao de sistemas lineares - Elimina¸c˜ao de Gauss



# Algoritmo: Elimina¸c˜ao de Gauss

Dados: A, b

Para k = 1, 2, . . . , n − 1 fa¸ca

Para i = k + 1, . . . , n fa¸ca

m = aⁱᵏ

Para aᵏᵏ fa¸ca

j = k + 1, . . . , n

aij = aij − makj

Fim para

bi = bi − mbk

Fim para

Fim para

Lilian Berti  Resolu¸c˜ao de sistemas lineares - Elimina¸c˜ao de Gauss



# Algoritmo: Resolução de Ax = b pela Eliminação de Gauss

# Algoritmo: Eliminação de Gauss

# Algoritmo: Resolução de Sistema triangular superior.

Lilian Berti  Resolução de sistemas lineares - Eliminação de Gauss




Exemplo:

Seja:

| 0, 0003x1 | + 3x2 | = 2, 001 |
| --------- | ----- | -------- |
| x1        | + x2  | = 1      |

a) Resolva o sistema linear pela eliminação de Gauss, utilize 4 dígitos significativos e arredondamento.

m21 = 0, 1 = 3333 L2 ← L2 − 3333L1

| 0, 0003x1 | + 3x2    | = 2, 001 |
| --------- | -------- | -------- |
|           | − 9998x2 | = −6668  |

x1 = 1 e x2 = 0, 6669

Note: x1 + x2 = 1, 6669 = 1

Lilian Berti  Resolução de sistemas lineares - Eliminação de Gauss





b) Resolva novamente trocando as linhas

| x1        | + x2  | = 1      |
| --------- | ----- | -------- |
| 0, 0003x1 | + 3x2 | = 2, 001 |

m21 = 0,0003 = 0, 0003

1

| x1 | + x2 | = 1      |
| -- | ---- | -------- |
|    | 3x2  | = 2, 001 |

x1 = 0, 333 e x2 = 0, 667.

Lilian Berti  Resolu¸c˜ao de sistemas lineares - Elimina¸c˜ao de Gauss



Observação: A escolha do maior elemento em módulo entre os candidatos a pivô faz com que os multiplicadores em módulo estejam entre 0 e 1, o que evita a ampliação dos erros de arredondamento.

# Estratégia de pivoteamento parcial

Na etapa k, escolhemos para pivô o elemento de maior módulo entre os coeficientes:

|aₖᵣ| = max |air| ⇒ pivô akr

1≤i≤n

Troca-se as linhas k e r se necessário.

Lilian Berti  Resolução de sistemas lineares - Eliminação de Gauss




# Exemplo:

| 0, 1 7 | −0, 3 | x1    |    | −19, 3 |       |
| ------ | ----- | ----- | -- | ------ | ----- |
| 0, 3   | −0, 2 | 10    | x2 | =      | 71, 4 |
| 3      | −0, 1 | −0, 2 | x3 | 7, 85  |       |

[A | b] =

| 0, 3 | −0, 2 | 10    | | | 71, 4 |
| ---- | ----- | ----- | - | ----- |---|
| 3    | −0, 1 | −0, 2 | | | 7, 85 |

# Etapa 1:

pivˆo: a31 = 3 L1 ↔ L3

| 3 | −0, 1 | −0, 2 | | | 7, 85 |
| - | ----- | ----- | - | ----- |---|

[A | b] =

| 0 | −0, 19  | 10, 02   | | | 70, 615   |
| - | ------- | -------- | - | --------- |---|
| 0 | 7, 0033 | −0, 2933 | | | −19, 5614 |

Lilian Berti

Resolu¸c˜ao de sistemas lineares - Elimina¸c˜ao de Gauss





# Etapa 2:

pivô: a32 = 7, 0033    L2 ↔ L3

|            | 3 | −0, 1   | −0, 2    | | | 7, 85     | |
| ---------- | - | ------- | -------- | - | --------- |---|---|
| \[A | b] = | 0 | 7, 0033 | −0, 2933 | | | −19, 5614 |
|            | 0 | −0, 19  | 10, 02   | | | 70, 615   | |

L3 ← L3 + 0, 0271L2

|            | 3 | −0, 1   | −0, 2    | | | 7, 85     | |
| ---------- | - | ------- | -------- | - | --------- |---|---|
| \[A | b] = | 0 | 7, 0033 | −0, 2933 | | | −19, 5614 |
|            | 0 | 0       | 10, 0121 | | | 70, 0849  | |

Portanto,

x1 = 3, x2 = −2, 5 e x3 = 7

Lilian Berti  Resolução de sistemas lineares - Eliminação de Gauss



# Método de Gauss-Jordan

Uma variação da Eliminação de Gauss:

Ax = b      ≈      Ix = c

em que I é a matriz identidade.

Lilian Berti

# Resolução de sistemas lineares - Eliminação de Gauss




# Exemplo

| 2 | 1 | −1 | x1 | 1    |
| - | - | -- | -- | ---- |
| 5 | 2 | 2  | x2 | = −4 |
| 3 | 1 | 1  | x3 | 5    |

Temos:

| 2 | 1 | −1 | | | 1  |
| - | - | -- | - | -- |---|
| 5 | 2 | 2  | | | −4 |
| 3 | 1 | 1  | | | 5  |

L1 ← 0, 5L1

| 1 | 0, 5 | −0, 5 | | | 0, 5 |
| - | ---- | ----- | - | ---- |---|
| 5 | 2    | 2     | | | −4   |
| 3 | 1    | 1     | | | 5    |

Lilian Berti  Resolu¸c˜ao de sistemas lineares - Elimina¸c˜ao de Gauss






# Lilian Berti

# Resolução de sistemas lineares - Eliminação de Gauss

| L2 ← −5L1 | L3 ← −3L1 |       |   |       | |
| --------- | --------- | ----- | - | ----- |---|
| 1         | 0, 5      | −0, 5 | | | 0, 5  |
| 0         | −0, 5     | 4, 5  | | | −6, 5 |
| 0         | −0, 5     | 2, 5  | | | 3, 5  |

| L2 ← −2L2 |       |       |   |      | |
| --------- | ----- | ----- | - | ---- |---|
| 1         | 0, 5  | −0, 5 | | | 0, 5 |
| 0         | 1     | −9    | | | 13   |
| 0         | −0, 5 | 2, 5  | | | 3, 5 |

|   | L1 ← L1 − 0, 5L2 |    | L3 ← L3 + 0, 5L2 |    | |
| - | ---------------- | -- | ---------------- | -- |---|
| 1 | 0                | 4  | |                | −6 |
| 0 | 1                | −9 | |                | 13 |
| 0 | 0                | −2 | |                | 10 |






L3 ← −0, 5L3
1 0 4      | −6
0 1 −9     |  13
0 0 1      | −5

L1 ← L1 − 4L3 e L2 ← L2 + 9L3
1 0 0   |     14
0 1 0   | −32
0 0 1   | −5

Portanto,

x1 = 14,, x2 = −32 e x3 = −5

Lilian Berti  Resolu¸c˜ao de sistemas lineares - Elimina¸c˜ao de Gauss





# Cálculo de determinantes usando a eliminação de Gauss

Ao final do processo de eliminação de Gauss:

| a11 | a12 | · · · | a1n | | | b1 |
| --- | --- | ----- | --- | - | -- |---|
| 0   | a22 | · · · | a2n | | | b2 |
| .   | .   | .     | .   | | | .  |
| .   | .   | .     | .   | | | .  |
| 0   | 0   | · · · | ann | | | bn |

Det(A) = a11a22 · · · ann.

Quando utilizamos pivoteamento parcial:

Det(A) = a11a22 · · · ann(−1)p,

em que p indica o número de linhas permutadas.

Lilian Berti  Resolução de sistemas lineares - Eliminação de Gauss




# Lilian Berti

# Resolução de sistemas lineares - Eliminação de Gauss

| 2 | 1 | −1 |   |   |
| - | - | -- | - | - |
| 5 | 2 | 2  | = | 2 |
| 3 | 1 | 1  |   |   |

L1 ↔ L2

| 5 | 2 | 2  |   |    |
| - | - | -- | - | -- |
| 2 | 1 | −1 | = | −2 |
| 3 | 1 | 1  |   |    |

L2 ↔ L3

| 5 | 2 | 2  |   |   |
| - | - | -- | - | - |
| 3 | 1 | 1  | = | 2 |
| 2 | 1 | −1 |   |   |






# Exemplo: Resolva o sistema complexo:

| 3 + 2i | 4 | z1 | = | 2 + i |
| ------ | - | -- | - | ----- |
| −i     | 1 | z2 |   | 3     |

# Lilian Berti

# Resolução de sistemas lineares - Eliminação de Gauss

