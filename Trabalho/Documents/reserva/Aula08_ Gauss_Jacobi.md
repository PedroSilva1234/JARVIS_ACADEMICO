
# Resolução de sistemas lineares - Método de Gauss - Jacobi

# Lilian Berti

# Métodos Numéricos

# Resolução de sistemas lineares - Método de Gauss - Jacobi

# Lilian Berti




# Resolução de sistemas lineares - Método de Gauss - Jacobi

O sistema linear Ax = b em que A : n × n e b : n × 1 é transformado em um sistema equivalente da forma

x = Bx + c

em que B : n × n e c : n × 1. Assim, partindo de uma aproximação inicial x(0) a sequência x(1), x(2), . . . é gerada por:

x(k+1) = Bx(k) + c,      k = 0, 1, 2, . . .

em que B é denominada matriz de iteração e o processo de iteração poderá convergir ou não dependendo das equações envolvidas.

Lilian Berti






# Norma: mede o tamanho dos vetores.

Seja x = [x1, x2, . . . , xn]T.

# Norma euclidianda:

x2 = x12 + x22 + · · · + xn2

# Norma 1:

x1 = |x1| + |x2| + |xn|

# Norma Infinito:

x∞ = max{|x1|, |x2|, . . . , |xn|}

# Exemplo:

Seja x = [5, 2, −1]T. Temos:

- x2 = 52 + 22 + (−1)2 = √30
- x1 = |5| + |2| + |−1| = 8
- x∞ = max{|5|, |2|, |−1|} = 5

Lilian Berti  Resolução de sistemas lineares - Método de Gauss - Jacobi





# Critério de Parada

EA = x(k) − x(k−1) ∞ = max {|x(k) − x(k−1)|}

1≤i≤n  i    i

max {|x(k) − x(k−1)|}

ER =   x(k)−x(k−1) ∞ = 1≤i≤n  i  (  i

x(k) ∞       max {|xi k)|}

1≤i≤n

Dada uma precisão o vetor x(k) será considerado solução, isto é,

x      (k)

¯ = x     se EA &#x3C;   ou ER &#x3C;

Lilian Berti  Resolução de sistemas lineares - Método de Gauss - Jacobi



# Método de Gauss- Jacobi

Considere o sistema linear

| a11x1 | + | a12x2 | + | a13x3 | = | b1 |
| ----- | - | ----- | - | ----- | - | -- |
| a21x1 | + | a22x2 | + | a23x3 | = | b2 |
| a31x1 | + | a32x2 | + | a33x3 | = | b3 |

Seja A = L + D + U em que

| 0   | 0   | 0 | a11 | 0   | 0   | 0 | a12 | a13 |
| --- | --- | - | --- | --- | --- | - | --- | --- |
| a21 | 0   | 0 | 0   | a22 | 0   | U | 0   | a23 |
| a31 | a32 | 0 | 0   | 0   | a33 | 0 | 0   | 0   |

Supondo aii = 0

Ax = b

(L + D + U)x = b

Dx = −(L + U)x + b

x(k+1) = −D−1(L + U)x(k) + D−1b

B

c

Lilian Berti

Resolução de sistemas lineares - Método de Gauss - Jacobi




# 1

| a₁₁ | 0     | 0     | a₁₂ | a₁₃ |
| --- | ----- | ----- | --- | --- |
| 0   | 1/a₂₂ | a₂₁   | 0   | a₂₃ |
| 0   | 0     | 1/a₃₃ | a₃₁ | a₃₂ |

Ent˜ao, podemos escrever o sistema de itera¸c˜ao como:

x(k+1) = 1 (b₁ − a₁₂x(ᵏ) − a₁₃x(ᵏ))

1 a₁₁ 2 3

x(k+1) = 1 (b₂ − a₂₁x(ᵏ) − a₂₃x(ᵏ))

2 a₂₂ 1 3

x(k+1) = 1 (b₃ − a₃₁x(ᵏ) − a₃₂x(ᵏ))

3 a₃₃ 1 2

Lilian Berti Resolu¸c˜ao de sistemas lineares - M´etodo de Gauss - Jacobi





Em resumo:

Dado uma aproximação inicial x(0) o método de Gauss - Jacobi consiste em obter x(1), x(2), . . . , x(k), x(k+1), . . . através

| x(k+1) =            | n    |           |   |   |
| ------------------- | ---- | --------- | - | - |
|                     | bi − | ∑ aijx(k) |   |   |
| j=1,i=j             |      |           |   |   |
| i = 1, 2, . . . , n |      |           |   |   |

até que o critério de parada seja satisfeito.

Na falta de informação de uma aproximação inicial pode-se tomar x(0) como sendo o vetor nulo.

Lilian Berti Resolução de sistemas lineares - Método de Gauss - Jacobi



# Exemplo: Resolva o sistema linear pelo método de Gauss - Jacobi

utilizando como aproximação inicial o vetor [1, 1; 0, 8; 0, 9]T e critério de parada ER &#x3C; 0, 05

8x1 + x2 − x3 = 8
x1 − 7x2 + 2x3 = −4
2x1 + x2 + 9x3 = 12

# Esquema iterativo:

| x(k+1) |   |   | = | 1  | (8 − x(k) + x(k))   | 8 | 2 | 3 |   |
| ------ | - | - | - | -- | ------------------- | - | - | - | - |
| x(k+1) |   |   | = | −1 | (−4 − x(k) − 2x(k)) | 2 | 7 | 1 | 3 |
| x(k+1) |   |   | = | 1  | (12 − 2x(k) − x(k)) | 3 | 9 | 1 | 2 |

Lilian Berti

Resolução de sistemas lineares - Método de Gauss - Jacobi




# Resolução de sistemas lineares - Método de Gauss - Jacobi

x(k+1) = 1 (8 − x(k) + x(k))

1 8 2 3

x(k+1) = − 1 (−4 − x(k) − 2x(k))

2 7 1 3

x(k+1) = 1 (12 − 2x(k) − x(k))

3 9 1 2

# Para k = 0

x(1) = [1, 0125 ; 0, 9857 ; 1]T

ER = x(1)−x(0) ∞ = max{0,0875;0,1857;0,1} = 0,1857 = 0, 1834 > 0, 05

x(1) ∞ max{1,0125;0,9857;1} 1,0125

# Para k = 1

x(2) = [1, 0018 ; 1, 0018 ; 0, 9988]T

ER = x(2)−x(1) ∞ = max{0,0107;0,0161;0,0012} = 0,0161 = 0, 0161 &#x3C; 0, 05

x(2) ∞ max{1,0018;1,0018;0,9988} 1,0018

Portanto, x (2) [1 9988]ᵀ

¯ = x = , 0018 ; 1, 0018 ; 0,





# Convergência: (Critério das linhas)

Seja o sistema linear Ax = b em que A : n × n e seja

n
αi = ∑j=1, i=j aij / aii i = 1, 2, . . . , n.

Se α = max αi &#x3C; 1, então o método de Gauss - Jacobi gera uma sequência convergente para a solução do sistema independente da aproximação inicial x(0).

Observação: Verificar se critério das linhas é satisfeito é equivalente a verificar se a matriz é estritamente diagonal dominante.

n
∑j=1, i=j aij &#x3C; aii i = 1, 2, . . . , n

Lilian Berti  Resolução de sistemas lineares - Método de Gauss - Jacobi




# Exemplo:

Verifique se a matriz do exemplo anterior satisfaz o critério das linhas.

| 8 | 1  | −1 |
| - | -- | -- |
| 1 | −7 | 2  |
| 2 | 1  | 9  |

Temos:

α1 = |1|+|−1| = 2 = 0, 25

|8| 8

α2 = |1|+|2| = 3 = 0, 43

|−7| 7

α3 = |2||+|1| = 3 = 0, 33

9| 9

Como α = max{α1, α2, α3} = 0, 43 &#x3C; 1, segue que o critério das linhas é satisfeito. Portanto, podemos afirmar que o método de Gauss-Jacobi irá convergir para a solução.

Lilian Berti  Resolução de sistemas lineares - Método de Gauss - Jacobi






# Exemplo: Seja:

2x1 − 6x2 − x3 = −38
−3x1 − x2 + 7x3 = −34
−8x1 + x2 − 2x3 = −20

# a)

Verifique se o critério das linhas é satisfeito. Temos:

α1 = −6 + −1 = 7 = 3, 5
2

α2 = −3 + 7 = 10
−1

α3 = −8 + 1 = 9 = 4, 5
−2      2

Como α = max{α1, α2, α3} = 10 > 1, segue que o critério das linhas não é satisfeito. Logo, não podemos afirmar que o método de Gauss-Jacobi irá convergir para a solução.

Lilian Berti  Resolução de sistemas lineares - Método de Gauss - Jacobi






b) Realize duas iterações do método de Gauss-Jacobi usando x(0) = [2; 6; 1]T. Sabendo que x∗ = [4, 8, −2]T, compare com a aproximação x(2) obtida.

# Esquema iterativo:

| x(k+1) | = | 1                      | (−38 + 6x(k) + x(k)) |   |   |   |   |   |
| ------ | - | ---------------------- | -------------------- | - | - | - | - | - |
| 1      |   | 2                      |                      | 3 |   |   |   |   |
| x(k+1) | = | −(−34 + 3x(k) − 7x(k)) |                      |   |   |   |   |   |
|        |   | 2                      |                      | 1 |   | 3 |   |   |
| x(k+1) | = | − 1                    | (−20 + 8x(k) − x(k)) |   |   |   |   |   |
|        |   | 3                      |                      | 2 |   | 1 |   | 2 |

# Para k = 0

x(1) = [−0, 5 ; 35 ; 5]T

# Para k = 1

x(2) = [88, 5 ; 70, 5 ; 29, 5]T

A sequência de aproximações está divergindo da solução exata.

Lilian Berti  Resolução de sistemas lineares - Método de Gauss - Jacobi






c) Faça permutação entre as linhas do sistema linear de modo a garantir a convergência do método.

Permutando as linhas 1 e 3.

−8x1 + x2 − 2x3 = −20
−3x1 − x2 + 7x3 = −34
2x1 − 6x2 − x3 = −38

Permutando as linhas 2 e 3.

−8x1 + x2 − 2x3 = −20
2x1 − 6x2 − x3 = −38
−3x1 − x2 + 7x3 = −34

Temos:

α1 = |1|+|−2| = 3 = 0, 375

α2 = |2|+|−1| = 3 = 0, 5

|−8|    8

α3 = |−3||+|−1| = 4 = 0, 5714

7|           7

Como α = max{α1, α2, α3} = 0, 5713 &#x3C; 1, segue que o critério das linhas é satisfeito. Logo, podemos afirmar que o método de Gauss-Jacobi irá convergir para a solução.

Lilian Berti  Resolução de sistemas lineares - Método de Gauss - Jacobi






# d) Realize duas iterações do método de Gauss-Jacobi no sistema linear permutado no item anterior usando a aproximação inicial x(0) = [2; 6; 1]T

# Esquema iterativo:

| x(k+1) | = | − 1 | (−20 − x(k) + 2x(k)) | 8 | 2 | 3 |
| ------ | - | --- | -------------------- | - | - | - |
| x(k+1) | = | − 1 | (−38 − 2x(k) + x(k)) | 6 | 1 | 3 |
| x(k+1) | = | 1   | (−34 + 3x(k) + x(k)) | 7 | 1 | 2 |

# Para k = 0

x(1) = [3 ; 6, 8333 ; −3, 1429]T

# Para k = 1

x(2) = [4, 1399 ; 7, 8572 ; −2, 5952]T

A sequência de aproximações está convergindo para a solução exata.

Lilian Berti  Resolução de sistemas lineares - Método de Gauss - Jacobi





# Resolução de sistemas lineares - Método de Gauss - Jacobi

Observação: O critério das linhas é uma condição suficiente para a convergência do método de Gauss - Jacobi. Caso, o critério não seja satisfeito não implica que o método irá divergir, nada se pode afirmar.

Lilian Berti