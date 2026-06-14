# Integração Numérica

# Lilian Berti

# Métodos Numéricos

# Lilian Berti

# Integração Numérica




# Regra 1/3 de Simpson (caso n = 2)

Interpolamos f(x) usando um polinômio de grau 2 nos pontos:

x0 = a, x1 = x0 + h e x2 = x1 + h = x0 + 2h = b, sendo h = (b − a) / 2

| b                                                | x2 |
| ------------------------------------------------ | -- |
| f(x) dx ≈ p2(x) dx ≈ f(x0)A0 + f(x1)A1 + f(x2)A2 |    |
| a                                                | x0 |

em que

Ai = ∫x0x2 Li(x) dx, para i = 0, 1, 2.

Lilian Berti Integração Numérica






# Temos:

A0 =    x2 L0(x) dx =    x2 ((x − x1)(x − x2) dx

x0                 x0 − x1)(x0 − x2)

= 21 2         x2 (x − x1)(x − x2) dx

h                 x0

Fazendo uma mudança de variável, t = x − x1 ⇒ x = t + x1.

A0 = 21 2         h t(t − h) dt =    1 2       t3 − t2h   h

−h                 2h                 3                 2                 −h

= 21 2         h3 − h3         −         − h3 − h3 = h

3                 2                 3

Lilian Berti   Integração Numérica






Verifique:

A1 =    x2 L1(x) dx = 4h  e  A2 =    x2 L2(x) dx = h .

x0          3          x0          3

Portanto,

b f(x) dx ≈ f(x0) h + f(x1) 4h + f(x2) h

a          3          3          3

b f(x) dx ≈ h [f(x0) + 4f(x1) + f(x2)] = IS

a          3

Lilian Berti  Integra¸c˜ao Num´erica






# Erro:

ES = − h5 fiv(γx) para γx ∈ [x0, x2] e h = (b − a) / 2

|ES| ≤ (b − a)5 max |fiv(x)|

2880 x∈[a,b]

Lilian Berti Integração Numérica






# Exemplo:

Calcule I =  4 √x dx utilizando a regra 1/3 de Simpson.

1

Temos:

h = b − a = 1, 5

2

|   | x   | x0 | x1 | x2 |
| - | --- | -- | -- | -- |
| 1 | 2,5 | 4  |    |    |

| f(x) | 1 | √₂, 5 | 2 |
| ---- | - | ----- | - |

I ≈ h [f(x0) + 4f(x1) + f(x2)] = 4, 6622

# 3

Lilian Berti  Integra¸c˜ao Num´erica






# Erro:

|ES| ≤ (b − a)⁵ max |fiv(x)|

2880 x∈[a,b]

|E | ≤ (4 − 1)⁵ max − 15 x−⁷ = 35 · 15 = 0, 7091

S 2880 x∈[a,b] 16 2 2880 16

Lilian Berti Integra¸c˜ao Num´erica






# Regra 1/3 de Simpson repetida

Subdividimos o intervalo [a, b] em um número maior de subintervalos n = 2m em que m é o número de repetições (n ≥ 2) com n par, pois o polinômio de grau 2 requer dois subintervalos (três pontos).

b f(x) dx ≈ x2 p2(x) dx + x4 p2(x) dx + · · · + xn p2(x) dx

a x0 x2 xn−2

≈ h [f(x0) + 4f(x1) + f(x2)] + h [f(x2) + 4f(x3) + f(x4)] + · · · + h f(xn−2) + 4f(xn−1) + f(xn)

≈ h (f(x0) + f(xn) + 4(f(x1 + f(x3) + · · · + f(xn−1)) + 2(f(x2) + f(x4) + · · · + f(xn−2)) = ISR

≈ h / 3

Lilian Berti Integração Numérica






Erro

ESR = − mh5 fiv(γx) em que h = b − a = b − a

90 n 2m

Temos: m b−a h4 (b − a)h4

ESR = − 2m fiv(γx) = − fiv(γx)

90 180

|ESR| ≤ (b − a)h4 max |fiv(x)|

180 x∈[a,b]

Lilian Berti Integra¸c˜ao Num´erica





# Exemplo

Calcule I = 4 √x dx utilizando a regra 1/3 de Simpson com 4 subintervalos em a, b.

Temos:

h = b − a = 4 − 1 = 0, 75

n = 4

|      | x    | x0    | x1   | x2    | x3 | x4 |
| ---- | ---- | ----- | ---- | ----- | -- | -- |
| 1    | 1,75 | 2,5   | 3,25 | 4     |    |    |
| f(x) | 1    | √₁,75 | √₂,5 | √₃,25 | 2  |    |

I ≈ h [f(x0) + 4(f(x1) + f(x3)) + 2f(x2) + f(x4)] = 4, 6663

Lilian Berti Integração Numérica




# Erro:

|ESR| ≤ (b − a)h⁴ max |fiv(x)|

180 x∈[a,b]

|ESR| ≤ 3 · 0, 75⁴ · 15 = 0, 0049

180 16

Erro absoluto: |4, 6667 − 4, 6663| = 0, 0004

Lilian Berti Integra¸c˜ao Num´erica





Exemplo

Quantos subintervalos s˜ao necess´arios no m´ınimo para que erro seja inferior a 10−4?

|ESR| ≤ (b − a)h4 max |fiv(x)| ≤ 10−4

180 x∈[a,b]

Ent˜ao:

4 − 1 h4 · 15 ≤ 10−4 ⇒ h4 &#x3C; 6 × 10−3 ⇒ h &#x3C; 0, 2783

180 16

Como h = b − a , segue que:

3 &#x3C; 0, 2783. n

n

Logo, n > 10, 7797. Portanto, s˜ao necess´arios no m´ınimo 12 subintervalos.

Lilian Berti  Integra¸c˜ao Num´erica




# Exemplo:

Calcule I =  4 ln(x3 + √ex + 1) dx utilizando 6 subintervalos pela Regra 1/3 Simpson.

Temos:

h = 4 − 1 = 0, 5

6

| x    | x0     | x1     | x2     | x3     | x4     | x5    | x6     |
| ---- | ------ | ------ | ------ | ------ | ------ | ----- | ------ |
| x    | 1      | 1,5    | 2      | 2,5    | 3      | 3,5   | 4      |
| f(x) | 1,0744 | 1,7433 | 2,3894 | 2,9578 | 3,4529 | 3,886 | 4,2691 |

I ≈ h [f(x0) + f(x6) + 4(f(x1) + f(x3) + f(x5)) + 2(f(x2) + f(x4))] = 8, 3

5624

Lilian Berti Integração Numérica





# Regra 3/8 de Simpson

Interpolando f(x) por um polinômio de grau 3, nos pontos:

x0 = a, x1 = x0 + h, x2 = x1 + h, x3 = x2 + h = b em que h = b − a

b (  3     x3    3h

a f x) dx ≈ x0   p(x) dx = 8 [f(x0) + 3f(x1) + 3f(x2) + f(x3)] = I3/8

# Erro:

E3/8 = − 3 h5fiv(γx) em que b − a

80

E3/8 = − 3     (b − a) h4fiv(γx) = − (b − a) h4fiv(γx)

80    3                 80

|E3/8| ≤ (b − a) h4 max |fiv(x)|

80       x∈[a,b]

Lilian Berti  Integração Numérica




# Exemplo:

Calcule I =  4 √x dx utilizando a:

(a) regra 3/8 de Simpson.

h = 4 − 1 = 1

| x    | 1 | 2  | 3  | 4 |
| ---- | - | -- | -- | - |
| f(x) | 1 | √₂ | √₃ | 2 |

I ≈ 3h [f(x0) + 3f(x1) + 3f(x2) + f(x3)] = 4, 6646

8

Lilian Berti Integra¸c˜ao Num´erica





# Observação

Comparando os resultados das aproximações para I = 4, 6667:

| n = 1 | Regra do Trapézio    | I ≈ 4, 5    | EA = 0, 1    |
| ----- | -------------------- | ----------- | ------------ |
| n = 2 | Regra 1/3 de Simpson | I ≈ 4, 6622 | EA = 0, 0045 |
| n = 3 | Regra 3/8 de Simpson | I ≈ 4, 6646 | EA = 0, 0021 |

Lilian Berti

Integração Numérica




# (b) regra 1/3 de Simpson com 6 subintervalos.

h = 4 − 1 = 0, 5

6

| x    | 1 | 1,5   | 2  | 2,5   | 3  | 3,5   | 4 |
| ---- | - | ----- | -- | ----- | -- | ----- | - |
| f(x) | 1 | √₁, 5 | √₂ | √₂, 5 | √₃ | √₃, 5 | 2 |

I ≈ 0, 5 [1 + 4(√1, 5 + √2, 5 + √3, 5) + 2(√2 + √3) + 2] = 4, 6666

3

# (c) regra 3/8 de Simpson com 6 subintervalos.

I ≈ 3 · 0, 5 [1+3(√1, 5+√2)+ √2, 5+√2, 5+3(√3+√3, 5)+2] = 4, 6665

8

Lilian Berti  Integra¸c˜ao Num´erica

