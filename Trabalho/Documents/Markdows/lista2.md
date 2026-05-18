UFMS - Universidade Federal de Mato Grosso do Sul
# Métodos Numéricos

# 2a Lista de Exercícios

# Sistemas Lineares

1. Resolver o seguinte sistema pelo método da Eliminação de Gauss com pivoteamento parcial:
x1 + 2x2 + x3 = 3
2,11x1 − 4,21x2 + 0,921x3 = 2,01
2x1 + x2 − x3 = 0
4,01x1 + 10,2x2 − 1,12x3 = −3,09
3x1 − 2x2 − x3 = −2
1,09x1 + 0,987x2 + 0,832x3 = 4,21
2. Encontre a decomposição LU da matriz:
| 1 | 6 | 4 |
| - | - | - |
| 0 | 4 | 1 |
3. Utilize as decomposições A = LU da questão 2 para resolver o seguinte sistema linear:
| 2 | 1 | 0 | x1 | b1 |
| - | - | - | -- | -- |
| 1 | 6 | 4 | x2 | b2 |
| 0 | 4 | 1 | x3 | b3 |

para b = (3, 11, 15)t e b = (1, 1, 1)t.
4. Calcule a inversa da matriz da questão 2 com o auxílio da decomposição LU.
5. Seja um sistema matricial AX = B, em que A ∈ Rn×n, X ∈ Rn×p e B ∈ Rn×p.
1. Verifique que tal sistema pode ser resolvido pela solução de p sistemas auxiliares Axk = bk, em que bk ∈ Rn é a k−ésima coluna de B.
2. Qual seria a vantagem de utilizar a fatoração A = LU para a resolução deste sistema?
3. Caso p = n e B = I, qual é a matriz X?
6. O processo de fatoração LU com pivoteamento parcial de uma matriz A resultou nas matrizes seguintes:
| 1 | 0 | 0 |
| ---- | ---- | - |
| −0,2 | 1 | 0 |
| 0,8 | −0,8 | 1 |

| −5 | −5 | 1 |
| -- | -- | ---- |
| 0 | −6 | −3,8 |
| 0 | 0 | 7 |

| 1 | 0 | 0 |
| - | - | - |
| 0 | 1 | 0 |
| 0 | 0 | 1 |

1. Qual é a matriz A?
2. Utilize L, U e P para resolver Ax = b onde b = [41, 8, 6, 10]t.
7. Resolva o seguinte sistema linear utilizando a fatoração LU com estratégia de pivoteamento parcial:
x1 − 3x2 + 2x3 = 11
−2x1 + 8x2 − x3 = −15
4x1 − 6x2 + 5x3 = 29
8. Determine a fatoração de Cholesky da matriz do sistema simétrico:
| 8 | 20 | 15 |
| -- | -- | -- |
| 20 | 80 | 50 |
| 15 | 50 | 60 |

| x1 | 50 |
| -- | --- |
| x2 | 250 |
| x3 | 100 |

1

# 9.

Seja o sistema linear

| 1 | 3 | −1 | x1 | −2 | |
| - | - | -- | -- | -- | - |
| 5 | 2 | 2 | x2 | = | 3 |
| 0 | 6 | 8 | x3 | −6 | |

(a) É possível dizer se o Método de Jacobi é convergente para esse sistema, usando o critério das linhas?

(b) Mostre que a aplicação do Método de Jacobi sobre o sistema equivalente obtido pela permutação das duas primeiras equações, gera uma sequência convergente. Realize três iterações do Método de Jacobi com x0 = (0, 6 − 0, 7 − 0, 75)t calculando o erro relativo em cada iteração.

# 10.

Considere o sistema linear Ax = b em que:

| 1 | 1 | 4 | 1 |
| - | - | -- | - |
| 0 | 1 | 2 | 4 |
| 2 | 4 | −1 | 0 |
| 5 | 1 | 1 | 1 |

A =

2

b =

9

(a) Monte o esquema iterativo para o método de Gauss-Jacobi de modo que a convergência do processo seja garantida. Justifique.

(b) Realize duas iterações do método de Gauss-Jacobi a partir de x(0) = [0 0 0]t.

(c) Repita os itens (a) e (b) utilizando o Método de Gauss-Seidel.

# 11.

Seja o sistema linear

| k | 3 | 1 | x1 | 1 | |
| - | - | - | -- | - | - |
| k | 7 | 1 | x2 | = | 2 |
| 1 | 6 | 8 | x3 | 3 | |

(a) Usando o critério de linhas, verifique quais os valores positivos de k que garantem a convergência do Método de Gauss-Seidel.

(b) Repita o exercício utilizando o critério de Sassenfeld.

(c) Escolha o menor número inteiro, positivo, para k e realize duas iterações do método de Seidel.

# 12.

Um engenheiro supervisiona a produção de quatro tipos de computadores. Existem quatro espécies de recursos necessários à produção: mão-de-obra, metais, plásticos e componentes eletrônicos. As quantidades destes recursos, necessários para produzir cada computador são:

| Computador | Mão de obra (h/comp.) | Metais (kg/comp.) | Plásticos (kg/comp) | Componentes (unid./comp.) |
| ---------- | --------------------- | ----------------- | ------------------- | ------------------------- |
| 1 | 3 | 20 | 10 | 10 |
| 2 | 4 | 25 | 15 | 8 |
| 3 | 7 | 40 | 20 | 10 |
| 4 | 20 | 50 | 22 | 15 |

Considere um consumo diário de 504h de mão-de-obra, 1970kg de metais, 970 de plásticos e 601 componentes.

(a) Use um método direto com pivoteamento parcial para calcular o número de computadores (número inteiro) de cada tipo produzidos por dia.

(b) Use o método iterativo de Gauss-Seidel, tomando como aproximação inicial x(0) = [9 10 12 10]t. Apresente apenas os cálculos relativos às duas primeiras iterações, indicando o erro relativo de cada iteração.

(c) Comente os resultados obtidos nos itens (a) e (b), analisando os critérios de convergência.

# Respostas

1. (a) x = 0, 25 0, 75 1, 25 T

(b) x = −0, 4278 0, 4268 5, 1142 T
2. L = 0, 5 1 0 e U = 0 5, 5 4.

0 0, 7273 1 0 0 −1, 9092
3. x = [−0, 9046 4, 8092 − 4, 2377]t; x = [0, 3334 0, 3333 − 0, 3333]t;

0, 4762 0, 0476 −0, 1905
4. A−1 = 0, 0476 −0, 0952 0, 3809.

−0, 1905 0, 3809 −0, 5238
5.
6.
7. x1 = 2, x2 = −1 e x3 = 3
8.
9. (a) Não, pois o critério das linhas não é satisfeito, α > 1.

(b) x(³) = [1, 019 − 1, 0164 0, 1013]t

ER = 0, 1164
10. (a)

(b) x(2) = −0, 65 0, 625 −0, 1875 1, 875 T

(c) x(2) = −0, 5625 0, 875 −0, 0625 2, 0625 T
11. (a) 4 < k < 6; (b) k > 4; (c) x(2) = 0, 0657 0, 2041 0, 2137 T