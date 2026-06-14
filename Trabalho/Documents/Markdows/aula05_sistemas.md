# Resolução de sistemas lineares

# Lilian Berti

# Métodos Numéricos

# Lilian Berti

# Resolução de sistemas lineares

# Resolução de sistemas lineares

Veremos métodos diretos e iterativos para resolver um sistema de n equações lineares e n variáveis, que pode ser representado na forma algébrica:

| a11x1 | + | a12x2 | + | · · · | + | a1nxn | = | b1 |
| ----- | - | ----- | - | ----- | - | ----- | - | -- |
| a21x1 | + | a22x2 | + | · · · | + | a2nxn | = | b2 |
| . | . | . | . | . | . | . | . | . |
| . | . | . | . | . | . | . | . | . |
| . | . | . | . | . | . | . | . | . |
| an1x1 | + | an2x2 | + | ... | + | annxn | = | bn |

em que x1, · · · , xn são as incógnitas, a11, · · · , ann são constantes e b1, · · · , bn, são os termos independentes.

Lilian Berti Resolução de sistemas lineares

# Podemos reescrever o sistema linear, na forma matricial

Ax = b,

| a11 | a12 | · · · | a1n | x1 | b1 |
| --- | --- | ----- | --- | -- | -- |
| a21 | a22 | · · · | a2n | x2 | b2 |
| . | . | . | . | . | . |
| . | . | . | . | . | . |
| . | . | . | . | . | . |
| an1 | an2 | · · · | ann | xn | bn |

Lilian Berti Resolução de sistemas lineares

# Exemplo

Um fabricante de moveis produz cadeiras, mesinhas de centro e mesas de jantar.

1. Cada cadeira leva 10 minutos para ser lixada, 6 minutos para ser tingida e 12 minutos para ser envernizada.
2. Cada mesinha de centro leva 12 minutos para ser lixada, 8 minutos para ser tingida e 12 minutos para ser envernizada.
3. Cada mesa de jantar leva 15 minutos para ser lixada, 12 minutos para ser tingida e 18 minutos para ser envernizada.

A bancada para lixar fica disponível 16 horas por semana, a bancada para tingir, 11 horas por semana, e a bancada para envernizar, 18 horas por semana. Quantos moveis devem ser fabricados por semana de cada tipo para que as bancadas sejam plenamente utilizadas?

Lilian Berti Resolução de sistemas lineares

| Item | tempo para lixar | tempo para tingir | tempo para lustrar |
| ----------------- | ---------------- | ----------------- | ------------------ |
| cadeira | 10 | 6 | 12 |
| mesinha | 12 | 8 | 12 |
| mesa | 15 | 12 | 18 |
| horas disponíveis | 16 | 11 | 18 |

Sejam:

x1 : o número de cadeiras a ser fabricadas.

x2 : o número de mesinhas a ser fabricadas.

x3 : o número de mesas a ser fabricadas.

Tem-se que 16 h = 960 minutos; 11 h = 660 minutos e 18 h = 1080 minutos.

Podemos montar o seguinte sistema linear:

10x1 + 12x2 + 15x3 = 960

6x1 + 8x2 + 12x3 = 660

12x1 + 12x2 + 18x3 = 1080

Lilian Berti Resolução de sistemas lineares

# Resolução de sistemas lineares

Dizemos que x∗ = (x∗, x∗, · · · , x∗) é solução de um sistema linear, se for solução de todas as equações lineares, ou seja:

a11x∗ + a12x∗ + · · · + a1nx∗ = b1
a21x∗ + a22x∗ + · · · + a2nx∗ = b2
...
an1x∗ + an2x∗ + ... + annx∗ = bn

# Exemplo

Considere o seguinte sistema linear

| x1 | + | x2 | + | x3 | = | 6 |
| --- | - | -- | - | -- | - | - |
| 2x1 | + | x2 | − | x3 | = | 1 |
| 3x1 | − | x2 | + | x3 | = | 4 |

Temos:

1. (1, 2, 3) é solução do sistema linear, pois:
2. | 1 | + | 2 | + | 3 | = | 6 |
| --- | - | - | - | - | - | - |
| 2.1 | + | 2 | − | 3 | = | 1 |
| 3.1 | − | 2 | + | 3 | = | 4 |

(−5, 11, 0) não é solução do sistema linear, pois:

Lilian Berti

Resolução de sistemas lineares

# Observação: Resolução de Sistemas Lineares

Ax = b em que A é uma matriz quadrada de ordem n

Se det(A) = 0 (A é uma matriz não singular) então o sistema linear é possível e determinado, ou seja, admite única solução.

Se det(A) = 0 (A é uma matriz singular)

- sistema possível e indeterminado, ou seja, possui infinitas soluções;
- sistema impossível, não há solução

b = 0 o sistema linear é denominado homogêneo e admite a solução x = 0.

Lilian Berti Resolução de sistemas lineares

# Resolução de Sistemas Lineares

Ax = b em que A é uma matriz quadrada de ordem n

Caso o det(A) = 0, então a matriz A é inversível. Dessa forma:

Ax = b

A-1Ax = A-1b

In x = A-1b

x = A-1b

Lilian Berti

# Exemplo: Resolva o sistema linear:

2x1 + 5x2 = 12
x1 + 3x2 = 7

Temos:

| A = | 2 | 5 | e | b = | 12 |
| --- | - | - | - | --- | -- |
| | 1 | 3 | | | 7 |

det(A) = 6 − 5 = 1 = 0, logo A é inversível, sendo

| A−1 = | 3 | −5 |
| ----- | -- | -- |
| | −1 | 2 |

Então:

x* = A−1b

| = | 3 | −5 | 12 |
| - | -- | -- | -- |
| | −1 | 2 | 7 |

= 1

2

Lilian Berti Resolução de sistemas lineares

# Teorema de Cramer:

Seja um sistema linear em que o número de equações é igual ao número de incógnitas. Se D = det(A) = 0, então o sistema admite solução e ela é única, x = (x1, x2, ..., xn) tal que:

x* = Di,   i = 1, ..., n,

em que Di é o determinante da matriz obtida de A, substituindo-se a i-ésima coluna pela coluna dos termos independentes das equações do sistema.

Lilian Berti Resolução de sistemas lineares

# Exemplo: Resolva o sistema linear usando o teorema de Cramer:

2x1 + 5x2 = 12

x1 + 3x2 = 7

Temos: A =

| 2 | 5 |
| - | - |
| 1 | 3 |

e b = 12

7

D = det(A) = 6 − 5 = 1 = 0

D1 =

| 12 | 5 |
| -- | - |
| 7 | 3 |

= 36 − 35 = 1 x1 = D1 = 1

D2 =

| 2 | 12 |
| - | -- |
| 1 | 7 |

= 14 − 12 = 2 x2 = D2 = 2

Portanto, x* =

1
2

Lilian Berti Resolução de sistemas lineares

# Exemplo

x1 + x2 + x3 = 1

2x1 − x2 − 3x3 = 2

2x1 + x2 + x3 = 1

Temos: A =

| 1 | 1 | 1 |
| - | -- | -- |
| 2 | −1 | −3 |
| 2 | 1 | 1 |

x =

| x1 | 1 |
| -- | - |
| x2 | 1 |
| x3 | 1 |

Primeiramente calculamos o det(A), para utilizar o teorema de Cramer. Temos:

D = det(A) =

| 1 | 1 | 1 |
| - | -- | -- |
| 2 | −1 | −3 |
| 2 | 1 | 1 |

= −1 − 6 + 2 + 2 + 3 − 2 = −2 = 0.

Como D = 0, o sistema linear admite solução única.

Lilian Berti Resolução de sistemas lineares

# Resolução de sistemas lineares

| A | = | 2 | −1 | −3 | x | = | x2 | b | = | 2 |
| - | - | - | -- | -- | - | - | -- | - | - | - |
| 2 | 1 | 1 | x3 | | 1 | | | | | |

# Determinando a solução:

| | 1 | 1 | 1 | D1 | 0 | | | | | |
| ---- | - | -- | ----- | -- | -- | - | - | -- | - | - |
| D1 = | 2 | −1 | −3 | = | 0, | | | | | |
| | | | então | x1 | = | D | = | −2 | = | 0 |

| | 1 | 1 | 1 | D2 | −5 | 5 | | | | |
| ---- | - | - | ----- | -- | --- | - | - | -- | - | - |
| D2 = | 2 | 2 | −3 | = | −5, | | | | | |
| | | | então | x2 | = | D | = | −2 | = | 2 |

| | 1 | 1 | 1 | D3 | 3 | 3 | | | | |
| ---- | - | -- | ----- | -- | -- | - | - | -- | - | -- |
| D3 = | 2 | −1 | 2 | = | 3, | | | | | |
| | | | então | x3 | = | D | = | −2 | = | −2 |

Lilian Berti

Observação: Para n grande, seria muito trabalhoso utilizar regra de Crammer, visto que seria necessário calcular n + 1 determinantes de uma matriz de ordem n.

Assim, o estudo de métodos eficientes é necessário, pois na prática exigem a resolução de sistemas lineares de grande porte.

# Lilian Berti

# Resolução de sistemas lineares

# Sistema triangular superior

# Exemplo

x1 + 2x2 − x3 + 3x4 = 6 (I)

x2 + 3x3 − x4 = −5 (II)

5x3 + 7x4 = 21 (III)

2x4 = 6 (IV)

Por (IV), temos: x4 = 6 = 3.

2

Por (III), substituindo o valor de x4 = 3, temos:

5x3 + 7.3 = 21 =⇒ 5x3 = 21 − 21 = 0 =⇒ x3 = 0

Por (II), substituindo o valor de x4 = 3 e x3 = 0, temos:

x2 + 3.0 − 3 = −5 =⇒ x2 = −5 + 3 = −2 =⇒ x2 = −2

Por (I), substituindo o valor de x4 = 3, x3 = 0 e x2 = −2, temos:

x1 + 2.(−2) − 0 + 3.3 = 6 =⇒ x1 = 6 + 4 − 9 =⇒ x1 = 1.

Portanto, a solução do sistema linear é x = [1, −2, 0, 3]T.

Lilian Berti Resolução de sistemas lineares

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

.

.

x1 = (b1 - a12x2 - · · · - a1n−1xn−1 - a1nxn) / a11

Lilian Berti Resolução de sistemas lineares

# Resolução de sistemas lineares

Portanto,

xn = bn

xi = bi − aijxj / aii, i = n − 1, . . . , 1

Algoritmo: Resolução de sistema triangular superior.

Dados: A (matriz triangular superior), b

xn = bⁿⁿ

Para i = n, n − 1, . . . , 1

soma = bi

Para j = i + 1, i + 2, . . . , n

soma = soma − aijxj

fim para

xi = soma / aii

Fim para

Lilian Berti

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

x1 = b1 / a11

x2 = (b2 - a21x1) / a22

.

.

xn = (bn - an1x1 - an2x2 - · · · - an,n−1xn−1) / ann

Lilian Berti Resolução de sistemas lineares

# Resolução de sistemas lineares

Portanto,

x1 = b1
a11
i−1
xi = bi − ∑j=1i-1 aijxj / aii, i = 2, . . . , n

# Algoritmo: Resolução de sistema triangular inferior.

Dados: A (matriz triangular inferior), b

x1 = b1
a11
Para i = 2, 3, . . . , n
soma = bi
Para j = 1, 2, . . . , i − 1
soma = soma − aijxj
fim para
xi = soma
aii
Fim para

Lilian Berti