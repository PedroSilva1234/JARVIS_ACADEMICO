# Sistema de Equações Diferenciais

# Métodos Numéricos

Lilian Berti

Sistema de Equações Diferenciais

# Sistema de Equações Diferenciais

y = f(x, y1, y2, · · · , yn) y(x) = y1(x) = y1,0

y = f(x, y1, y2, · · · , yn) y(x) = y2(x) = y2,0

. . .

. = .

y = f(x, y1, y2, · · · , yn) y(x) = yn(x) = yn,0

Pode ser escrito

Y = f(x, Y) Y(x0) = Y0

em que

| y1(x) | f(x, Y) | y1,0 |
| ----- | ------- | ---- |
| y2(x) | f(x, Y) | y2,0 |
| . | . | . |
| . | . | . |
| yn(x) | f(x, Y) | yn,0 |

Lilian Berti

Sistema de Equações Diferenciais

Para simplicidade, e sem perda de generalidade, consideramos o caso n = 2, e para maior clareza usaremos a notação:

y1 = f(x, y, z)

z2 = f(x, y, z)

y(x0) = y0

z(x0) = z0

Assim, se o Método de Euler é utilizado para resolver este sistema acima, teremos:

yi+1 = yi + hf(xi, yi, zi)

zi+1 = zi

Lilian Berti Sistema de Equações Diferenciais

# Exemplo:

Use o método de Euler para obter uma aproximação numérica da solução do sistema de equações diferenciais:

| y | = | z | y(0) = 1 |
| - | - | ------ | -------- |
| z | = | y + ex | z(0) = 0 |

para x ∈ [0; 0, 2] com h = 0, 1.

Temos

f(x, y, z) = y z + ex

Pontos da malha: x0 = 0, x1 = 0, 1 e x2 = 0, 2

y0 = 1 e z0 = 0

Lilian Berti Sistema de Equações Diferenciais

# Método de Euler

i = 0

| y₁ | = | y₀ | + | hf(x₀, y₀, z₀) |
| -- | - | -- | ----------- | -------------- |
| z₁ | | z₀ | | |
| = | 1 | + | hf(0, 1, 0) | |
| | 0 | | | |
| = | 1 | + | 0, 1 | 0 |
| | 0 | | 2 | 0, 2 |

i = 1

| y₂ | = | y₁ | + | hf(x₁, y₁, z₁) |
| -- | - | -- | ---- | -------------- |
| z₂ | | z₁ | | |
| = | 1 | + | 0, 1 | 0, 2 |
| | | 2 | 2214 | 0, 4105 |

Portanto,

y(0, 2) ≈ 1, 02 e z(0, 2) ≈ 0, 4105

Lilian Berti Sistema de Equações Diferenciais

# Exemplo: O progresso de uma epidemia de gripe numa população

de N indivíduos é modelado pelo seguinte sistema de equações diferenciais:

| y | = | −βyz |
| - | - | -------- |
| z | = | βyz − αz |
| w | = | αz |

em que y é o número de pessoas sujeitas de pegar gripe, z é o número de pessoas infectadas e w é o número de pessoas imunes, incluindo todos os recuperados, no tempo t.

Os parâmetros α e β são as taxas de recuperação e transmissão (por dia), respectivamente. Assume-se que a população é fixa, logo no novos nascimentos são balanceados pelas mortes.

Lilian Berti Sistema de Equações Diferenciais

Considere: α = 0, 05, β = 0, 0002, y(0) = 980, z(0) = 20 e w(0) = 0.

Temos:

| y | = | −0, 0002yz |
| - | - | ------------------ |
| z | = | 0, 0002yz − 0, 05z |
| w | = | 0, 05z |

Lilian Berti Sistema de Equações Diferenciais

a) Avalie a situação da população passados 10 dias do começo da epidemia, usando o método de Runge Kutta de 2ª ordem (Euler Aperfeiçoado) com h = 5.

Pontos da malha: x0 = 0 x1 = 5 x2 = 10

y0 = 980 z0 = 20 w0 = 0

f(x, y, z, w) = 0,0002yz − 0,05z

0,05z

# Método de Euler Aperfeiçoado

Yi+1 = Yi + h (k1 + k2)

em que k1 = f(xi, Yi) e k2 = f(x + h, Y + hk1) sendo Y = zi

k1 = f(xi, Yi) e k2 = f(x + h, Y + hk1) sendo Y = zi

Lilian Berti Sistema de Equações Diferenciais

# Lilian Berti

# Sistema de Equações Diferenciais

| i | 0 | | | | | | | | | |
| -- | --- | ------ | ---------------- | -------- | --------- | ----- | ------ | -------- | - | ------- |
| | y0 | 980 | −3, 92 | | | | | | | |
| k1 | f | x0, z0 | = | f | 0, 20 | = | 2, 92 | | | |
| | w0 | 0 | 1 | | | | | | | |
| k2 | = | f | x0 + h, z0 + hk1 | w0 | | | | | | |
| | 980 | −3, 92 | 960, 4 | −6, 6460 | | | | | | |
| | = | f | 5, 20 | + 5 | 2, 92 | = | f | 5, 34, 6 | = | 4, 9160 |
| | | 0 | 1 | | 5 | 1, 73 | | | | |
| y1 | y0 | h ( ) | | | | | | | | |
| z1 | = | z0 + 2 | k1 + k2 | w1 | | | | | | |
| | 980 | 5 | −3, 92 | −6, 6460 | 953, 585 | | | | | |
| | = | 20 | + 2 | 2, 92 | + 4, 9160 | = | 39, 59 | | | |
| | 0 | 1 | | 1, 73 | 6, 825 | | | | | |

# Lilian Berti

# Sistema de Equações Diferenciais

| i | 1 | | | | | | | |
| ------ | ---------------- | ----------------- | --------- | --------- | ---------- | --------- | ---------- | --------- |
| | y1 | | | 953, 585 | −7, 5505 | | | |
| k1 = f | x1, z1 | = f | 5, 39, 59 | = 5, 5710 | | | | |
| | w1 | | | 6, 825 | 1, 9795 | | | |
| k2 = f | x1 + h, z1 + hk1 | | | | | | | |
| y1 | | 953, 585 | | −7, 5505 | 915, 8325 | −12, 3537 | | |
| = f | 10, 39, 59 + 5 | | | | 5, 5710 | = f | 5, 67, 445 | = 8, 9814 |
| | | 6, 825 | | 1, 9795 | 16, 7225 | 3, 3723 | | |
| y2 | y1 h ( ) | | | | | | | |
| z2 | = z1 + 2 k1 + k2 | | | | | | | |
| w2 | w1 | | | | | | | |
| | 953, 585 | 5 | −7, 5505 | −12, 3537 | 903, 8245 | | | |
| = | 39, 59 + 2 | 5, 5710 + 8, 9814 | | | = 75, 9710 | | | |
| | 6, 825 | | 1, 9795 | 3, 3723 | 20, 2045 | | | |

Portanto,

| y(10) | ≈ | 903, 8245 |
| ----- | - | --------- |
| z(10) | ≈ | 75, 9710 |
| w(10) | ≈ | 20, 2045 |

b) Interprete os resultados obtidos no fim de cada iteração.

Ao longo do tempo:

- o número de sujeitos a pegarem gripe (y) diminuiu
- 980 → 953, 585 → 903, 8245

o número de infectados (z) aumenta
- 20 → 39, 59 → 75, 9710

o número de pessoas (w) aumenta

Lilian Berti Sistema de Equações Diferenciais

# Exemplo:

Um paraquedista cai do avião a uma altura de 600 metros. Após 5 segundos o paraquedas abre.

A altura de queda do paraquedista como função do tempo, y(t) é dado por:

y = −g + α(t) y(0) = 600m y (0) = 0m/s

em que g = 9, 81m/s² é a aceleração da gravidade e m = 80kg é o peso do paraquedista. A resistência do ar α(t) é proporcional ao quadrado da velocidade, com diferentes constantes de proporcionalidade antes e depois da abertura do paraquedas:

α(t) = c1[y (t)]², t < 5s

α(t) = c2[y (t)]², t ≥ 5s

Considere c1 = 1/150 e c2 = 4/150. A qual altura o paraquedas abre? (Considere um espaçamento h=2,5)

Lilian Berti Sistema de Equações Diferenciais

# Fazendo uma mudança de variável: x = t

# Escrevendo o problema como um sistema de equações diferenciais com valor de inicial.

Tomando z = y. Então:

| Se x < 5 | Se x ≥ 5 |
| -------------- | --------------- |
| y = z | y = z |
| z = −9,81 + z² | z = −9,81 + 4z² |
| 80×150 | |

Lilian Berti Sistema de Equações Diferenciais

# Pontos da malha:

x0 = 0, x1 = 2, x2 = 5

y0 = y(0) = 600 z0 = y(0) = 0

# Se x &#x3C; 5

f(x, Y) = −9,81 z y2 + 12000

# Se x ≥ 5

f(x, Y) = −9,81 + 3000

# Usando o Método de Euler Aperfeiçoado

Yi+1 = Yi + h (k1 + k2)

em que k1 = f(xi, Yi) e k2 = f(x + h, Y + hk1) em que Y = yi

zi

Lilian Berti Sistema de Equações Diferenciais

# 1. Sistema de Equações Diferenciais

i = 0

k1 = f(x0, y0) = f(0, 600) = −0

z0 = 0, 9, 81

k2 = f(x0 + h, y0 + hk1) = f(2, 5; 600 + 5 − 0) = f(5, −600) = −24, 525

0 = 9, 81 24, 525 − 9, 7599

y1 = y0 + h (k1 + k2)

z1 = z0 2

= 600 + 5 − 0 + −24, 525 = 569, 3438

0 2 9, 81 − 9, 7599 − 24, 4624

Lilian Berti

# 1

i = 1

k1 = f x1, y1 = f 2, 5; 569, 3438 = −24, 4624

z1 −24, 4624 −9, 6105

k2 = f x1 + h, y1 + hk1

z1

= f 5, 569, 3438 + 5 −24, 4624 = f 5, 508, 1878 = −48, 4887

−24, 4624 −9, 6105 −48, 4887 −9, 0263

y2 = y1 + h (k1 + k2)

z2 = z1 2

= 569, 3438 + 5 −24, 4624 + −48, 4887 = 478, 1549

−24, 4624 2 −9, 6105 −9, 0263 −47, 7584

Assim, y(5) ≈ 478, 1549 e z(5) ≈ −47, 7584

Portanto, o paraquedas abre em aproximadamente 478, 1549m de altura.

Lilian Berti Sistema de Equações Diferenciais