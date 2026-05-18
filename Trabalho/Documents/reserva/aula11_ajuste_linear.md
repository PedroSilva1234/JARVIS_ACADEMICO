
# Ajuste de Curvas pelo Método de Quadrados Mínimos

# Lilian Berti

# Métodos Numéricos

Lilian Berti  Ajuste de Curvas pelo Método de Quadrados Mínimos



# Ajuste de Curvas

Objetivo: Aproximar uma função f(x) por outra função g(x) ou dado um conjunto de pontos encontrar uma função que melhor os ajusta.

# Exemplo:

A tabela abaixo fornece o número de habitantes de um determinado país (em milhões):

| ano(t)          | 2000 | 2005 | 2012  | 2015  | 2019  |
| --------------- | ---- | ---- | ----- | ----- | ----- |
| habitantes p(t) | 70,2 | 93,1 | 119,0 | 146,2 | 169,8 |

Qual o número de habitantes em 2021?

Lilian Berti  Ajuste de Curvas pelo Método de Quadrados Mínimos




# Caso discreto

Dada a tabela:

|   | x1 | x2 | · · · | xn−1 | xn |
| - | -- | -- | ----- | ---- | -- |
|   | y1 | y2 | · · · | yn−1 | yn |

com x1, x2, · · · , xn ∈ [a, b]. O problema de ajuste de curva consiste em escolhidas m funções g1(x), g2(x), · · · , gm(x), com m &#x3C; n contínuas em [a, b], obter m constantes α1, α2, · · · , αm tais que a função:

g(x) = α1g1(x) + α2g2(x) + · · · + αmgm(x)

melhor se ajusta aos pontos.

Lilian Berti Ajuste de Curvas pelo Método de Quadrados Mínimos





# Exemplos

# 1 Aproximação por uma reta

g1(x) = 1 e g2(x) = x

# 2 Aproximação por uma parábola

g1(x) = 1, g2(x) = x e g3(x) = x2

# 3 Aproximação por

g1(x) = 1/x e g2(x) = x2.

Lilian Berti  Ajuste de Curvas pelo Método de Quadrados Mínimos



# Método dos Quadrados Mínimos

Determina αj para j = 1, 2, · · · , m de forma a minimizar os resíduos, ou seja

| minimiza |   |                 |
| :------: | - | --------------- |
|     n    | = | n               |
|  ∑ (ri)² | = | ∑ (yi − g(xi))² |
|    i=1   |   | i=1             |

<svg height="100" width="300">
<line x1="0" y1="50" x2="300" y2="50" style="stroke: black;"></line>
<line x1="50" y1="0" x2="50" y2="100" style="stroke: black;"></line>
<text x="10" y="55">5</text>
<text x="10" y="45">4</text>
<text x="10" y="35">3</text>
<text x="10" y="25">2</text>
<text x="10" y="15">1</text>
<text x="10" y="5">0</text>
<text x="150" y="70">0</text>
<text x="200" y="70">1</text>
<text x="250" y="70">2</text>
<text x="300" y="70">3</text>
<text x="350" y="70">4</text>
<text x="400" y="70">5</text>
</svg>

Lilian Berti Ajuste de Curvas pelo Método de Quadrados Mínimos




# Ajuste de Curvas pelo Método de Quadrados Mínimos

Considere

F(α1, α2, · · · , αn) =    (yi − g(xi))² =




Por simplicidade, tomando m = 2, obtemos:

n
[yi − α₁g₁(xi) − α₂g₂(xi)] · (−g (x )) = 0 para j = 1, 2
j
i=1

Obtemos:

| n                                            | g1(xi)g1(xi) α1 + g1(xi)g2(xi) α2 = yig1(xi) | i=1 |
| -------------------------------------------- | -------------------------------------------- | --- |
| g2(xi)g1(xi) α1 + g2(xi)g2(xi) α2 = yig2(xi) | i=1                                          |     |

um sistema de m equa¸c˜oes e m vari´aveis, denominado sistema de

equa¸c˜oes normais.

Lilian Berti  Ajuste de Curvas pelo M´etodo de Quadrados M´ınimos





# Lembrando: Produto escalar

Dados x, y ∈ Rn,





Utilizando a notação de produto escalar, podemos reescrever:

n  n

g (x )g (x ) =&#x3C; g  (  )

¯  , g

¯  >  y g  x =&#x3C; y

¯, g

k i  j  i  k j  k j  i  ¯j >

i=1  i=1

em que g  [  (   )  (  )  · · ·  (  )]ᵀ

¯k = gk x1  gk x2  gk xn  e

y  [  · · ·  ]ᵀ  · · ·  · · ·

¯ = y1  y2  yn  , para k = 1, 2,  , m e j = 1, 2,  , m.

Podemos reescrever o sistema como:

&#x3C; g

¯ , g

¯  > α  +  &#x3C; g

¯ , g

¯  > α  =  &#x3C; y

¯, g

1  1  1  1   2  2  ¯1 >

&#x3C; g

¯ , g

¯  > α  +  &#x3C; g

¯ , g

¯  > α  =  &#x3C; y

¯, g

2  1  1  2   2  2  ¯2 > .

Caso o determinante da matriz de coeficientes é diferente de zero,

o sistema admite única solução, sendo α1, α2 que minimiza F.

Lilian Berti  Ajuste de Curvas pelo Método de Quadrados Mínimos






# Exemplo

Ajustar os dados da tabela por uma reta

| x | 0 | 0,25  | 0,5    | 0,75  | 1      |
| - | - | ----- | ------ | ----- | ------ |
| y | 1 | 1,284 | 1,6487 | 2,117 | 2,7183 |

3.0

2.5

2.0

> 1.5

1.0

0.5

0.0-

0.00  0.25  0.50  0.75  1.00  1.25  1.50

-0.50   -0.25

X

Lilian Berti  Ajuste de Curvas pelo M´etodo de Quadrados M´ınimos






Para ajustar com uma reta, tomamos

g(x) = α1g1(x) + α2g2(x),

em que g1(x) = 1 e g2(x) = x.

Determinamos a melhor reta que se ajusta aos dados, ou seja, encontramos os valores de α1 e α2, resolvendo o seguinte sistema:

| ¯, g1 ¯ | α1 | + | ¯, g2 ¯ | α2 | = | ¯, g1 ¯ |
| ------- | -- | - | ------- | -- | - | ------- |
| ¯, g2 ¯ | α1 | + | ¯, g2 ¯ | α2 | = | ¯, g2 ¯ |

em que

| g1 | 1 | 1     | 1      | 1     |        |
| -- | - | ----- | ------ | ----- | ------ |
| g2 | 0 | 0,25  | 0,5    | 0,75  | 1      |
| y  | 1 | 1,284 | 1,6487 | 2,117 | 2,7183 |

Lilian Berti  Ajuste de Curvas pelo Método de Quadrados Mínimos






Logo,

# 5α1 + 2, 5α2 = 8, 768

# 2, 5α1 + 1, 875α2 = 5, 4514

Fazendo, L2 ← L2 − 0, 5L1, temos:

# 5α1 + 2, 5α2 = 8, 768

# 0, 625α2 = 1, 0674

Assim: α1 = 0, 8997 e α2 = 1, 7078.

Portanto, a reta que melhor se ajusta aos dados é:

# g(x) = 0, 8997 + 1, 7078x

Lilian Berti Ajuste de Curvas pelo Método de Quadrados Mínimos



# Tabela de Resíduos

| x    | 0      | 0,25    | 0,5     | 0,75    | 1      |        |
| ---- | ------ | ------- | ------- | ------- | ------ | ------ |
| y    |        | 1       | 1,284   | 1,6487  | 2,117  | 2,7183 |
| g(x) | 0,8997 | 1,3267  | 1,7536  | 2,1806  | 2,6075 |        |
| r(x) | 0,1003 | -0,0427 | -0,1049 | -0,0636 | 0,1108 |        |

n (ri)² = 0, 0392.

i=1

# Lilian Berti

# Ajuste de Curvas pelo Método de Quadrados Mínimos




# Lilian Berti  Ajuste de Curvas pelo M´etodo de Quadrados M´ınimos

| 3.0   | 2.5   | 2.0  | -    | 1.5  | 1.0      | 0.5 |
| ----- | ----- | ---- | ---- | ---- | -------- | --- |
| y     | 0.0   | 0.50 | 0.75 | 1.00 | 1.25g(x) |     |
| -0.50 | -0.25 | 0.00 | 0.25 | 1.50 | x        |     |





# Observação:

No caso, g1(x) = 1 e g2(x) = x, com n pontos tabelados, podemos escrever o sistema linear como:

| n | α1          | + | Σi=1n xi α2    | = | Σi=1n yi   |
| - | ----------- | - | -------------- | - | ---------- |
| n | Σi=1n xi α1 | + | Σi=1n (xi)² α2 | = | Σi=1n xiyi |

Lilian Berti  Ajuste de Curvas pelo Método de Quadrados Mínimos




# Exemplo:

Ajustar os dados por uma parábola

| x | -2 | -1 | 1 | 2 |
| - | -- | -- | - | - |
| y | 1  | -3 | 1 | 9 |

# Lilian Berti

Ajuste de Curvas pelo Método de Quadrados Mínimos






y ≈ α1g1(x) + α2g2(x) + α3g3(x),

em que g1(x) = 1, g2(x) = x e g3(x) = x2.

Determinando α1, α2 e α3.

|   | α1 |   | α2 |   | α3 | = | 1> |
| - | -- | - | -- | - | -- | - | -- |
|   | α1 |   | α2 |   | α3 | = | 2> |
|   | α1 |   | α2 |   | α3 | = | 3> |

em que

| g1 | 1  | 1  | 1 | T |   |
| -- | -- | -- | - | - | - |
| g2 | −2 | −1 | 1 | 2 | T |
| g3 | 4  | 1  | 1 | 4 | T |

e

| ȳ | 1 | −3 | 1 | 9 | T |
| -- | - | -- | - | - | - |

Lilian Berti  Ajuste de Curvas pelo Método de Quadrados Mínimos






# Assim:

| 4α1  | + 10α3 | = 8  |
| ---- | ------ | ---- |
| 10α2 | = 20   |      |
| 10α1 | + 34α3 | = 38 |
| 4α1  | + 10α3 | = 8  |
| 10α2 | = 20   |      |
| 9α3  | = 18   |      |

Obtemos: α1 = −3, α2 = 2 e α3 = 2.

Portanto, a parábola que melhor se ajusta aos dados é:

g(x) = −3 + 2x + 2x².

Lilian Berti  Ajuste de Curvas pelo Método de Quadrados Mínimos





O consumo de gás natural sofre uma redução significativa durante os meses de verão. Na tabela estão registrados alguns valores recolhidos ao longo do ano de 2006.

| x (mês)     | 1  | 3   | 4   | 6 | 9  | 12 |
| ----------- | -- | --- | --- | - | -- | -- |
| y (consumo) | 20 | 7,5 | 6,5 | 7 | 10 | 15 |

Uma companhia de gás sugeriu um modelo do tipo

M(x) = ax2 + b1x

para estimar o consumo de gás em qualquer mês do ano. Determine os parâmetros a e b.

Lilian Berti  Ajuste de Curvas pelo Método de Quadrados Mínimos




# Ajuste de Curvas pelo Método de Quadrados Mínimos

y ≈ M(x) = ax2 + b

em que g1(x) = x2 e g2(x) = 1/x

Determinando a e b, resolvendo:

| 1, g1> | a | + | 1, g1> | b | = | 1, g1> |
| ------ | - | - | ------ | - | - | ------ |
| 1, g1> | a | + | 1, g1> | b | = | 2, g2> |

em que

| g1 | 9   | 16  | 36  | 81  | 144  |    |
| -- | --- | --- | --- | --- | ---- | -- |
| g2 | 1/3 | 1/4 | 1/6 | 1/9 | 1/12 |    |
| y  | 20  | 7,5 | 6,5 | 7   | 10   | 15 |

Lilian Berti






Logo,

28931a + 35b = 3413, 5

35a + 1, 2207b = 27, 6528

Utilizando o método de eliminação de gauss, (L₂ ← L₂ − 0, 0012L₁) obtemos:

28931a + 35b = 3413, 5

1, 1787b = 23, 5566

Assim: a = 0, 0938 e b = 19, 9631.

Portanto, M(x) = 0, 0938x2 + 19, 9631

x

Lilian Berti Ajuste de Curvas pelo Método de Quadrados Mínimos

