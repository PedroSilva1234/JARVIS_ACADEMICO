# Interpola¸c˜ao Polinomial

# Lilian Berti

# M´etodos Num´ericos

# Lilian Berti

# Interpola¸c˜ao Polinomial



# Interpola¸c˜ao Polinomial

Utilizada quando ´e necess´ario fazer estimativas de valores intermedi´arios entre dados precisos.

# Exemplo

Um ve´ıculo de fabrica¸c˜ao nacional, ap´os v´arios testes, apresentou os resultados a seguir quando analisou-se o consumo de combust´ıvel de acordo com a velocidade m´edia imposta ao ve´ıculo. Os testes foram realizados em rodovia em opera¸c˜ao normal de tr´afego, numa distˆancia de 72 km.

| velocidade (km/h) | 55    | 70    | 85    | 100   | 115   | 130   |
| ----------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| consumo (km/l)    | 14,08 | 13,56 | 13,28 | 12,27 | 11,30 | 10,40 |

Determine o consumo aproximado para o caso de desenvolvida a velocidade de 80km/h

Lilian Berti  Interpola¸c˜ao Polinomial




Dados os (n+1) pontos distintos

(x₀, f(x₀)), (x₁, f(x₁)), · · · , (xₙ , f(xₙ ))

aproximamos f(x) por um polinˆomio pn (x) de grau no m´aximo n tal que f(xi) = pn (xi), para i = 1, 2, · · · , n.

Lembrando: pn (x) = a0 + a1x + a2x² + · · · + an−1xn−1 + an xn em que ai, i = 0, 1, · · · , n s˜ao escalares.

Lilian Berti  Interpola¸c˜ao Polinomial






Para n + 1 pontos distintos existe um único polinômio pn(x) de grau no máximo n tal que pn(xi) = f(xi), para i = 0, 1, · · · , n.

Por exemplo:

- Existe uma única reta que liga dois pontos.
- Existe uma única parábola que liga três pontos ou mesmo se os pontos estiverem alinhados uma única reta.

Lilian Berti

Interpola¸c˜ao Polinomial





Forma de Lagrange para o polinˆomio de interpola¸c˜ao

Sejam x0, x1, · · · , xn, distintos. Considere os polinˆomios Li(x) de grau n, para i = 1, 2, · · · , n, dado por:

Li(x) = ( (x − x0)(x − x1) · · · (x − xi−1)(x − xi+1) · · · (x − xn )

(xi − x0)(xi − x1) · · · (xi − xi−1)(xi − xi+1) · · · (xi − xn )

Note que:

Para n = 2, temos x0, x1 e x2. Assim:

L0(x) = ((x − x1)(x − x2)

L1(x) = (x − x0)(x − x2) e

(x1 − x0)(x1 − x2)

L2(x) = ((x − x0)(x − x1)

(x2 − x0)(x2 − x1)

Lilian Berti  Interpola¸c˜ao Polinomial






# Lilian Berti

# Interpola¸c˜ao Polinomial

Temos:  (x₀ − x₁)(x₀ − x₂)

L0(x0) = (x0 − x1)(x0 − x2) = 1

L0(x1) = (x1 − x1)(x1 − x2) = 0

L0(x2) = (x2 − x1)(x2 − x2) = 0

De modo geral:

Li(x) = 0 se i = j

j = 1 se i = j





Dessa forma, para n + 1 pontos distintos (xi, f(xi)), i = 0, 1, · · · , n, temos:

pn (x) = f(x0)L0(x) + f(x1)L1(x) + · · · + f(xn )Ln (x)

o polinˆomio de interpola¸c˜ao da forma de Lagrange, sendo este polinˆomio de grau no m´aximo n e satisfazendo pn (xi) = f(xi), i = 0, 1, · · · , n.

Lilian Berti  Interpola¸c˜ao Polinomial




# Exemplo:

Dada a tabela:

|      | x | -1 | 0  | 2 |
| ---- | - | -- | -- | - |
| f(x) | 4 | 1  | -1 |   |

a) Determine um polinômio que interpola f(x) em x₀ = −1 e x₁ = 0. Calcule uma aproximação para f(−0, 3)

p₁(x) = f(x₀)L₀(x) + f(x₁)L₁(x)

temos:

L₀(x) = \(\frac{x - x₁}{x₀ - x₁}\) = \(\frac{x - 0}{-1 - 0}\) = −x

L₁(x) = \(\frac{x - x₀}{x₁ - x₀}\) = \(\frac{x + 1}{0 + 1}\) = x + 1

Logo:

p₁(x) = 4(−x) + 1(x + 1) = −3x + 1

Então, f(−0, 3) ≈ P₁(−0, 3) = 1, 9.

Lilian Berti   Interpolação Polinomial





# b) Calcule uma aproximação para f(0, 5) utilizando um polinômio de interpolação de grau 2.

Temos:

p2(x) = f(x0)L0(x) + f(x1)L1(x) + f(x2)L2(x)

| L0(x) | = ((x − x1)(x − x2) | = (x − 0)(x − 2)   | = x2 − 2x |
| ----- | ------------------- | ------------------ | --------- |
|       | (x0 − x1)(x0 − x2)  | = (−1 − 0)(−1 − 2) | = 3       |

| L1(x) | = ((x − x0)(x − x1) | = (x + 1)(x − 2) | = −x2 − x − 2 |
| ----- | ------------------- | ---------------- | ------------- |
|       | (x1 − x0)(x1 − x2)  | = (0 + 1)(0 − 2) | = 2           |

| L2(x) | = ((x − x0)(x − x1) | = (x + 1)(x − 0) | = x2 + x |
| ----- | ------------------- | ---------------- | -------- |
|       | (x2 − x0)(x2 − x1)  | = (2 + 1)(2 − 0) | = 6      |

p2(x) = 4L0(x) + 1L1(x) + (−1)L2(x)

p2(0, 5) = 4L0(0, 5) + 1L1(0, 5) + (−1)L2(0, 5)

p2(0, 5) = 4(−0.25) + 1.125 − 0.125 = 0 ≈ f(0, 5)

Lilian Berti  Interpolação Polinomial



# Exemplo

Um veículo de fabricação nacional, após vários testes, apresentou os resultados a seguir quando analisou-se o consumo de combustível de acordo com a velocidade média imposta ao veículo. Os testes foram realizados em rodovia em operação normal de tráfego, numa distância de 72 km.

| velocidade (km/h) | 55    | 70    | 85    | 100   | 115   | 130   |
| ----------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| consumo (km/l)    | 14,08 | 13,56 | 13,28 | 12,27 | 11,30 | 10,40 |

Determine o consumo aproximado para o caso de desenvolvida a velocidade de 80km/h, utilizando um polinômio interpolador de grau 2.

Lilian Berti  Interpolação Polinomial




# Temos:

p2(x) = f(x0)L0(x) + f(x1)L1(x) + f(x2)L2(x)

em que

| L0(x) = ((x − x1)(x − x2) | = (x − 85)(x − 100) | = (x − 85)(x − 100) |
| ------------------------- | ------------------- | ------------------- |
| x0 − x1)(x0 − x2)         | (70 − 85)(70 − 100) | 450                 |

| L1(x) = ((x − x0)(x − x2) | = (x − 70)(x − 100) | = (x − 70)(x − 100) |
| ------------------------- | ------------------- | ------------------- |
| x1 − x0)(x1 − x2)         | (85 − 70)(85 − 100) | −225                |

| L2(x) = ((x − x0)(x − x1) | = (x − 70)(x − 85)   | = (x − 70)(x − 85) |
| ------------------------- | -------------------- | ------------------ |
| x2 − x0)(x2 − x1)         | (100 − 70)(100 − 85) | 450                |

Logo

p2(x) = f(x0)L0(x) + f(x1)L1(x) + f(x2)L2(x)

p2(80) = 13, 56L0(80) + 13, 28L1(80) + 12, 27L2(80)

˙                  ˙                      ˙

= 13, 56(0, 2222) + 13, 28(0, 8889) + 12, 27( − 0, 1111)

= 13, 45

Portanto, quando desenvolvida a velocidade de 80km/h, o consumo aproximado é 13, 45km/l.

Lilian Berti  Interpolação Polinomial





# Diferenças Divididas

Seja f(x) uma função tabelada em n + 1 pontos distintos x0, x1, · · · , xn. Definimos o operador diferenças dividida por:

f[xi] = f(xi), i = 1, 2, · · · , n

f[x0, x1, · · · , xn] = f[x1, x2, · · · , xn] − f[x0, x1, · · · , xn−1]




Utilizando a defini¸c˜ao, temos:

f[x0, x1] = f[x1] − f[x0] = f(x1) − f(x0)
x1 − x0

f[x0, x1, x2] =
f[x1, x2] − f[x0, x1] =
f[x2] − f[x1] − f[x1] − f[x0]
x2 − x1 − x1 − x0

f[x0, x1, x2, x3] = f[x1, x2, x3] − f[x0, x1, x2]
x3 − x0

Observa¸c˜ao: f[x0, x1, · · · , xn] ´e sim´etrico nos argumentos. Por exemplo, para n = 2

f[x0, x1, x2] = f[x0, x2, x1] = f[x1, x0, x2] = f[x1, x2, x0] =
f[x2, x1, x0] = f[x2, x0, x1].

Lilian Berti  Interpola¸c˜ao Polinomial






# Esquema prático para calcular as diferenças divididas no caso n = 2.

| x  | ordem 0 | ordem 1                      | ordem 2                                  |
| -- | ------- | ---------------------------- | ---------------------------------------- |
| x0 | f\[x0]  |                              |                                          |
| x1 | f\[x1]  | x1 − x0                      | f\[x0, x1, x2] = f\[x1, x2] − f\[x0, x1] |
|    |         | f\[x1, x2] = f\[x2] − f\[x1] | x2 − x0                                  |
| x2 | f\[x2]  | x2 − x1                      | f\[x1, x2, x3] = f\[x2, x3] − f\[x1, x2] |
|    |         | f\[x2, x3] = f\[x3] − f\[x2] | x3 − x1                                  |
| x3 | f\[x3]  | x3 − x2                      |                                          |

Lilian Berti  Interpolação Polinomial






# Exemplo:

Dada a tabela

|      | -2 | -1 | 0  | 1  |
| ---- | -- | -- | -- | -- |
| f(x) | -2 | 29 | 30 | 31 |

Construir a tabela das diferenças divididas.

| x  | ordem 0 | ordem 1                  | ordem 2     | ordem 3                  |
| -- | ------- | ------------------------ | ----------- | ------------------------ |
| -2 | -2      |                          |             |                          |
| -1 | 29      | -1 - (-2) = 1 - 31 = -15 | 30 - 29 = 1 | 0 - (-2) = 0 - (-15) = 5 |
| 0  | 30      | 0 - (-1) = 1 - 1 = 0     | 1 - (-2)    | 31 - 30 = 1              |
| 1  | 31      | 1 - 0                    |             |                          |

Lilian Berti Interpolação Polinomial





Forma de Newton para o polinômio de interpolação

# pn(x) = f(x0) + (x − x0)f[x0, x1] + (x − x0)(x − x1)f[x0, x1, x2] + · · · + (x − x0)(x − x1) · · · (x − xn)f[x0, x1, x2, · · · , xn]

Lilian Berti

Interpola¸c˜ao Polinomial






Exemplo:

Dada a tabela:

|      | x  | -1 | 0  | 3 |
| ---- | -- | -- | -- | - |
| f(x) | 15 | 8  | -1 |   |

a) Calcule f(1) usando a forma de Newton para o polinômio de interpola¸c˜ao utilizando todos os pontos da tabela.

Temos três pontos para interpola¸c˜ao, segue que, o polinômio é de grau no máximo 2 (n = 2). Então:

p2(x) = f[x0] + (x − x0)f[x0, x1] + (x − x0)(x − x1)f[x0, x1, x2]

Lilian Berti  Interpola¸c˜ao Polinomial





# Construindo a tabela de diferenças divididas:

| x  | ordem 0 | ordem 1                  | ordem 2  |
| -- | ------- | ------------------------ | -------- |
| -1 | 15      |                          |          |
| 0  | 8       | 0 - (-1) = -3 - (-7) = 1 |          |
|    |         | -1 - 8 = -3              | 3 - (-1) |
|    |         | 3 - 0                    |          |
| 3  | -1      |                          |          |

Logo,

p2(x) = 15 + (x + 1) · (-7) + (x + 1)(x - 0) · 1 = x² - 6x + 8.

Dessa forma

f(1) ≈ p2(1) = 3.

Lilian Berti  Interpolação Polinomial



b) Calcule f(2) atrav´es de um polinˆomio que interpola f(x) nos pontos x0 = 0 e x1 = 3.

p1(x) = f[x0] + (x − x0)f[x0, x1] = 8 + (x − 0)(−3) = 8 − 3x

f(2) ≈ p2(2) = 2.

Lilian Berti  Interpola¸c˜ao Polinomial



Exemplo: A tabela apresenta a velocidade de queda de um paraquedista em função do tempo

| tempo (s)        | 1   | 3    | 5    | 7    | 20   |
| ---------------- | --- | ---- | ---- | ---- | ---- |
| velocidade (m/s) | 800 | 2310 | 3090 | 3940 | 8000 |

Estime o valor da velocidade no instante de tempo t = 10s utilizando um polinômio de grau 1, 2, 3 e 4 na forma de Newton.

Lilian Berti  Interpolação Polinomial




# Lilian Berti

# Interpola¸c˜ao Polinomial

Fazendo x ← t e f ← v.

# Tabela das diferen¸cas divididas

| x  | ordem 0 | ordem 1 | ordem 2 | ordem 3  | ordem 4 |         |
| -- | ------- | ------- | ------- | -------- | ------- | ------- |
| 1  | 800     |         |         |          |         |         |
| 3  | 2310    | -91,25  |         | 390      | 16,6667 |         |
| 5  | 3090    | 8,75    | -0,9275 |          | 425     | -0,9566 |
| 7  | 3940    | -7,5128 |         | 312,3077 |         |         |
| 20 | 8000    |         |         |          |         |         |







Interpolando em x0 = 7 e x1 = 20

p1(x) = f(x0) + (x − x0)f[x0, x1] = 3940 + (x − 7)312, 3077

p1(10) = 4876, 9231 ≈ f(10)

Interpolando em x0 = 5,  x1 = 7,  x2 = 20

p2(x) = f(x0) + (x − x0)f[x0, x1] + (x − x0)(x − x1)f[x0, x1, x2]

p2(x) = 3090 + (x − 5)425 + (x − 5)(x − 7)(−7, 5128)

p2(10) = 5102, 308 ≈ f(10)

Interpolando em x0 = 3,   x1 = 5,  x2 = 7,  x3 = 20

p3(x) =  f(x0) + (x − x0)f[x0, x1] + (x − x0)(x − x1)f[x0, x1, x2] + (x − x0)(x − x1)(x − x2)f[x0, x1, x2, x3]

p3(x) = 2310 + (x − 3)390 + (x − 3)(x − 5)8, 75 + (x − 3)(x − 5)(x − 7)(−0, 9566)

p3(10) = 5245, 807 ≈ f(10)

Lilian Berti  Interpola¸c˜ao Polinomial






# Interpolando em x0 = 1, x1 = 3,  x2 = 5,  x3 = 7,  x4 = 20

p4(x) =  f(x0) + (x − x0)f[x0, x1] + (x − x0)(x − x1)f[x0, x1, x2] +
(x − x0)(x − x1)(x − x2)f[x0, x1, x2, x3] + (x − x0)(x − x1)(x − x2)(x − x3)f[x0, x1, x2, x3, x4]

p4(x) = 800 + (x − 1)755 + (x − 1)(x − 3)(−91, 25) + (x − 1)(x − 3)(x − 5)(16, 6667) +
(x − 1)(x − 3)(x − 5)(x − 7)(−0, 9275)

p4(10) = 6219, 773 ≈ f(10)

Lilian Berti  Interpola¸c˜ao Polinomial





Exemplo

Um cabo sob a ação do seu próprio peso está suspenso entre dois pontos distante 24 metros. A parte mais baixa ficou a 12 metros de altura. Foram medidas diferentes alturas:

| x | -12   | -9    | -7    | -2    | 2     | 7     | 9     | 12    |
| - | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| y | 18,51 | 15,53 | 14,10 | 12,16 | 12,16 | 14,10 | 15,53 | 18,51 |

Estime a altura de 5 metros do centro.

Lilian Berti

Interpola¸c˜ao Polinomial





Pela simetria em relação ao eixo y é suficiente considerar os pontos x0 = 2, x1 = 7, x2 = 9

# Tabela das diferenças divididas

| x | ordem 0 | ordem 1 | ordem 2 |       |
| - | ------- | ------- | ------- | ----- |
| 2 | 12,16   |         | 0,388   |       |
| 7 | 14,10   | 0,0467  |         | 0,715 |
| 9 | 15,53   |         |         |       |

Pela forma de Newton para o polinômio de interpolação, temos:

p2(x) = 12,16 + (x − 2)0,388 + (x − 2)(x − 7)0,0467

Logo, p2(5) = 13,0438.

Portanto, a altura de 5 metros do centro é aproximadamente 13,0438 metros.

Lilian Berti  Interpolação Polinomial

